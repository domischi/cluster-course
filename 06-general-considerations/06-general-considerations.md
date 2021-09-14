# Some general considerations when you want to run large simulations
Disclaimer: This is personal opinion, at the time of writing (September 20201), and does not represent those of people, institutions or organizations that I may or may not be associated with in a professional or personal capacity, unless explicitly stated. Furthermore, I acknowledge to overgeneralize and as such the information here is provided on an "as is" basis with no guarantees of completeness accuracy, usefulness or timeliness.

## Cluster vs. Cloud
Cluster:
- is cheaper
- is easier to setup
- allows great scaling if necessary
- has already access to many software licences you need as a researcher

Cloud can be used in specialized instances easier:
- Want to have a dedicated machine to do something -> EC2
- Need something that is always accessible -> EC2 / EB
- Need to host a database -> RDS
- Need fairly large storage -> S3
- Need the latest and greatest GPU to fit an ML model -> EC2 with a specialized instance

Generally though, cluster will serve you better if you want to run simulations.

## "Reasonable" Size for simulations
To give a rough idea how large simulations are typically done in the field of computational sciences
- 1k CPU hours: Quick verification of a theoretical model, simplified model to explain experiments.
- 10k CPU hours: Doing a thorough study of something that is explained theoretically (still an add-on to a paper, not main content)
- 100k CPU hours: Doing a mainly numerical study
- 1M CPU hours: Doing an in-depth numerical study with a provably hard system to simulate (e.g., NP hard). Such studies typically require additional funding, and here it starts to make sense to start thinking about optimizing code beyond using the optimal algorithm (i.e., using specialized libraries, rewriting parts in compiled languagues, thinking about memory layout...)

## How to size individual SLURM submissions
- Storage on the cluster only starts costing at fairly large data sizes (10s of TB, [Source](https://www.hpc.caltech.edu/rates))
- Standard submissions do not include GPU. If you have machine learning applications or use libraries that can use GPU, then it might make sense to ask SLURM for a GPU (include "#SBATCH --gres=gpu:1" in the submission script)
- Standard submissions come with limited RAM (typically around 1GB per core). Usually the default is sufficient. If you see your code crashing because of too little available memory, you can try to increase it (include "#SBATCH --mem-per-cpu=xG" in the submission script, where x is the number of GB you need in memory)
- Time: Ask for around twice the time you expect your code to run. Typically you get scheduled quite fast, but if there's a high load on the cluster it can take a bit to get a job started (rarely more than a few hours).
- While additional features such as GPUs and sometimes memory (not at Caltechs cluster at the time of writing) will be charged extra, time is computed by time used, not time asked for. Therefore, no problem in asking for more time than required. Only downside: Can take longer to get execution scheduled.

## What to store?
Generally speaking: Enough but not too much. My rule of thumb:
- Store scalar data in every loop. (Though not necessarily do the write to harddrive every loop, but just keeping a tab on what you want to store)
- Store complete data dumps more sparsely (if at all). Here, consider how long it takes to write a complete data dump, and compare this to the runtime of a single simulation loop iteration. Make sure you spend more time on actual simulation than data dumping.
- When you write data, make sure to do it somewhat clever. Generating a plot with matplotlib and storing it takes easily a second, so you don't want to make plots every iteration. Storing a data dump in a file you can append to great. Do you have to read and rewrite entire files (e.g. json files)? Maybe switch to another format.
- To give an indication: Smaller projects for me are around 10-100MB for providing model support for experiments. Numerically focused papers produce for me around 1-10GB of data, which can still easily be uploaded to open source data repositories such as the [Caltech data repository](https://data.caltech.edu/) or [Zenodo](https://zenodo.org/).

## How to store?
There are many formats to store scientific simulation data. If you work with something specific (CAD, GIS, gene-expression data, ...) use the standard format in the field and don't reinvent the wheel. If you work with some more general data there are several options:
- Raw binary files: Extremely fast, can easily be appended, but really not save to work with. Data gets easily corrupted, no one can analyze the data not having exactly your code and software versions. Don't do this!
- Raw ASCII encoded files: Can easily be appended, but not as fast as raw binary files. Still, typically you only store numbers here, but it can be unclear what they mean. Again, usually not a great way to store data.
- CSV files: Can easily be appended, but requires a fairly rigid data strucuture. If you just want to save a table or a matrix, then this is a great solution, but if you need to save scalars, vectors, and arbitrary objects within each loop, CSV files become unruly.
- Python pickled data: In theory, this would be a decent way of storing the data. However, appending is difficult so each loop should generate a new file. Additionally, different versions of pickle are incompatible with each other, and as such it again can be difficult to work with. Can only really be opened in Python and as such requires whoever wants to verify the data also to work in Python.
- JSON data: Used in this tutorial for simplicity of use. Can store things such as dictionaries or lists natively (need to convert numpy arrays though). Cannot easily be appended, and should also generate a new file each loop. Can be opened in many different programming and scripting languages, and as such provides a good interface.
- HDF5 data: Binary data format, specifically designed for scientific data. As such it can easily be appended, and is very quick for analysis. However, due to its specialization it is a bit more difficult to work with, and well developed libraries and tutorials only exist for commen scientific languages (Fortran, Python, C/C++, Julia, ...) but maybe not in some more commercial languages / applications.
In conclusion: If you have heavy IO needs, go with HDF5 as it can be appended to, and is very fast. If you have strucutred data and you don't require meta data to be stored, go with CSV. If you need a catch-all solution, store a dictionary as we did in the tutorial in json format in each loop.
