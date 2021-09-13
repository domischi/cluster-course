1. Let's upload the contents of this folder to the cluster

    `rsync -azhru --info=progress2 ../04-cluster-parallel-w-dask` <your-user-name>@<cluster-name>:~/

2. Upload the `requirements.txt` to the cluster

    `rsync -azhru --info=progress2 ../requirements.txt` <your-user-name>@<cluster-name>:~/

3. Let's start working on the cluster.
    1. Login to the cluster

        `ssh <your-user-name>@<cluster-name>`

    2. Install the required packages (for simplicity, we don't do anything like a virtualenv, but it would work without issues, just remember to load it in submission scripts if you go down this path)

        `pip install -r requirements.txt`

    3. Make your scratch folder (fast memory, make sure all simulations run there, src can be located somewhere else but for simplicity, we just move everything there)

        `mkdir /scratch/<your-user-name>; ln -s /scratch/<your-user-name> ~/scratch;`

    4. Move all simulation data to scratch and change directory there

        `mv 04-cluster-parallel-w-dask scratch/; cd scratch/04-cluster-parallel-w-dask` 

    5. We reuse the same parameter sweep as in our example 03, so no change required in any of the python files, however we need to change our submission script. Edit this with the editor of your choice (vim/emacs/nano/...)
        - The first lines in submit.sh are variables for the submission script (i.e. command line arguments you'd pass when submitting)
        - Here, ntasks says how many cpu cores the virtual machine will get. In our case we want to have one core per simulation to be as quick as we can. Hence 5. Note we could give a lower number and dask would figure out how to allocate, but using more isn't helpful as we do not have more than 5 tasks.
        - We also want to change the time variable to be long enough that our simulation surely finishes, but small enough that we do get scheduled quickly. My rule of thumb: twice the amount of time that I expect the simulation to run.
        - Change your email address in mail-user and you get notified when the job starts and finishes.
        - The lower part of the script is basically just what the cluster needs to execute on the command line. We go fairly basic, but have a few debugging lines outputting things such as the environment variables.
    6. Schedule the job to be executed (due to the small size, we should get very quickly scheduled)

        `sbatch submit.sh`

    7. Check the status of your job:

        `squeue -u <your-user-name>`

       If the list is empty your job is already executed and finished. If not, ST will give you the status of the job. Here the most important ones: R is running, PD is pending, CG is finishing up
4. Once it's finished (either bc you receive the finished mail, or because you see squeue being empty), download the data again to be local. I.e., not on the cluster but on a local terminal session, download the data.

    `rsync -azhru --info=progress2 <your-user-name>@<cluster-name>:~/scratch/04-cluster-parallel-w-dask/data .`

    Make sure you download the data timely after the simulation finished (typically within 30 days) as scratch will get purged regularly to empty space
5. Now you can look at the data locally as you did before.
