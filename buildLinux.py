#!/usr/bin/env python3

import os
import sys
import subprocess

def clean_files():
    for f in [".config", ".config.old", "Module.symvers"]:
        try:
            os.remove(f)
        except OSError:
            pass  # If the file does not exist, we don't need to do anything

def copy_config_files():
    try:
        print(os.getcwd())
        subprocess.check_call("cp  ../../projects/camkes-vm-images/qemu-arm-virt/linux_configs/config .config", shell=True)
        subprocess.check_call("cp .config .config.old", shell=True)
    except Exception as e:
        print(f"Failed to copy or backup config file\n{e}")
        exit(1)

def update_config():
    try:
        subprocess.check_call("yes '' | make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- oldconfig", shell=True)
    except Exception as e:
        print(f"Failed to update .config file\n{e}")
        exit(1)

def prepare_source():
    try:
        subprocess.check_call("make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- prepare", shell=True)
    except Exception as e:
        print(f"Failed to prepare source tree for compilation\n{e}")
        exit(1)

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
    subprocess.check_call("make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- clean", shell=True)
    clean_files()
    copy_config_files()
    update_config()
    prepare_source()
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

