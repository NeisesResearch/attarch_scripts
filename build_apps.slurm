#!/bin/bash

#SBATCH --job-name=build_apps
#SBATCH --output=out/app_result_%A_%a.txt
#SBATCH --array=0-6
#SBATCH --mem=120G
#SBATCH --cpus-per-task=18

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

srun echo "I am running on node: $SLURMD_NODENAME"

# Change to the directory where the kernels are and run the build script
srun /bin/bash -c "cd ${basedir}/dissertation && singularity exec ${basedir}/camkes_latest.sif ./build_app.sh ${version}"

