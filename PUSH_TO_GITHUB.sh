#!/bin/bash
# Push The Best 2 Podcast to GitHub

cd /Users/ziverclaw96/.openclaw/workspace/best2podcast

echo "Pushing to GitHub..."

# Set remote
git remote add origin https://github.com/samuelpchristensen/thebest2podcast.git 2>/dev/null || true

# Push
git branch -M main
git push -u origin main

echo ""
echo "✅ Pushed to GitHub!"
echo ""
echo "Next: Deploy to Netlify"
echo "1. Go to https://netlify.com"
echo "2. Sign up (free)"
echo "3. 'Add new site' → 'Import from GitHub'"
echo "4. Select: samuelpchristensen/thebest2podcast"
echo "5. Click 'Deploy'"
echo ""
echo "Build settings (should auto-detect):"
echo "  Build command: cd website && hugo --gc --minify"
echo "  Publish directory: website/public"
