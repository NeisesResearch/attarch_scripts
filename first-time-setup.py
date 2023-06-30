#!/usr/bin/env python3

import os
import shutil
import stat

# Get the path to the directory this script is in
script_path = os.path.dirname(os.path.realpath(__file__))

# Ensure the hooks directory exists
hooks_dir = os.path.join(script_path, '.repo', 'hooks')
os.makedirs(hooks_dir, exist_ok=True)

# Copy the post-sync hook
source_file = os.path.join(script_path, 'attarch_scripts', 'post-sync.py')
dest_file = os.path.join(hooks_dir, 'post-sync')
shutil.copyfile(source_file, dest_file)

# Make the post-sync hook executable
st = os.stat(dest_file)
os.chmod(dest_file, st.st_mode | stat.S_IEXEC)

