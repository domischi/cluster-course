from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np
import os


DATA_DIR = "./data"
os.makedirs(DATA_DIR, exist_ok=True)

# Let's define the right-hand side of the equation
def RHS(t, y, m, gamma, k):
    return np.array([y[1], -(gamma * y[1] + k * y[0]) / m])


def do_one_parameter_config(m, gamma, k, t_min=0.0, t_max=25.0, y0=1.0, dydt0=0.0, SAVE=False):
    T = np.linspace(t_min, t_max, 101)
    sol = solve_ivp(
        RHS, t_span=(t_min, t_max), y0=(y0, dydt0), args=(m, gamma, k), t_eval=T
    )
    plt.figure()
    plt.plot(T, sol["y"][0])
    plt.xlabel(r"$t$", fontsize=14)
    plt.ylabel(r"$x$", fontsize=14)
    plt.title(f"$m={m:.2e},~\gamma={gamma:.2e},~k={k:.2e}$")
    if SAVE:
        plt.savefig(f"{DATA_DIR}/very-important-figure-{m=:.2f}_{gamma=:.2f}_{k=:.2f}.png")
        plt.close()
    else:
        plt.show()


for gamma in [0.1, 0.5, 1, 2, 10]:
    do_one_parameter_config(1, gamma, 1, SAVE=True)
