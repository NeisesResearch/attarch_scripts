import os
import glob

# Current working directory
repo_test_dir = os.getcwd()

attarch_dirs = glob.glob(os.path.join(repo_test_dir, 'attarch', '*.*.y'))
am_cakeml_dir = 'am-cakeml'
vm_examples_dir = os.path.join('projects', 'vm-examples', 'apps', 'Arm')

# Create a symlink in projects/vm-examples/apps/Arm/ that corresponds to each of attarch-4.9, attarch-4.14, etc.
for attarch_dir in attarch_dirs:
    attarch_version = os.path.basename(attarch_dir)
    symlink_name = os.path.join(repo_test_dir, vm_examples_dir, f'attarch-{attarch_version}')
    relative_attarch_dir = os.path.join(os.path.relpath('attarch', start=vm_examples_dir), attarch_version)

    if not os.path.exists(symlink_name):
        os.symlink(relative_attarch_dir, symlink_name)
    else:
        print(f"Symlink {symlink_name} already exists, skipping...")

    # Create a symlink in each attarch directory that corresponds to the am-cakeml directory.
    am_cakeml_symlink = os.path.join(attarch_dir, 'am-cakeml')
    relative_am_cakeml_dir = os.path.relpath('am-cakeml', start=f'attarch/{attarch_version}')

    if not os.path.exists(am_cakeml_symlink):
        os.symlink(relative_am_cakeml_dir, am_cakeml_symlink)
    else:
        print(f"Symlink {am_cakeml_symlink} already exists, skipping...")

    # Create a symlink in each attarch directory called "linux-stable" that points to the appropriate linux kernel.
    linux_stable_symlink = os.path.join(attarch_dir, 'linux-stable')
    relative_linux_stable_dir = os.path.relpath(f'linux-kernels/{attarch_version}', start=f'attarch/{attarch_version}')

    if not os.path.exists(linux_stable_symlink):
        os.symlink(relative_linux_stable_dir, linux_stable_symlink)
    else:
        print(f"Symlink {linux_stable_symlink} already exists, skipping...")

lines_to_append = """
RUN curl -L https://github.com/CakeML/cakeml/releases/download/v2076/cake-x64-32.tar.gz > cake-x64-32.tar.gz \\
    && tar -xvzf cake-x64-32.tar.gz && cd cake-x64-32 && make cake \\
    && mv cake /usr/bin/cake32

RUN curl -L https://github.com/CakeML/cakeml/releases/download/v2076/cake-x64-64.tar.gz > cake-x64-64.tar.gz \\
    && tar -xvzf cake-x64-64.tar.gz && cd cake-x64-64 && make cake \\
    && mv cake /usr/bin/cake64
"""

filename = "seL4-CAmkES-L4v-dockerfiles/dockerfiles/extras.Dockerfile"

with open(filename, 'a') as file:
    file.write(lines_to_append)

