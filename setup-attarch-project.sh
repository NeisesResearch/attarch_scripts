#!/bin/bash

set -e

# Clone the git repository
echo "Cloning the attarch_scripts repository..."
git clone https://github.com/NeisesResearch/attarch_scripts.git

# Initialize the repository
echo "Initializing the repository..."
repo init -u https://github.com/ku-sldg/attarch-manifest.git -b measurement_integration

# Sync the repository
echo "Syncing the repository..."
repo sync

# Ensure the slurm output directories are available
mkdir -p out
mkdir -p results

# Ensure Python3 is installed and available
if ! command -v python3 &> /dev/null
then
    echo "Python3 could not be found. Please ensure it's installed and available in the system path."
    exit 1
fi

# Run the first-time setup script from the attarch_scripts repository
echo "Running the first-time setup script..."
python3 ./attarch_scripts/first-time-setup.py

# Move the Simulate.sh file to the parent directory
echo "Moving build scripts..."
mv ./attarch_scripts/simulate_all.slurm .
mv ./attarch_scripts/build_app.sh .
mv ./attarch_scripts/buildLinux.py ./linux-kernels/
mv ./attarch_scripts/build_linux.slurm .

# Remove the attarch_scripts repository
echo "Cleaning up..."
rm -rf ./attarch_scripts

echo "Script completed successfully."

