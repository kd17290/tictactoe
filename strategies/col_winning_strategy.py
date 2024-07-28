from dataclasses import dataclass

from models.board import Board
from models.enums import Symbol
from strategies.winning_strategy import WinningStrategy


@dataclass
class ColumnWinningStrategy(WinningStrategy):
    def has_won(self, board: Board, symbol: Symbol) -> bool:
        for col in range(board.size):
            col_symbols = [board.cells[row][col].symbol for row in range(board.size)]
            if col_symbols and len(set(col_symbols)) == 1 and col_symbols[0] == symbol:
                return True
        return False
