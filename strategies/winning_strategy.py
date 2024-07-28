from abc import ABC, abstractmethod
from dataclasses import dataclass

from models.board import Board
from models.enums import Symbol


@dataclass
class WinningStrategy(ABC):
    @abstractmethod
    def has_won(self, board: Board, symbol: Symbol) -> bool:
        ...
