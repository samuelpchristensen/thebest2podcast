#!/bin/bash
# Deploy The Best 2 Podcast website

set -e

echo "Building The Best 2 Podcast website..."

cd website

# Check if Hugo is installed
if ! command -v hugo &> /dev/null; then
    echo "Hugo not found. Installing..."
    brew install hugo
fi

# Build the site
echo "Building site..."
hugo --gc --minify

# Check if build succeeded
if [ ! -d "public" ]; then
    echo "Build failed - public directory not found"
    exit 1
fi

echo "Build successful!"
echo ""
echo "To deploy:"
echo "1. Push to GitHub: git push origin main"
echo "2. Connect to Netlify/Vercel"
echo "3. Or copy public/ to your web server"
echo ""
echo "Local preview: hugo server"
