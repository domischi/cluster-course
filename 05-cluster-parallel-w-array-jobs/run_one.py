import sacred
from sacred.observers import FileStorageObserver
from simulation_logic import do_one_parameter_config

ex = sacred.Experiment('simulation')
ex.observers.append(FileStorageObserver('data'))

@ex.config
def cfg():
    m = 1.
    gamma = 0.
    k = 1.
    t_min = 0.
    t_max = 15.
    y0 = 1.
    dydt0 = 0.

@ex.main ## Important: Here we removed the auto from automain -> it's not automagically called
def run_one_simulation(_config, _run):
    do_one_parameter_config(
            m=_config['m'],
            gamma=_config['gamma'],
            k=_config['k'],
            t_min=_config['t_min'],
            t_max=_config['t_max'],
            y0=_config['y0'],
            dydt0=_config['dydt0'],
            SAVE=True,
            ex=ex
            )

