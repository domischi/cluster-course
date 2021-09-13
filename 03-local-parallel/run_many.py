import dask
import dask.distributed

def run_one(config_updates):
    from run_one import ex ## This will be executed on each compute instance, hence needs to be imported within the function
    ex.run(config_updates=config_updates)

# This if __name__ thing is necessary, because dask needs to make sure only the master node calls this code.
if __name__ == '__main__':
    lazy_results = [] # Define a list to hold all our simulations
    gammas = [0.2, 0.5, 1., 2, .5] # Where do we want to iterate over?
    client = dask.distributed.Client(threads_per_worker = 1, n_workers = len(gammas)) # Define a "cluster" locally, where each simulation gets 1 (logical) core, but we spawn len(gammas) of them
    for gamma in gammas:
        config_updates = {'gamma':gamma}
        lazy_results.append(dask.delayed(run_one)(config_updates)) # delayed only tells dask that this is a task it should compute eventually, but for now, let's just say sometime
    dask.compute(*lazy_results) # Now it executes all the simulations.
