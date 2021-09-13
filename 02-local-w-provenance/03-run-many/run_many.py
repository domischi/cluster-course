from run_one import ex # We import the experiment here. It knows what are the default values, how to run the code, and where to store it's results

for gamma in [0.2, 0.5, 1.0, 2, 0.5]:  # Over what parameters do we loop
    config_updates = { # Update the default variables (all others are still the same)
        "gamma": gamma
    }
    ex.run(config_updates=config_updates)  # Run with the updated parameters
