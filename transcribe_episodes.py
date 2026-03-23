#!/usr/bin/env python3
"""
Transcribe The Best 2 Podcast episodes using OpenAI Whisper API
Usage: python3 transcribe_episodes.py
"""

import os
import sys

# Episodes to transcribe
EPISODES = [
    {
        "name": "Brad Wilcox - Teacher, Author, Speaker",
        "youtube_id": "geDmF4AslpU",
        "episode": 13,
        "file": "ep13-brad-wilcox"
    },
    {
        "name": "Steven Sharp Nelson - Cello Guy", 
        "youtube_id": "3BM8zSXGK2s",
        "episode": 12,
        "file": "ep12-steven-sharp-nelson"
    },
    {
        "name": "Thomas B. Griffith - Lawyer & Federal Judge",
        "youtube_id": "1cKn7NnXXz8",
        "episode": 3,
        "file": "ep3-thomas-b-griffith"
    }
]

def check_api_key():
    """Check if OpenAI API key is set"""
    api_key = os.environ.get('OPENAI_API_KEY')
    if not api_key:
        print("❌ ERROR: OPENAI_API_KEY not set!")
        print("\nTo set your API key:")
        print("  export OPENAI_API_KEY='sk-...'")
        print("\nGet your API key at: https://platform.openai.com/api-keys")
        print("\nEstimated cost: ~$0.50-1.00 for 3 episodes (~3 hours)")
        sys.exit(1)
    return api_key

def download_audio(episode):
    """Download audio from YouTube"""
    import subprocess
    
    print(f"\n📥 Downloading: {episode['name']}")
    
    cmd = [
        "yt-dlp",
        "-x", "--audio-format", "mp3",
        "-o", f"transcripts/audio/{episode['file']}.%(ext)s",
        f"https://youtube.com/watch?v={episode['youtube_id']}"
    ]
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        print(f"❌ Download failed: {result.stderr}")
        return False
    
    print(f"✅ Downloaded: {episode['file']}.mp3")
    return True

def transcribe_audio(episode):
    """Transcribe audio using OpenAI Whisper"""
    from openai import OpenAI
    
    client = OpenAI()
    audio_path = f"transcripts/audio/{episode['file']}.mp3"
    
    print(f"🎙️  Transcribing: {episode['name']}")
    
    try:
        with open(audio_path, "rb") as audio_file:
            transcript = client.audio.transcriptions.create(
                model="whisper-1",
                file=audio_file,
                response_format="text"
            )
        
        # Save transcript
        output_path = f"transcripts/text/{episode['file']}.txt"
        with open(output_path, "w") as f:
            f.write(transcript)
        
        print(f"✅ Transcribed: {len(transcript)} characters")
        print(f"💾 Saved to: {output_path}")
        
        return transcript
        
    except Exception as e:
        print(f"❌ Transcription failed: {e}")
        return None

def update_episode_file(episode, transcript):
    """Update episode markdown file with transcript"""
    episode_file = f"website/content/episodes/{episode['file']}.md"
    
    if not os.path.exists(episode_file):
        print(f"⚠️  Episode file not found: {episode_file}")
        return
    
    with open(episode_file, 'r') as f:
        content = f.read()
    
    # Replace placeholder with actual transcript
    placeholder = "*[Transcript will be added here once transcribed]*"
    
    # Format transcript for markdown
    formatted_transcript = f"""## Full Transcript

{transcript}

---

*Transcribed by OpenAI Whisper*"""
    
    content = content.replace(placeholder, formatted_transcript)
    
    with open(episode_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Updated: {episode_file}")

def main():
    """Main transcription workflow"""
    print("=" * 60)
    print("🎙️  The Best 2 Podcast - Transcription Tool")
    print("=" * 60)
    
    # Check API key
    check_api_key()
    
    # Create directories
    os.makedirs("transcripts/audio", exist_ok=True)
    os.makedirs("transcripts/text", exist_ok=True)
    
    print(f"\n📋 Episodes to transcribe: {len(EPISODES)}")
    print(f"💰 Estimated cost: ~${len(EPISODES) * 0.30:.2f}")
    
    for i, episode in enumerate(EPISODES, 1):
        print(f"\n{'='*60}")
        print(f"Episode {i}/{len(EPISODES)}: {episode['name']}")
        print(f"{'='*60}")
        
        # Check if already transcribed
        transcript_path = f"transcripts/text/{episode['file']}.txt"
        if os.path.exists(transcript_path):
            print(f"⏭️  Already transcribed. Skipping...")
            with open(transcript_path, 'r') as f:
                transcript = f.read()
        else:
            # Download audio
            if not download_audio(episode):
                continue
            
            # Transcribe
            transcript = transcribe_audio(episode)
            if not transcript:
                continue
        
        # Update episode file
        update_episode_file(episode, transcript)
    
    print(f"\n{'='*60}")
    print("✅ All done! Transcripts added to episode files.")
    print(f"{'='*60}")
    print("\nNext steps:")
    print("  1. Review transcripts in website/content/episodes/")
    print("  2. Make any edits needed")
    print("  3. Deploy: cd website && hugo server")

if __name__ == "__main__":
    main()
