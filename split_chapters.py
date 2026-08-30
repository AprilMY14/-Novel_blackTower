#!/usr/bin/env python3
"""Extract chapters from DOCX and save as individual text files."""

import zipfile
import xml.etree.ElementTree as ET
import pathlib
import re
import sys

def extract_chapters_from_docx(docx_path):
    """Extract paragraphs from DOCX file."""
    z = zipfile.ZipFile(docx_path)
    root = ET.fromstring(z.read('word/document.xml'))
    ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    
    paras = []
    for node in root.findall('.//w:p', ns):
        texts = ''.join(t.text or '' for t in node.findall('.//w:t', ns))
        if texts.strip():
            paras.append(texts.strip())
    
    return paras

def split_into_chapters(paras):
    """Split paragraphs into chapters based on 'Chapter X' headers."""
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
    
    return chapters

def save_chapters(chapters, output_dir):
    """Save each chapter to a separate file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Found {len(chapters)} chapters\n")
    for ch_num in sorted(chapters.keys()):
        txt = chapters[ch_num]
        txt_file = output_dir / f'chapter-{ch_num:02d}.txt'
        txt_file.write_text(txt, encoding='utf-8')
        lines = len(txt.split('\n'))
        print(f"✓ Chapter {ch_num:2d}: {len(txt):8d} chars, {lines:3d} lines → {txt_file.name}")

if __name__ == '__main__':
    docx_path = pathlib.Path(r'c:\Users\Administrator\Documents\GitHub\Novel\.kiro\steering\Old files\Chapter 1 - 18.docx')
    output_dir = pathlib.Path(r'c:\Users\Administrator\Documents\GitHub\Novel\chapters\finished-book')
    
    try:
        paras = extract_chapters_from_docx(docx_path)
        print(f"Total paragraphs extracted: {len(paras)}\n")
        
        chapters = split_into_chapters(paras)
        save_chapters(chapters, output_dir)
        
        print(f"\n✅ All chapters saved to: {output_dir}")
    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)
