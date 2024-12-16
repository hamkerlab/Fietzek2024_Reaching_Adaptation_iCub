"""
Code for the paper:

Fietzek, T., Ruff, C., & Hamker, F. H. (2024).
A Brain-Inspired Model of Reaching and Adaptation on the iCub Robot.


Script to run multiple simulations in parallel.

> python run_multi_sim.py
"""

from subprocess import Popen


num_trials = 20 # total number of simulations
offset = 0 # simulation id to start from
max_prcs_count = 4 # maximum parallel simulations -> take care of number of processor cores

script = 'run_adaptation.py' # 'run_reaching.py' # select either reach or adaption task

prcs = []
try:
    idx = offset
    while(idx < num_trials+offset):
        if len(prcs) < max_prcs_count:
            prcs.append(Popen(['python3', script, str(idx)]))
            idx += 1
        else:
            ret = prcs[0].wait()
            if type(ret) == int:
                prcs.pop(0)

    for process in prcs:
        process.wait()

except KeyboardInterrupt:
    print("interrupted")
    for process in prcs:
        process.terminate()
