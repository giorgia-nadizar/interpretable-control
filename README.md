****# Interpretable Control
Repository for the GECCO'24 interpretable control competition.

## Install
Clone the repository and create the conda virtual environment with all needed packages.
```shell
git clone https://github.com/giorgia-nadizar/interpretable-control.git
cd interpretable-control
conda env create -f environment.yml
conda activate ic38
```
To render the 'Walker2d' gym environment you might need to run the following within your conda environment:
```shell
conda install -c conda-forge libstdcxx-ng
```

## Content

### Continuous control track
The `continuous` package contains files for the continuous control track of the competition.
- `continuous_controller.py` has a general controller class (which you can extend with your own implementation) and a random controller for testing purposes
- `walker_example.py` shows the basic evaluation loop for the chosen environment, the `Walker2d-v4`

The competition's final evaluation will be performed with the same environment (`Walker2d-v4`) and episode length 
(1000 steps) as in the `walker_example.py` file.

### Discrete control track
The `discrete` package contains file for the discrete control track of the competition.
