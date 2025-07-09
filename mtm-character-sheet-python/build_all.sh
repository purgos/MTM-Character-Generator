#!/bin/bash

echo "Building MTM Character Sheet for both Linux and Windows..."

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

# Build Linux executable
echo "Building Linux executable..."
pyinstaller character_sheet_linux.spec

# Note: Windows executable can only be built on Windows
echo ""
echo "Linux build complete! The Linux executable is in the dist/ folder."
echo "For Windows executable, please:"
echo "1. Copy this project to a Windows machine"
echo "2. Run build_windows.bat on Windows"
echo ""
echo "Linux executable: ./dist/MTM_Character_Sheet_Linux" 