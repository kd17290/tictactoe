from dataclasses import dataclass

from models.board import Board
from models.enums import Symbol
from strategies.winning_strategy import WinningStrategy


@dataclass
class RowWinningStrategy(WinningStrategy):
    def has_won(self, board: Board, symbol: Symbol) -> bool:
        for row in range(board.size):
            row_symbols = [board.cells[row][col].symbol for col in range(board.size)]
            if row_symbols and len(set(row_symbols)) == 1 and row_symbols[0] == symbol:
                return True
        return False
