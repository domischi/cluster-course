import os
import json


def run_one(config_updates):
    from run_one import (
        ex,
    )  ## This will be executed on each compute instance, hence needs to be imported within the function

    ex.run(config_updates=config_updates)


with open("queue.json", "r") as f:
    simulation_parameter_list = json.load(f)

# get which job we need to do. The int is necessary because environment variables are stored as strings
run_id = int(os.environ.get("SLURM_ARRAY_TASK_ID"))

# Only use the config update we need to work on
config_updates = simulation_parameter_list[run_id]

# Now run it
run_one(config_updates)
