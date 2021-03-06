import os
import dask
import dask.distributed


def run_one(config_updates):
    from run_one import ex
    ex.run(config_updates=config_updates)


if __name__ == "__main__":
    lazy_results = []
    gammas = [0.2, 0.5, 1.0, 2.0, 5.0]
    client = dask.distributed.Client(  ## If we don't have as many cores as we have tasks this initializes a Client with the right number of cores to get the largest client we can get
        threads_per_worker=1, n_workers=int(os.environ.get("SLURM_NTASKS", len(gammas)))
    )
    for gamma in gammas:
        config_updates = {"gamma": gamma}
        lazy_results.append(dask.delayed(run_one)(config_updates))
    dask.compute(*lazy_results)
