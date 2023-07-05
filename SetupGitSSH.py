import os
import re
import subprocess

# Start at the current directory
root_dir = os.getcwd()

# Iterate over all the directories in the current directory
for folder in os.listdir(root_dir):
    # If it's one of the specified directories
    if re.match(r'\d+\.\d+\.y', folder):
        # Change into the directory
        os.chdir(os.path.join(root_dir, folder))

        # If there is a .git directory in the current directory
        if '.git' in os.listdir():
            # Open the .git/config file
            with open('.git/config', 'r') as file:
                # Read the file's content
                file_data = file.read()

            # Replace the URL
            file_data = re.sub(r'url =https://github.com/ku-sldg/attarch',
                               r'url =git@github.com:ku-sldg/attarch',
                               file_data)

            # Write the new content back to the file
            with open('.git/config', 'w') as file:
                file.write(file_data)

            # Checkout the appropriate branch
            subprocess.call(['git', 'checkout', 'linux-' + folder])

        # Change back to the root directory
        os.chdir(root_dir)

