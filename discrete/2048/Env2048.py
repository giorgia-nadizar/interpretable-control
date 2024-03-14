import gymnasium as gym
from gymnasium import spaces
from typing import Optional
import random
from typing import List, Tuple, Dict, Any


class Env2048(gym.Env):
    def __init__(self,
                 terminate_with_illegal_move: Optional[bool] = True,
                 render_mode: Optional[str] = None,
                 seed: Optional[int] = None,
                 ) -> None:
        super().__init__()
        if render_mode is not None and render_mode not in 'terminal':
            raise AttributeError(f'render_mode is {render_mode}, but it must be either terminal or None (if disabled).')

        self.seed: Optional[int] = seed
        self.render_mode: Optional[str] = render_mode
        self.action_space: spaces.Discrete = spaces.Discrete(4, seed=seed)
        self.terminate_with_illegal_move: bool = terminate_with_illegal_move

        self._action_to_direction: Dict[int, str] = {
            0: 'W',  # UP
            1: 'S',  # DOWN
            2: 'A',  # LEFT
            3: 'D',  # RIGHT
        }

        # parameter needed for rendering purposes
        self.column_width: int = 18

        # AT INITIALIZATION, THIS IS A TUPLE OF 4 INTEGER VALUES INDICATING THE POSITIONS (ROW_INDEX, COLUMN_INDEX) OF THE SPAWNED VALUES (e.g., (0, 1, 3, 1) means that 2s are spawned in positions (0, 1) and (3, 1) in the grid).
        # DURING THE GAME, THIS IS A TUPLE OF 3 INTEGER VALUES, INDICATING THE SPAWNED VALUE (EITHER 2 OR 4) AND THE POSITION (ROW_INDEX, COLUMN_INDEX) IN THE GRID.
        self.spawn: Tuple[int, ...] = tuple()

        self.grid: Grid = Grid.create_empty_grid()  # 4X4 MATRIX
        self.total_score: int = 0
        # value, row index, column index (indexes from 0 to 3, inclusive)
        self.highest_tile: Tuple[int, int, int] = tuple()
        self.move_count: int = 0
        self.direction: str = 'INITIALIZE'

    def _get_obs(self) -> Grid:
        return self.grid

    def _get_info(self) -> Dict[str, Any]:
        return {'direction': self.direction, 'spawn': self.spawn, 'total_score': self.total_score,
                'highest_tile': self.highest_tile, 'move_count': self.move_count}

    def reset(self,
              seed: Optional[int] = None,
              options: Optional[Dict[str, Any]] = None
              ) -> Tuple[Grid, Dict[str, Any]]:
        super().reset(seed=seed, options=options)

        self.seed = seed
        self.random_generator = random.Random(seed) if seed is not None else random.Random()
        self.action_space = spaces.Discrete(4, seed=seed)
        self.grid = Grid.create_empty_grid()

        spawn: List[Tuple[int, int]] = []
        for i, j in self.random_generator.sample([(i, j) for i in range(4) for j in range(4)], k=2):
            self.grid.set(i, j, 2)
            spawn.append((i, j))

        self.highest_tile = (2, spawn[0][0], spawn[0][1])
        self.spawn = (spawn[0][0], spawn[0][1], spawn[1][0], spawn[1][1])
        self.total_score = 0
        self.move_count = 0
        self.direction = 'INITIALIZE'

        return self._get_obs(), self._get_info()

    def step(self, action: int) -> Tuple[Grid, int, bool, bool, Dict[str, Any]]:
        self.direction = self._action_to_direction[action]
        self.move_count += 1
        try:
            score, self.grid = self.grid.move(self.direction)
        # TODO define more specific error
        except ValueError as e:
            return self._get_obs(), 0, self.terminate_with_illegal_move, False, self._get_info()

        terminated = False
        truncated = False
        self.total_score += score

        if not self.grid.is_full():
            spawn_coord: Tuple[int, int] = self.random_generator.choice(self.grid.empty_cells())
            spawn_val: int = self.random_generator.choice([2] * 9 + [4])
            self.grid.set(spawn_coord[0], spawn_coord[1], spawn_val)
            self.spawn = (spawn_val, spawn_coord[0], spawn_coord[1])
        else:
            self.spawn = (-1, -1, -1)

        self.highest_tile = self.grid.highest_tile()

        if self.grid.is_game_over():
            terminated = True

        return self._get_obs(), score, terminated, truncated, self._get_info()

    def render(self) -> None:
        if self.render_mode == 'terminal':
            print(f'HIGHEST TILE: {self.highest_tile}')
            print(f'TOTAL SCORE: {self.total_score}')
            print(f'MOVE N. {self.move_count}')
            print(f'EXECUTED MOVE: {self.direction}')
            print()
            self.grid.print(column_width=self.column_width)
            print()
