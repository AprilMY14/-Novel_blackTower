#!/usr/bin/env python3
"""Create HTML review files for the active version of each chapter."""

import pathlib
import re

chapter_dir = pathlib.Path('c:/Users/Administrator/Documents/GitHub/Novel/chapters/finished-book')

# Prefer remaster versions when present; otherwise fall back to the regular chapter text.
preferred_files = {}
for txt_file in sorted(chapter_dir.glob('chapter-*.txt')):
    match = re.search(r'chapter-(\d+)', txt_file.name)
    if not match:
        continue
    ch_num = int(match.group(1))
    if txt_file.name.endswith('-remaster.txt'):
        preferred_files[ch_num] = txt_file
    elif ch_num not in preferred_files:
        preferred_files[ch_num] = txt_file

for ch_num, txt_file in sorted(preferred_files.items()):
    story = txt_file.read_text(encoding='utf-8')
    lines = len(story.split('\n'))
    chars = len(story)
    is_remaster = 'remaster' in txt_file.name
    status_label = 'Remaster Active' if is_remaster else 'Legacy Source'
    html_content = f'''<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Chapter {ch_num} Review</title>
<style>
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: 100%; min-height: 100%; }}
body {{
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background: radial-gradient(circle at top, rgba(255,255,255,0.35), transparent 26%), linear-gradient(135deg, #0f172a 0%, #1e293b 26%, #312e81 72%, #4338ca 100%);
  padding: 28px; color: #0f172a; margin: 0;
}}
.page {{ max-width: 1280px; margin: 0 auto; background: rgba(255,255,255,0.94); border: 1px solid rgba(148,163,184,0.2); border-radius: 22px; box-shadow: 0 28px 80px rgba(15, 23, 42, 0.28); overflow: hidden; backdrop-filter: blur(12px); }}
.review-shell {{ display: flex; min-height: 100%; }}
.sidebar {{ width: 300px; background: linear-gradient(180deg, #0f172a 0%, #111827 100%); color: white; padding: 26px 22px 20px; display: flex; flex-direction: column; gap: 22px; }}
.eyebrow {{ font-size: 0.72rem; letter-spacing: 0.18em; text-transform: uppercase; color: #cbd5e1; opacity: 0.8; }}
.sidebar h2 {{ font-size: 1.9rem; line-height: 1.1; letter-spacing: -0.04em; }}
.meta-list {{ display: grid; gap: 12px; }}
.meta-item {{ background: rgba(148,163,184,0.08); border: 1px solid rgba(148,163,184,0.18); border-radius: 12px; padding: 10px 12px; display: flex; justify-content: space-between; align-items: center; gap: 12px; }}
.meta-item span {{ color: #cbd5e1; font-size: 0.8rem; }}
.meta-item strong {{ font-size: 0.9rem; font-weight: 700; }}
.sidebar .decision {{ margin-top: auto; display: grid; gap: 10px; }}
button {{ border: none; border-radius: 12px; font-weight: 700; font-size: 0.94rem; cursor: pointer; transition: transform 0.18s ease, box-shadow 0.18s ease, filter 0.18s ease; box-shadow: 0 12px 22px rgba(15,23,42,0.12); padding: 12px 16px; }}
button:hover {{ transform: translateY(-1px); filter: brightness(1.04); }}
.approve {{ background: linear-gradient(135deg, #10b981 0%, #059669 100%); color: white; }}
.revise {{ background: linear-gradient(135deg, #fbbf24 0%, #f59e0b 100%); color: white; }}
.reject {{ background: linear-gradient(135deg, #f87171 0%, #dc2626 100%); color: white; }}
.status {{ width: 100%; padding: 10px 12px; border-radius: 10px; font-weight: 700; text-align: center; border: 1px solid transparent; }}
.status-approved {{ background: #dcfce7; color: #166534; border-color: rgba(22,101,52,0.18); }}
.status-revise {{ background: #fef3c7; color: #92400e; border-color: rgba(146,64,14,0.2); }}
.status-rejected {{ background: #fee2e2; color: #991b1b; border-color: rgba(153,27,27,0.2); }}
.status-remaster {{ background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%); color: #92400e; border-color: rgba(146,64,14,0.24); }}
.main-panel {{ flex: 1; display: flex; flex-direction: column; background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); }}
.header {{ padding: 26px 28px 16px; border-bottom: 1px solid rgba(148,163,184,0.18); background: linear-gradient(180deg, rgba(248,250,252,0.8), rgba(255,255,255,0.95)); }}
.chapter-kicker {{ font-size: 0.72rem; letter-spacing: 0.18em; text-transform: uppercase; color: #6366f1; font-weight: 700; margin-bottom: 8px; }}
.header h1 {{ font-size: clamp(1.7rem, 2vw, 2.4rem); letter-spacing: -0.04em; margin-bottom: 12px; }}
.stats {{ display: flex; flex-wrap: wrap; gap: 10px; }}
.stats span {{ display: inline-flex; align-items: center; padding: 7px 12px; border-radius: 999px; background: #eef2ff; border: 1px solid rgba(99,102,241,0.15); color: #3730a3; font-size: 0.8rem; font-weight: 600; }}
.content {{ padding: 28px 32px 32px; font-family: 'Georgia', 'Times New Roman', serif; font-size: 17px; line-height: 1.9; letter-spacing: 0.01em; white-space: pre-wrap; word-wrap: break-word; color: #1f2937; flex: 1; }}
.content.hidden {{ display: none; }}
.editor-panel {{ display: none; padding: 28px 32px 32px; background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%); }}
.editor-panel.visible {{ display: block; }}
.editor-panel textarea {{ width: 100%; min-height: 70vh; border: 1px solid rgba(148,163,184,0.5); border-radius: 16px; padding: 18px 20px; font-size: 16px; line-height: 1.8; resize: vertical; font-family: 'Georgia', 'Times New Roman', serif; background: white; color: #111827; box-shadow: inset 0 1px 2px rgba(15,23,42,0.04); }}
.editor-actions {{ display: flex; gap: 10px; margin-top: 12px; flex-wrap: wrap; }}
.editor-actions button {{ flex: 1; min-width: 120px; }}
.save-edit {{ background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%); color: white; }}
.cancel-edit {{ background: linear-gradient(135deg, #e2e8f0 0%, #cbd5e1 100%); color: #0f172a; }}
.download-edit {{ background: linear-gradient(135deg, #6366f1 0%, #4338ca 100%); color: white; }}
@media (max-width: 900px) {{ body {{ padding: 14px; }} .review-shell {{ flex-direction: column; }} .sidebar {{ width: 100%; }} .editor-panel {{ padding: 18px 18px 20px; }} .content {{ padding: 20px 18px 24px; }} }}
@media (max-width: 640px) {{ .header {{ padding: 20px 18px 12px; }} .content {{ padding: 20px 18px 24px; font-size: 16px; }} .sidebar {{ padding: 18px 16px 16px; }} }}
</style>
</head>
<body>
<div class="page">
  <div class="review-shell">
    <aside class="sidebar">
      <div class="eyebrow">Manuscript Review</div>
      <h2>Chapter {ch_num}</h2>
      <div class="meta-list">
        <div class="meta-item"><span>Characters</span><strong>{chars:,}</strong></div>
        <div class="meta-item"><span>Lines</span><strong>{lines}</strong></div>
        <div class="meta-item"><span>Status</span><strong>{status_label}</strong></div>
        <div class="meta-item"><span>Source</span><strong>{'Remaster' if is_remaster else 'Legacy'}</strong></div>
      </div>
      <div class="decision">
        <button class="approve" onclick="approve()">✓ Approve</button>
        <button class="revise" onclick="revise()">◉ Revise</button>
        <button class="reject" onclick="reject()">✗ Reject</button>
        <div class="status { 'status-remaster' if is_remaster else '' }" id="statusMsg" style="display:block;">{status_label}</div>
      </div>
    </aside>
    <main class="main-panel">
      <div class="header">
        <div class="chapter-kicker">Review Workspace</div>
        <h1>Chapter {ch_num}</h1>
        <div class="stats">
          <span>📄 {chars:,} chars</span>
          <span>📝 {lines} lines</span>
          <span>📚 {'Remaster' if 'remaster' in txt_file.name else 'Legacy source'}</span>
        </div>
      </div>
      <div class="content" id="chapterContent">{story}</div>
      <div class="editor-panel" id="editorPanel">
        <textarea id="editBox" aria-label="Revise chapter text"></textarea>
        <div class="editor-actions">
          <button class="save-edit" onclick="saveEdits()">Save Changes</button>
          <button class="cancel-edit" onclick="cancelEdits()">Cancel</button>
          <button class="download-edit" onclick="downloadEdits()">Download .txt</button>
        </div>
      </div>
    </main>
  </div>
</div>
<script>
const chapterKey = 'ch{ch_num}';
const chapterContentKey = 'content_ch{ch_num}';
const contentBox = document.getElementById('chapterContent');
const editorPanel = document.getElementById('editorPanel');
const editBox = document.getElementById('editBox');
function renderContent(value) {{ contentBox.textContent = value; }}
function openEditor() {{ const currentText = localStorage.getItem(chapterContentKey) || contentBox.textContent; editBox.value = currentText; contentBox.classList.add('hidden'); editorPanel.classList.add('visible'); }}
function closeEditor() {{ editorPanel.classList.remove('visible'); contentBox.classList.remove('hidden'); editBox.value = ''; }}
function setStatus(state, text) {{ const msg = document.getElementById('statusMsg'); msg.textContent = text; msg.className = 'status'; if(state === 'approved') {{ msg.classList.add('status-approved'); }} else if(state === 'revise') {{ msg.classList.add('status-revise'); }} else if(state === 'rejected') {{ msg.classList.add('status-rejected'); }} msg.style.display = 'block'; }}
function approve() {{ localStorage.setItem(chapterKey, 'approved'); setStatus('approved', '✓ Approved'); closeEditor(); }}
function revise() {{ localStorage.setItem(chapterKey, 'revise'); setStatus('revise', '◉ Editing revision'); openEditor(); }}
function reject() {{ if(confirm('Reject this chapter?')) {{ localStorage.setItem(chapterKey, 'rejected'); setStatus('rejected', '✗ Rejected'); closeEditor(); }} }}
function saveEdits() {{ const updatedText = editBox.value; localStorage.setItem(chapterContentKey, updatedText); renderContent(updatedText); closeEditor(); setStatus('revise', '✓ Revision saved'); }}
function cancelEdits() {{ closeEditor(); setStatus('revise', '◉ Revision cancelled'); }}
function downloadEdits() {{ const text = localStorage.getItem(chapterContentKey) || contentBox.textContent; const blob = new Blob([text], {{ type: 'text/plain;charset=utf-8' }}); const url = URL.createObjectURL(blob); const a = document.createElement('a'); a.href = url; a.download = 'chapter-{ch_num}-revised.txt'; document.body.appendChild(a); a.click(); a.remove(); URL.revokeObjectURL(url); }}
window.addEventListener('load', () => {{ const savedText = localStorage.getItem(chapterContentKey); if(savedText) {{ renderContent(savedText); }} const status = localStorage.getItem(chapterKey); if(status === 'approved') {{ setStatus('approved', '✓ Approved'); }} else if(status === 'revise') {{ setStatus('revise', '◉ Marked for revision'); }} else if(status === 'rejected') {{ setStatus('rejected', '✗ Rejected'); }} }});
</script>
</body>
</html>'''

    review_file = chapter_dir / f'chapter-{ch_num:02d}-review.html'
    review_file.write_text(html_content, encoding='utf-8')
    print(f"✓ chapter-{ch_num:02d}-review.html from {txt_file.name}")

print(f"\n✅ Created {len(preferred_files)} active chapter review files")
