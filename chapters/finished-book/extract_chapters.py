import zipfile
import xml.etree.ElementTree as ET
import pathlib
import re

# Extract DOCX
docx_path = r'c:\Users\Administrator\Documents\GitHub\Novel\.kiro\steering\Old files\Chapter 1 - 18.docx'
z = zipfile.ZipFile(docx_path)
root = ET.fromstring(z.read('word/document.xml'))
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# Get all paragraphs
paras = []
for node in root.findall('.//w:p', ns):
    texts = ''.join(t.text or '' for t in node.findall('.//w:t', ns))
    if texts.strip():
        paras.append(texts.strip())

# Split into chapters - look for "Chapter X" pattern
chapters = {}
current_chapter = None
current_content = []

for para in paras:
    match = re.match(r'^Chapter\s+(\d+)', para, re.IGNORECASE)
    if match:
        # Save previous chapter
        if current_chapter is not None:
            chapters[current_chapter] = '\n\n'.join(current_content)
        # Start new chapter
        current_chapter = int(match.group(1))
        current_content = [para]
    elif current_chapter is not None:
        current_content.append(para)

# Save last chapter
if current_chapter is not None:
    chapters[current_chapter] = '\n\n'.join(current_content)

# Create output folder and files
out = pathlib.Path(r'c:\Users\Administrator\Documents\GitHub\Novel\chapters\finished-book')
out.mkdir(parents=True, exist_ok=True)

print(f"Found {len(chapters)} chapters")
for ch_num in sorted(chapters.keys()):
    txt = chapters[ch_num]
    # Save text file
    txt_file = out / f'chapter-{ch_num:02d}.txt'
    txt_file.write_text(txt, encoding='utf-8')
    print(f"✓ Chapter {ch_num:2d}: {len(txt):6d} chars - {txt_file.name}")

print(f"\nAll chapters saved to: {out}")
