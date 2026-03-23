#!/bin/bash
# Deploy The Best 2 Podcast to Netlify
# Run this after buying thebest2podcast.com

echo "🚀 The Best 2 Podcast - Deployment Script"
echo "=========================================="

# Check if git repo exists
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
fi

# Add all files
echo "Adding files to git..."
git add .

# Commit
echo "Committing..."
git commit -m "Website ready for deployment - thebest2podcast.com"

# Instructions for GitHub
echo ""
echo "=========================================="
echo "NEXT STEPS:"
echo "=========================================="
echo ""
echo "1. Create GitHub repository:"
echo "   - Go to https://github.com/new"
echo "   - Name: thebest2podcast"
echo "   - Make it public"
echo "   - DON'T initialize with README"
echo ""
echo "2. Connect and push:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/thebest2podcast.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Deploy to Netlify:"
echo "   - Go to https://netlify.com"
echo "   - Sign up (free)"
echo "   - 'Add new site' → 'Import from GitHub'"
echo "   - Select your repo"
echo "   - Click 'Deploy'"
echo ""
echo "4. Add custom domain:"
echo "   - In Netlify: Site settings → Domain management"
echo "   - Add: thebest2podcast.com"
echo "   - Update DNS at your registrar"
echo ""
echo "=========================================="
echo "Your site is ready at:"
echo "   /Users/ziverclaw96/.openclaw/workspace/best2podcast/website/public/"
echo "=========================================="
