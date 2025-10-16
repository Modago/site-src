#!/bin/bash

# Build the site
echo "Building site..."
pelican content -s publishconf.py

# Deploy to modago.github.io repo (master/main branch)
echo "Deploying to GitHub Pages..."
ghp-import -b master output -p -r pages

echo "Done! Site published to https://modago.github.io"