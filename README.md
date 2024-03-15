# Interpretable Control
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

## Repository content

### Continuous control track
The `continuous` package contains files for the continuous control track of the competition.
- `continuous_controller.py` has a general controller class (which you can extend with your own implementation) and a random controller for testing purposes
- `example_walker.py` shows the basic evaluation loop for the chosen environment, the `Walker2d-v4`

The competition's final evaluation will be performed with the same environment (`Walker2d-v4`) and episode length 
(1000 steps) as in the `walker_example.py` file.

### Discrete control track
The `discrete` package contains file for the discrete control track of the competition.
- `discrete_controller.py` has a general controller class (which you can extend with your own implementation) and a random controller for testing purposes
- `example_2048.py` shows the basic evaluation loop for the 2048 environment

Note that if you want to employ this environment outside the `discrete` package you need to import such package.

The 2048 environment can have illegal moves, you can decide the behavior of the environment with the argument
`terminate_with_illegal_move`.
The competition's final evaluation will be performed with `terminate_with_illegal_move=True`, i.e., we will terminate
the evaluation if the policy performs an illegal move.

## Task details

### Continuous control: Walker2D

For more details on the 'Walker2D' we refer to the official documentation on the Gymnasium website:
[https://gymnasium.farama.org/environments/mujoco/walker2d/](https://gymnasium.farama.org/environments/mujoco/walker2d/).


### Discrete control: 2048

As discrete control task we chose the game [2048](https://en.wikipedia.org/wiki/2048_(video_game)), for which we 
implemented a Gym-like interface.
For further details on the game play we refer to the Wikipedia page of the game 
[https://en.wikipedia.org/wiki/2048_(video_game)](https://en.wikipedia.org/wiki/2048_(video_game)).

The **action space** is a `Discrete(4)`, each corresponding to a movement direction, and a keyboard key (if the game
was playing by a human on a PC):

| Value | Meaning | Button |
|-------|---------|--------|
| `0`   | `UP`    | `W`    |
| `1`   | `DOWN`  | `S`    |
| `2`   | `LEFT`  | `A`    |
| `3`   | `RIGHT` | `D`    |

The **observation space** is a `Box(0, 2048, (4, 4), int)`, corresponding to the current status of the game board.

At each step, the `reward` consists of the score increase determined by the move.

Within the `info`, there are other game play details:
- `direction`: the direction of the last move (as button)
- `spawn`: the location (x,y) and value of the last spawned value
- `total_score`: the game total score
- `highest_tile`: the highest tile on the board
- `move_count`: the number of moves performed

The game **starts** with an empty board, i.e., all zeros, except two randomly places `2`.

The game **ends** if one of the following conditions is met:
- _game won_: the highest tile is 2048
- _game lost_: the board is full and no more moves are possible
- _illegal_: the last move performed was illegal. This can be disabled by setting `terminate_with_illegal_move=False` 
when creating the environment.