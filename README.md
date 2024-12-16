# A Brain-Inspired Model of Reaching and Adaptation on the iCub Robot

Code for the paper: \
Fietzek, T., Ruff, C., & Hamker, F. H. (2024). \
**A Brain-Inspired Model of Reaching and Adaptation on the iCub Robot.** \
2024 IEEE International Symposium on Robotic and Sensors Environments (ROSE), 1–7. \
https://doi.org/10.1109/ROSE62198.2024.10591174


Adapted from the code: \
https://github.com/hamkerlab/Baladron2023-MotorLearning-BG-Cereb

Baladron, J., Vitay, J., Fietzek, T., & Hamker, F. H. (2023). \
**The contribution of the basal ganglia and cerebellum to motor learning: A neuro-computational approach.** \
PLOS Computational Biology, 19(4), e1011024. \
https://doi.org/10.1371/journal.pcbi.1011024



## Dependencies

The code depends on
 - the neuro-simulator ANNarchy (Artificial Neural Networks architect) version 4.7.2.
    - Installation instructions for Linux and MacOS are available in the official ANNarchy documentation: <https://annarchy.github.io/>
 - the YARP/iCub Software version 3.6.
    - Installation instructions can be found at: <https://github.com/robotology/robotology-superbuild?tab=readme-ov-file#binary-installation>
 - the ANNarchy-iCub interface version >=1.1.0.
    - Installation instructions are available in the documentation: <https://annarchy.github.io/ANNarchy-iCub/d4/d6d/md_Installation.html>

The versions for ANNarchy and YARP are relative flexible, but there could appear problems with higher/lower versions.


## Simulations

The code in the folder `code/` contains the model definitions and implements the reaching and adaptation tasks.

### Reaching Task:
The number of goals in the reaching task (2, 4 and 8 in the manuscript) can be changed at the beginning of `run_reaching.py`.

The simulation can be started by execution the following python script:
```bash
python run_reaching.py
```

### Adaptation Task:

The simulation conditions (shift on/off; online/offline learning; take images while experiment is running) can be set at the beginning of `run_adaption.py`

The simulation can be started by execution the following python script:
```bash
python run_adaptation.py
```

#### Preparation for simulations with simulated iCub and simulator experiment images:
For the online adaption experiment in the gazebo classic simulator add the following line to the .bashrc file and replace path_to_repo with the path to the cloned repository
export GAZEBO_MODEL_PATH=${GAZEBO_MODEL_PATH}:path_to_repo/code/gazebo_conf/
Then gazebo can be started with one of the start_simulator_ scripts.

```bash
bash start_simulator_no_gui.sh # or
bash start_simulator_no_gui_screen.sh # start the simulator in a screen session
```


### Hints:

The scripts will initialize the random concrete action, run the initial basal ganglia training and then run the full model simulation with 2 or 8 goals using the cerebellar reservoir. A full simulation will take **several hours**.

The code has been tested on Linux Ubuntu 22.4 Mint 21.3 20.3, using python 3.10 and 3.8 and ANNarchy version 4.7. We cannot assure that it will work on other versions.


