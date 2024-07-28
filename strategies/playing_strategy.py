from abc import ABC, abstractmethod
from dataclasses import dataclass

from models.board import Board
from models.cell import Cell
from models.enums import Symbol


@dataclass
class BotPlayingStrategy(ABC):
    @abstractmethod
    def play_next_move(self, board: Board, symbol: Symbol) -> Cell:
        ...
