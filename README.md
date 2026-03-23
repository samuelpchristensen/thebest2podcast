# The Best 2 Podcast Website

A modern, SEO-optimized website for The Best 2 Podcast built with Hugo.

## Features

- **SEO-optimized** transcript pages for search engine discoverability
- **Responsive design** that works on all devices
- **Fast loading** static site (no database needed)
- **YouTube integration** with embedded players
- **Episode navigation** (previous/next)
- **Clean, modern design** matching the podcast branding

## Structure

```
best2podcast/
├── website/                    # Hugo site
│   ├── content/
│   │   ├── episodes/          # Episode pages with transcripts
│   │   ├── about.md           # About page
│   │   └── subscribe.md       # Subscribe page
│   ├── themes/best2/          # Custom theme
│   │   ├── layouts/           # HTML templates
│   │   └── assets/css/        # Styles
│   └── hugo.toml              # Site config
├── episodes.json              # Episode data from YouTube
├── generate_episodes.py       # Script to generate episode files
└── transcribe_episodes.sh     # Script to transcribe videos
```

## Local Development

### Prerequisites

```bash
# Install Hugo
brew install hugo

# Install Python (for transcription)
brew install python

# Install yt-dlp (for downloading videos)
brew install yt-dlp
```

### Run Locally

```bash
cd website
hugo server
```

Site will be available at http://localhost:1313

## Deployment

### Option 1: Netlify (Recommended)

1. Push to GitHub
2. Connect repo to Netlify
3. Build command: `hugo`
4. Publish directory: `public`

### Option 2: GitHub Pages

1. Push to GitHub
2. Enable GitHub Pages
3. Use GitHub Actions for automated deployment

### Option 3: Vercel

1. Import GitHub repo to Vercel
2. Framework preset: Hugo
3. Build command: `hugo --gc --minify`

## Adding Transcripts

### Method 1: YouTube Auto-Captions (Free)

1. Go to YouTube Studio
2. Select video → Subtitles
3. Download .srt file
4. Convert to markdown and paste into episode file

### Method 2: Whisper API (Best Quality)

```bash
# Install whisper
pip install openai-whisper

# Download and transcribe
yt-dlp -x --audio-format mp3 [YOUTUBE_URL]
whisper audio.mp3 --model medium --output_format txt
```

### Method 3: Use transcribe_episodes.sh

Edit the script with your OpenAI API key, then:

```bash
./transcribe_episodes.sh
```

## SEO Benefits

Each transcript page includes:
- Full episode text (searchable)
- Schema.org PodcastEpisode markup
- Proper heading structure
- Meta descriptions
- Open Graph tags for social sharing

This makes episodes discoverable via Google search for specific topics discussed.

## Customization

### Colors
Edit `website/themes/best2/assets/css/main.css`:
- `--color-primary: #C41E3A` (red from logo)

### Logo
Replace `website/static/images/logo.png`

### Content
Edit files in `website/content/`

## Domain Setup

1. Purchase domain (e.g., best2podcast.com)
2. Add to hosting platform (Netlify/Vercel)
3. Configure DNS
4. Enable HTTPS

## Analytics

Add Google Analytics or Plausible to track:
- Episode popularity
- Transcript page views
- Search traffic sources

## Support

For questions or issues, contact Samuel Christensen.
