from typing import Optional, List, Dict
import random

from discrete.env_2048.grid2048 import Grid


class DiscreteController:

    def control(self, observation: Grid) -> int:
        raise NotImplementedError


class RandomDiscreteController(DiscreteController):

    def __init__(self, seed: Optional[int] = None):
        self.seed: Optional[int] = seed
        self.random_generator = random.Random(seed) if seed is not None else random.Random()

    def control(self, observation: Grid) -> int:
        action_to_direction: Dict[int, str] = {
            0: 'W',  # UP
            1: 'S',  # DOWN
            2: 'A',  # LEFT
            3: 'D',  # RIGHT
        }

        possible_moves: List[int] = []
        for move in sorted(list(action_to_direction.keys())):
            if observation.is_valid_move(action_to_direction[move]):
                possible_moves.append(move)

        if len(possible_moves) == 0:
            return 0

        return self.random_generator.choice(possible_moves)
