#!/bin/bash
set -e  # Exit on any error

# Create virtual environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install uv
uv pip install -r requirements.txt

# Create models directory and download models
mkdir -p models
python scripts/download_models.py

# Start docker containers
docker compose up --build -d

echo -e "\nSetup complete! The TTS service should be available at http://localhost:5002" 