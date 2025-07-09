#!/bin/bash

# Run the MTM Character Sheet Linux executable
# Make sure you're in the correct directory
cd "$(dirname "$0")"

# Check if the executable exists
if [ -f "./dist/MTM_Character_Sheet_Linux" ]; then
    echo "Starting MTM Character Sheet (Linux)..."
    ./dist/MTM_Character_Sheet_Linux
else
    echo "Error: MTM_Character_Sheet_Linux executable not found!"
    echo "Please build the executable first by running: ./build_linux.sh"
    exit 1
fi 