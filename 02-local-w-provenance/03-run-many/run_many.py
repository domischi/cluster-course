from run_one import ex ## We import the experiment here. It knows which command to run, and where to store stuff

for gamma in [0.2, 0.5, 1., 2, .5]:
    config_updates = {'gamma':gamma}
    ex.run(config_updates=config_updates)
