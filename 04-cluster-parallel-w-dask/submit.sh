#!/bin/bash
#SBATCH --job-name="Harmonic Oscillator"
#SBATCH --ntasks=<number of simulations> # How many simulations do you need to run
#SBATCH --time=00:00:05                  # Time can also be more than 24 hours by using a format like days-hours:minutes:seconds. Note that there's a maximal time limit and you will not get scheduled if it's too long
#SBATCH --mail-type=ALL
#SBATCH --mail-user=<your-mail-address>  # Where do you want to get your mails to?
#SBATCH --output=out                     # In what file to store the output?
#SBATCH --error=out                      # And where to store the error messages (here we pipe them in the same file for simplicity)
#======START===============================
source ~/.bashrc
echo "The current job ID is $SLURM_JOB_ID"
echo "Running on $SLURM_JOB_NUM_NODES nodes: $SLURM_JOB_NODELIST"
echo "A total of $SLURM_NTASKS tasks is used"
echo "Environment Variables"
env
CMD="python3 run_many.py"
echo $CMD
$CMD
#======END================================= 
