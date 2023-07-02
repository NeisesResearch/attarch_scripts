# Dissertation Project Script Collection

This repository houses a collection of scripts that manage my dissertation project. To set up a complete development and testing environment for the app (except for the Docker container), invoke the following command:

```bash
bash <(curl https://raw.githubusercontent.com/NeisesResearch/attarch_scripts/master/setup-attarch-project.sh)
```

## Requirements

### Running the Script

- **Bash Shell:** The script is a Bash script and requires a Bash-compatible shell to run it.

- **Git:** The script clones a Git repository, so Git must be installed. [Download Git](https://git-scm.com/)

- **Repo Command Line Tool:** This script uses the Repo command-line tool, built on top of Git for managing multiple repositories. [Repo Documentation](https://source.android.com/setup/develop/repo)

- **Python3:** The script requires Python3. [Download Python3](https://www.python.org/)

- **Internet Access:** The script fetches repositories from the internet, requiring a functioning internet connection.

- **File System Permissions:** The script performs file operations, requiring read, write, and execute permissions in the file system.

### Building the Project

- **Docker Container:** A Docker container is necessary for building the project. Details about setup and usage can be found in the [seL4 Dockerfiles documentation](https://docs.sel4.systems/projects/dockerfiles/).

## Repository Contents

- **buildLinux.py:** This Python script cleans and performs a fresh build of the Linux kernel. It supports versions 4.9.y, 4.14.y, 4.19.y, 5.4.y, 5.10.y, 5.15.y, and 6.1.y. The script accepts input of one or more versions or "lts" (excluding the 4.y series). It also accepts "all" as input to build all supported kernel versions.

- **build_app.sh:** This Bash script automates the process of updating and building the application from scratch. It requires input of one specific kernel version to tailor the app building and testing process.

- **build_linux.slurm:** This script is designed for High-Performance Computing (HPC) environments. It uses the Slurm workload manager to automate the building process of all supported Linux kernel versions.

- **first-time-setup.py:** This script is automatically invoked during the initial project setup (via `curl <(bash .../setup-attarch-project.sh)`), establishing the necessary file system structure by creating essential symbolic links. This file is deleted post-setup, requiring no further user interaction.

- **setup-attarch-project.sh:** This is the project's primary setup script. It downloads and initializes the entire project when invoked via curl. Post-setup, it leaves the Linux kernel build process selection to the user, providing the option to use `build_app.sh` for building the application after the Linux kernel build.
