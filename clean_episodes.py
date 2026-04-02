#!/usr/bin/env python3
"""
Clean up episode markdown files
Removes duplicate headings, placeholder text, and redundant content
"""

import os
import re
import glob

EPISODES_DIR = "/Users/ziverclaw96/.openclaw/workspace/best2podcast/website/content/episodes"

def clean_episode_file(filepath):
    """Clean up a single episode file"""
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if not frontmatter_match:
        print(f"Skipping {filepath}: no frontmatter found")
        return
    
    frontmatter = frontmatter_match.group(1)
    body = content[frontmatter_match.end():]
    
    # Remove duplicate "## Full Transcript" headings
    body = re.sub(r'## Full Transcript\s*\n\s*## Full Transcript', '## Full Transcript', body)
    
    # Remove placeholder transcript instructions
    placeholder_pattern = r'\n*To get this episode transcribed:.*?Paste transcript here for SEO benefits\n*'
    body = re.sub(placeholder_pattern, '\n\n', body, flags=re.DOTALL)
    
    # Remove "*[Transcript will be added here once transcribed]*" placeholder
    body = re.sub(r'\*\[Transcript will be added here once transcribed\]\*\n*', '', body)
    
    # Remove empty transcript section if no actual transcript content
    if '## Full Transcript' in body and not body.split('## Full Transcript')[1].strip():
        body = body.split('## Full Transcript')[0].strip()
    
    # Clean up multiple consecutive blank lines
    body = re.sub(r'\n{3,}', '\n\n', body)
    
    # Write cleaned content
    cleaned_content = frontmatter + body
    
    with open(filepath, 'w') as f:
        f.write(cleaned_content)
    
    print(f"✅ Cleaned: {os.path.basename(filepath)}")

def main():
    """Process all episode files"""
    episode_files = glob.glob(os.path.join(EPISODES_DIR, "ep*.md"))
    
    print(f"Found {len(episode_files)} episode files\n")
    
    for filepath in sorted(episode_files):
        clean_episode_file(filepath)
    
    print(f"\n✅ All {len(episode_files)} episodes cleaned!")

if __name__ == "__main__":
    main()
