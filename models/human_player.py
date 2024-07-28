from dataclasses import dataclass

from models.board import Board
from models.cell import Cell
from models.player import Player
from models.user import User


# Flyweight pattern: Extrinsic data, contains intrinsic data User class
@dataclass
class HumanPlayer(Player):
    user: User

    def make_move(self, board: Board) -> Cell:
        row = int(input("enter row: "))
        col = int(input("enter col: "))
        return Cell(row, col, self.symbol)
