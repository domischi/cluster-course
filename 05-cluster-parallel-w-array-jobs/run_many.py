import os
import json

def run_one(config_updates):
    from run_one import ex ## This will be executed on each compute instance, hence needs to be imported within the function
    ex.run(config_updates=config_updates)

with open('queue.json', 'r') as f:
    simulation_parameter_list = json.load(f)

run_id = int(os.environ.get('SLURM_ARRAY_TASK_ID')) # get which job we need to do. The int is necessary because environment variables are stored as strings
config_updates = simulation_parameter_list[run_id] # Only use the config update we need to work on
run_one(config_updates) # Now run it
