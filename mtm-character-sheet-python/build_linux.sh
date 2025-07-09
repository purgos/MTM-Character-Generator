#!/bin/bash

echo "Building MTM Character Sheet for Linux..."

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 is not installed"
    echo "Please install Python 3.8+ first"
    exit 1
fi

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Build the executable
echo "Building Linux executable..."
pyinstaller character_sheet_linux.spec

echo ""
echo "Build complete! The Linux executable is in the dist/ folder."
echo "You can run it with: ./dist/MTM_Character_Sheet_Linux" 