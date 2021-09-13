import sacred
from sacred.observers import FileStorageObserver
from simulation_logic import do_one_parameter_config

ex = sacred.Experiment("simulation")
ex.observers.append(FileStorageObserver("data"))  ## We want to store data as files in the folder data

## Think of this as your default configuration
## Every variable defined in this function is handled magically by the provenance system
@ex.config
def cfg():
    m     = 1.0
    gamma = 0.0
    k     = 1.0
    t_min = 0.0
    t_max = 15.0
    y0    = 1.0
    dydt0 = 0.0


@ex.automain  ## This tells python to use ex as our provenance system and to call this function as the main function
def run_one_simulation(_config, _run):
    # _config contains all the variables you define in cfg
    # _run contains data about the run
    do_one_parameter_config(
        m=_config["m"],  ## I know, that's quite cumbersome. For larger simulations, I recommend passing just a parameter dictionary (i.e., _config) and let the downstream functions extract their parameters
        gamma=_config["gamma"],
        k=_config["k"],
        t_min=_config["t_min"],
        t_max=_config["t_max"],
        y0=_config["y0"],
        dydt0=_config["dydt0"],
        SAVE=True,  ## We want to save (see logic in 02_simulation_logic.py)
        ex=ex,  ## Pass over the experiment handler ex
    )
