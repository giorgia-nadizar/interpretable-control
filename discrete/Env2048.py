import gymnasium as gym
from gymnasium import spaces
from typing import Optional
from discrete.src.Grid import Grid
import random
import time
from typing import List, Tuple, Dict, Any


class Env2048(gym.Env):
    def __init__(self,
                 render_mode: Optional[str] = None,
                 verbose: bool = True,
                 column_width: int = 18,
                 delay_in_milliseconds: float = 0.0
                 ) -> None:
        super().__init__()
        self.render_mode: Optional[str] = render_mode
        self.action_space: spaces.Discrete = spaces.Discrete(4)

        self._action_to_direction: Dict[int, str] = {
            0: 'W', # UP
            1: 'S', # DOWN
            2: 'A', # LEFT
            3: 'D', # RIGHT
        }

        self.verbose: bool = verbose
        self.column_width: int = column_width
        self.delay_in_milliseconds: float = delay_in_milliseconds

        self.spawn: Tuple[int, ...] = tuple()
        self.grid: Grid = Grid.create_empty_grid() # 4X4 MATRIX
        self.total_score: int = 0
        self.highest_tile: Tuple[int, int, int] = tuple() # CELL VALUE, ROW_INDEX, COLUMN_INDEX (INDICES GO FROM 0 TO 3, INCLUSIVE)
        self.move_count: int = 0

    def reset(self, seed: Optional[int] = None, options: Optional[Dict[str, Any]] = None) -> Tuple[Grid, Dict]:
        super().reset(seed=seed, options=options)

        self.seed: Optional[int] = seed
        self.random_generator: random.Random = random.Random(seed) if seed is not None else random.Random()
        grid: Grid = Grid.create_empty_grid()

        spawn: List[Tuple[int, int]] = []
        for i, j in self.random_generator.sample([(i, j) for i in range(4) for j in range(4)], k=2):
            grid.set(i, j, 2)
            spawn.append((i,j))
        
        self.highest_tile = (2, spawn[0][0], spawn[0][1])
        self.spawn = (spawn[0][0], spawn[0][1], spawn[1][0], spawn[1][1])
        self.grid = grid
        self.total_score = 0
        self.move_count = 0

        if self.verbose:        
            print()
            print('='*50+'BEGIN'+'='*50)
            print()       
            print(f'HIGHEST TILE: {self.highest_tile}')
            print(f'TOTAL SCORE: {self.total_score}')
            print(f'MOVE N. {self.move_count}')
            print(f'EXECUTED MOVE: {'INITIALIZE'}')
            print()
            self.grid.print(column_width=self.column_width)
            print()

        return self.grid, {}

    def step(self, action: int) -> Tuple[Grid, int, bool, bool, Dict]:
        direction: str = self._action_to_direction[action]
        score, grid = self.grid.move(direction)
        self.grid = grid
        terminated = False
        truncated = False

        self.total_score += score

        if not self.grid.is_full():
            spawn_coord: Tuple[int, int] = self.random_generator.choice(self.grid.empty_cells())
            spawn_val: int = self.random_generator.choice([2, 2, 2, 2, 4])
            self.grid.set(spawn_coord[0], spawn_coord[1], spawn_val)
            self.current_spawn = (spawn_val, spawn_coord[0], spawn_coord[1])
        else:
            self.current_spawn = (-1, -1, -1)

        self.move_count += 1
        self.highest_tile = self.grid.highest_tile()
        time.sleep(self.delay_in_milliseconds / 1000.0)

        if self.verbose:
            print(f'HIGHEST TILE: {self.highest_tile}')
            print(f'TOTAL SCORE: {self.total_score}')
            print(f'MOVE N. {self.move_count}')
            print(f'EXECUTED MOVE: {'INITIALIZE'}')
            print()
            self.grid.print(column_width=self.column_width)
            print()

        if self.grid.is_game_over():
            terminated = True
            truncated = True

        if terminated or truncated:
            if self.verbose:
                print()
                print('='*50+'GAME OVER'+'='*50)
                print()
        
        return self.grid, score, terminated, truncated, {}
