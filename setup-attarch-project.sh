#!/bin/bash

set -e

# Step 1: Initialize the repository
echo "Initializing the repository..."
repo init -u https://github.com/ku-sldg/attarch-manifest.git -b measurement_integration

# Step 2: Sync the repository
echo "Syncing the repository..."
repo sync

# Ensure Python3 is installed and available
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please ensure it's installed and available in the system path."
    exit 1
fi

# Step 3: Run the Python3 script
echo "Running the first-time setup script..."
python3 ./tools/attarch/first-time-setup.py

echo "Script completed successfully."

