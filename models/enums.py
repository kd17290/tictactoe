from enum import Enum


class Symbol(Enum):
    O = 0
    X = 1


class DifficultyLevel(Enum):
    easy = 0
    medium = 1
    hard = 2


class GameStatus(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    FINISHED = 2
    DRAW = 3
