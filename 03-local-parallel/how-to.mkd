Now we want to make it parallel, first only locally
1. Make sure you do not write the same file from all process. In our example, change `DATA_DIR` in `simulation_logic.py` to something unique. Here, we use uuid (safe to use everywhere)
2. Change automain to main in `run_one.py`. Otherwise, it can lead to problems as we now need to define our own `__main__`.
3. Run the `run_many.py` that initializes a dask task list and then executes it by calling
    `python run_many.py`
