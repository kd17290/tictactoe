from dataclasses import dataclass

from models.board import Board
from models.enums import Symbol
from strategies.winning_strategy import WinningStrategy


@dataclass
class DiagonalWinningStrategy(WinningStrategy):
    def has_won(self, board: Board, symbol: Symbol) -> bool:
        main_diagonal_symbols = [board.cells[i][i].symbol for i in range(board.size)]
        if (
            main_diagonal_symbols
            and len(set(main_diagonal_symbols)) == 1
            and main_diagonal_symbols[0] == symbol
        ):
            return True
        other_diagonal_symbols = [
            board.cells[i][board.size - 1 - i].symbol for i in range(board.size)
        ]
        if (
            other_diagonal_symbols
            and len(set(other_diagonal_symbols)) == 1
            and other_diagonal_symbols[0] == symbol
        ):
            return True
        return False
