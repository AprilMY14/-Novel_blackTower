$serverSource = @'
using System;
using System.IO;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;

public static class FinishedBookServer {
    private static readonly string Root = @"C:\Users\Administrator\Documents\GitHub\Novel";

    public static void Main() {
        var listener = new TcpListener(IPAddress.Loopback, 8000);
        listener.Start();
        Console.WriteLine("Finished Book is running at http://localhost:8000/chapters/finished-book/");
        Console.WriteLine("Keep this window open. Press Ctrl+C to stop the server.");
        while (true) {
            TcpClient client = listener.AcceptTcpClient();
            ThreadPool.QueueUserWorkItem(_ => Handle(client));
        }
    }

    private static void Handle(TcpClient client) {
        using (client)
        using (NetworkStream stream = client.GetStream())
        using (var reader = new StreamReader(stream, Encoding.ASCII, false, 1024, true)) {
            string request = reader.ReadLine();
            if (String.IsNullOrEmpty(request)) return;

            string[] parts = request.Split(' ');
            string requested = parts.Length > 1 ? parts[1] : "/";
            int query = requested.IndexOf('?');
            if (query >= 0) requested = requested.Substring(0, query);

            string relative = Uri.UnescapeDataString(requested).TrimStart('/').Replace('/', Path.DirectorySeparatorChar);
            if (relative.Length == 0) relative = "index.html";

            string path = Path.GetFullPath(Path.Combine(Root, relative));
            int status = 200;
            string statusText = "OK";
            if (!path.StartsWith(Root + Path.DirectorySeparatorChar, StringComparison.OrdinalIgnoreCase)) {
                status = 403; statusText = "Forbidden";
            } else if (Directory.Exists(path)) {
                path = Path.Combine(path, "index.html");
            }
            if (status == 200 && !File.Exists(path)) {
                status = 404; statusText = "Not Found";
            }

            byte[] body = status == 200 ? File.ReadAllBytes(path) : Encoding.UTF8.GetBytes(statusText);
            string extension = Path.GetExtension(path).ToLowerInvariant();
            string contentType = extension == ".html" ? "text/html; charset=utf-8" : extension == ".txt" ? "text/plain; charset=utf-8" : "application/octet-stream";
            byte[] header = Encoding.ASCII.GetBytes("HTTP/1.1 " + status + " " + statusText + "\r\nContent-Type: " + contentType + "\r\nContent-Length: " + body.Length + "\r\nConnection: close\r\n\r\n");
            stream.Write(header, 0, header.Length);
            stream.Write(body, 0, body.Length);
        }
    }
}
'@

try {
    Add-Type -TypeDefinition $serverSource -ErrorAction Stop
    [FinishedBookServer]::Main()
}
catch [System.Net.Sockets.SocketException] {
    Write-Host "Port 8000 is already being used. Open http://localhost:8000/chapters/finished-book/ or close the other server first."
}
