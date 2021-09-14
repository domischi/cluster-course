This is some exemplary material on how to run simulations on the (Caltech) cluster. In particular, this course uses an exemplary tech stack of 
- [SLURM](https://slurm.schedmd.com/documentation.html) for cluster side scheduling
- [Dask](https://dask.org/) for some local and cluster side parallization
- [Sacred](https://sacred.readthedocs.io/en/stable/index.html) for simulation provenance
- [Jupyter Notebook](https://jupyter.org/) for interactive python
It should be noted that there are many other great solutions for all of these tasks, and this is merely a suggestion of what one can use.

For this course, the curriculum is as follows:
- In 01 we introduce the problem via an interactive jupyter notebook. 
- In 02 we introduce experiment provenance with sacred. 
- In 03 we parallelize our application locally.
- In 04 we port the application to the cluster using the same software stack as used locally.
- In 05 we port the application using the array-job capability of slurm for the simplest parallelization on the cluster.
- In 06 we discuss some general considerations when we make certain design choices (opinion piece, see disclaimer there)

The expectation is that after going through this course, you have the knowledge and some templates to run your own code on the cluster, and that you know which paramters affect what behavior on the cluster.
