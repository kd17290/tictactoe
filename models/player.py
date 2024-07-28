from abc import ABC, abstractmethod
from dataclasses import dataclass

from models.board import Board
from models.cell import Cell
from models.enums import Symbol


@dataclass
class Player(ABC):
    symbol: Symbol

    @abstractmethod
    def make_move(self, board: Board) -> Cell:
        ...
