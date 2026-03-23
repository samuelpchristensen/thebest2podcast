#!/usr/bin/env python3
"""
Generate episode markdown files from episodes.json
Also handles YouTube video download and transcription
"""

import json
import os
import re
from datetime import datetime, timedelta

# Load episodes data
with open('episodes.json', 'r') as f:
    data = json.load(f)

episodes = data['episodes']

# Template for episode markdown
EPISODE_TEMPLATE = """---
title: "{title}"
guest: "{guest}"
episode: {episode}
location: "{location}"
duration: "{duration}"
youtube_id: "{youtube_id}"
date: {date}
---

{guest} shares insights from their mission in {location} and how those experiences shaped their career and life.

## About {guest}

{guest} is featured in this episode of The Best 2 Podcast, sharing how their mission experience influenced their personal and professional journey.

## Key Topics

- Mission experiences in {location}
- Career development and growth
- Personal transformation through service
- Lessons learned and applied

## Watch the Episode

<iframe width="100%" height="400" src="https://www.youtube.com/embed/{youtube_id}" title="{guest} - The Best 2 Podcast" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

## Full Transcript

*[Transcript will be added here once transcribed]*

To get this episode transcribed:
1. Download audio from YouTube
2. Use Whisper API or similar service
3. Paste transcript here for SEO benefits
"""

def slugify(text):
    """Convert text to URL-friendly slug"""
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    return re.sub(r'[-\s]+', '-', text)

def parse_duration(duration_str):
    """Convert duration string to approximate minutes"""
    if 'hour' in duration_str.lower():
        if ',' in duration_str or 'and' in duration_str.lower():
            # "1 hour, 2 minutes" format
            parts = duration_str.replace(',', '').split()
            hours = int(parts[0])
            mins = int(parts[2]) if len(parts) > 2 else 0
            return hours * 60 + mins
        else:
            return 60
    else:
        # "45 minutes" format
        return int(duration_str.split()[0])

def parse_date(published_str):
    """Convert relative date to approximate ISO date"""
    now = datetime.now()
    if 'year' in published_str:
        years = int(published_str.split()[0]) if published_str[0].isdigit() else 1
        return (now - timedelta(days=years*365)).strftime('%Y-%m-%dT00:00:00Z')
    elif 'month' in published_str:
        months = int(published_str.split()[0]) if published_str[0].isdigit() else 1
        return (now - timedelta(days=months*30)).strftime('%Y-%m-%dT00:00:00Z')
    else:
        return now.strftime('%Y-%m-%dT00:00:00Z')

def extract_guest_name(title):
    """Extract guest name from episode title"""
    # Pattern: "Ep. X: Name - Title | Location"
    match = re.search(r'Ep\.\s*\d+:\s*([^-]+)', title)
    if match:
        return match.group(1).strip()
    return title

def generate_episode_file(episode):
    """Generate markdown file for an episode"""
    episode_num = episode['episode']
    title = episode['title']
    guest = extract_guest_name(title)
    location = episode['location']
    duration = episode['duration']
    youtube_id = episode['youtube_id']
    published = episode['published']
    
    # Create filename
    slug = slugify(f"ep{episode_num}-{guest}")
    filename = f"website/content/episodes/{slug}.md"
    
    # Generate date
    date = parse_date(published)
    
    # Generate content
    content = EPISODE_TEMPLATE.format(
        title=title,
        guest=guest,
        episode=episode_num,
        location=location,
        duration=duration,
        youtube_id=youtube_id,
        date=date
    )
    
    # Write file
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w') as f:
        f.write(content)
    
    print(f"Generated: {filename}")
    return filename

def generate_transcript_script():
    """Generate a script to download and transcribe episodes"""
    script = """#!/bin/bash
# Transcription workflow for The Best 2 Podcast
# Requires: yt-dlp, ffmpeg, and OpenAI API key

EPISODES_DIR="transcripts"
mkdir -p "$EPISODES_DIR"

# Function to transcribe a video
transcribe_video() {
    local youtube_id=$1
    local output_name=$2
    
    echo "Processing: $output_name (ID: $youtube_id)"
    
    # Download audio
    yt-dlp -x --audio-format mp3 -o "$EPISODES_DIR/${output_name}.%(ext)s" \
        "https://youtube.com/watch?v=$youtube_id"
    
    # Transcribe with Whisper (requires OpenAI API key)
    # whisper "$EPISODES_DIR/${output_name}.mp3" --model medium --output_format txt
    
    echo "Completed: $output_name"
}

# Example usage:
# transcribe_video "geDmF4AslpU" "ep13-brad-wilcox"

echo "Transcription script ready. Uncomment lines and add API key to use."
"""
    
    with open('transcribe_episodes.sh', 'w') as f:
        f.write(script)
    os.chmod('transcribe_episodes.sh', 0o755)
    print("Generated: transcribe_episodes.sh")

# Generate all episode files
print("Generating episode files...")
for episode in episodes:
    generate_episode_file(episode)

# Generate transcription script
generate_transcript_script()

print(f"\nGenerated {len(episodes)} episode files")
print("Next steps:")
print("1. Install Hugo: brew install hugo")
print("2. cd website && hugo server")
print("3. To transcribe episodes, edit transcribe_episodes.sh and run it")
