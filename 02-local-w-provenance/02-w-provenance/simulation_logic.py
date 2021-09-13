from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import os

## Important: Work on a temporary directory, as you now handle storage over the provenance system
DATA_DIR = '/tmp/work_dir'
os.makedirs(DATA_DIR, exist_ok=True)

def RHS(t, y, m, gamma, k):
    return np.array([y[1], -(gamma*y[1]+k*y[0])/m])

## Important: pass the sacred experiment as a parameter
def do_one_parameter_config(m, gamma, k, t_min=0., t_max=25., y0=1., dydt0=0., SAVE=False, ex=None):
    T = np.linspace(t_min, t_max, 101)
    sol=solve_ivp(RHS, t_span=(t_min, t_max), y0=(y0,dydt0), args=(m, gamma, k), t_eval=T)
    plt.figure()
    plt.plot(T, sol['y'][0])
    plt.xlabel(r'$t$', fontsize=14)
    plt.ylabel(r'$x$', fontsize=14)
    plt.title(f'$m={m:.2e},~\gamma={gamma:.2e},~k={k:.2e}$')
    if SAVE:
        fname = f'{DATA_DIR}/very-important-figure.png' ## Important: We no longer need to handle file names ourself
        plt.savefig(fname)
        if ex is not None:
            ex.add_artifact(fname)
        plt.close()
    else:
        plt.show()
