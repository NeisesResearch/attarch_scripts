#!/usr/bin/env python3

import os
import sys
import subprocess

def compile_kernel():
    try:
        subprocess.check_call(f"make -j{os.cpu_count()} ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu-", shell=True)
    except Exception as e:
        print(f"Failed to compile the kernel\n{e}")
        exit(1)

def build_version(version):
    print(f"Building version {version}")
    try:
        os.chdir(version)
    except OSError as e:
        print(f"Failed to change directory to: {version}\n{e}")
        return
    compile_kernel()
    os.chdir("..")  # Go back to the parent directory

# Define the versions
all_versions = ["4.9.y", "4.14.y", "4.19.y", "5.4.y", "5.10.y", "5.15.y", "6.1.y"]
lts_versions = [v for v in all_versions if v != "4.9.y"]

# Get the version argument
try:
    arg = sys.argv[1]
except IndexError:
    print("Please provide a version argument")
    exit(1)

# Determine which versions to build
if arg == "all":
    versions = all_versions
elif arg == "lts":
    versions = lts_versions
elif arg in all_versions:
    versions = [arg]
else:
    print(f"Invalid argument {arg}")
    exit(1)

# Build the chosen versions
os.chdir("linux-kernels")
for version in versions:
    build_version(version)

