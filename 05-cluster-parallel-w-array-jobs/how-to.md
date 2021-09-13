1. We could still use the strategy to generate the parameter list in every client and then only select the one we would like. However, it's often beneficial to have all parameters you'd like to tune over saved as a queue file. Here we generate one by `generate-queue.py` and get the results stored in `queue.json`
2. Let's upload the contents of this folder to the cluster
    `rsync -azhru --info=progress2 ../05-cluster-parallel-w-array-jobs` <your-user-name>@<cluster-name>:~/
2. Let's start working on the cluster.
    1. Login to the cluster
        `ssh <your-user-name>@<cluster-name>`
    2. If you followed along you should have the scratch directory already
    3. Move all simulation data to scratch and change directory there
        `mv 05-cluster-parallel-w-array-jobs scratch/; cd scratch/05-cluster-parallel-w-array-jobs` 
    4. `simulation_logic.py` and `run_one.py` are unchanged. The `run_many.py` now just looks which job it should do, and ignores all others. The logic becomes considerably simpler and you never waste CPU time.
    5. `submit-array.sh` still needs to be adapted:
        - Here, ntasks is 1, as every instance only gets one core to work with
        - However, we need an array of jobs, hence setting the array flag with the number of array jobs
        - We also want to change the time variable to be long enough that our simulation surely finishes, but small enough that we do get scheduled quickly. My rule of thumb: twice the amount of time that I expect the simulation to run.
        - Change your email address in mail-user and you get notified when the job starts and finishes.
    5. Schedule the job to be executed (due to the small size, we should get very quickly scheduled)
        `sbatch submit-array.sh`
    6. Check the status of your job:
        `squeue -u <your-user-name>`
       If the list is empty your job is already executed and finished. If you're quick enough, you see 5 jobs all running, but all having the main number <underscore> their array index. This allows you to see which jobs are still running. Possibly not all run at the same time, but it's handled flexibly by the cluster
3. Once it's finished (either bc you receive the finished mail, or because you see squeue being empty), download the data again to be local. I.e., not on the cluster but on a local terminal session, download the data.
    `rsync -azhru --info=progress2 <your-user-name>@<cluster-name>:~/scratch/05-cluster-parallel-w-array-jobs/data .`
    Make sure you download the data timely after the simulation finished (typically within 30 days) as scratch will get purged regularly to empty space
4. Now you can look at the data locally as you did before.
