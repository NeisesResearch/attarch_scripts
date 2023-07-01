#!/bin/bash

#SBATCH --job-name=build_kernels
#SBATCH --output=out/build_result_%A_%a.txt
#SBATCH --array=0-6
#SBATCH --cpus-per-task=20

versions=(
"4.9.y"
"4.14.y"
"4.19.y"
"5.4.y"
"5.10.y"
"5.15.y"
"6.1.y"
)

# Get the version for this array task
version=${versions[$SLURM_ARRAY_TASK_ID]}
basedir="/panfs/panfs.ittc.ku.edu/scratch/m811n155/"

# Change to the directory where the kernels are and run the build script
srun /bin/bash -c "cd ${basedir}/dissertation/linux-kernels && singularity exec ${basedir}/camkes_latest.sif python3 ./buildLinux.py ${version}"

