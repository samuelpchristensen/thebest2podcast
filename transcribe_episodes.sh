#!/bin/bash
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
    yt-dlp -x --audio-format mp3 -o "$EPISODES_DIR/${output_name}.%(ext)s"         "https://youtube.com/watch?v=$youtube_id"
    
    # Transcribe with Whisper (requires OpenAI API key)
    # whisper "$EPISODES_DIR/${output_name}.mp3" --model medium --output_format txt
    
    echo "Completed: $output_name"
}

# Example usage:
# transcribe_video "geDmF4AslpU" "ep13-brad-wilcox"

echo "Transcription script ready. Uncomment lines and add API key to use."
