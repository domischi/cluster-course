- 01: Here we just clean the simulation. If you execute the python file, you just get the final figures produced by the script. I.e., execute 

      python cleaned-simulation.py

    and you get the figures stored in a new folder data

- 02: Here we start using a data provenance system, in particular we use [Sacred](https://sacred.readthedocs.io/en/stable/index.html)
    - For this we start separating the 'run an individual simulation' logic from the actual simulation code. 
    - Starting with `simulation_logic.py` the changes we did:
        - Change to a temporary work dir. You don't want your code to write directly to the results folder, but let this be handled by the provenance solution.
        - To your simulation code, handle the data provenance by passing `ex` as an optional parameter. Then in the code, make sure to store the artifacts such as plots (or raw data files) using `ex.add_artifact`
        - You no longer need to make sure all filenames are unique. This is now handled by the provenance system. Hence, we can name our figure still 'very-important-figure.png' for every run.
    - `run_one.py` contains the logic to run a single simulation. Detailed comments in the file on how this needs to be written. To run the example, execute

          python run_one.py

- 03: Let's do parameter sweeps fully provenanced
    - `simulation_logic.py` requires no change because we separated the run logic from the simulation logic
    - `run_one.py` requires no change but is no longer the exectued file.
    - Now the logic to execute the parameter swee is in `run_many.py`. (Detailed comments in the file) To execute this example run

          python run_many.py
