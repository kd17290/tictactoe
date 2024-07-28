from dataclasses import dataclass
from random import choice

from models.board import Board
from models.cell import Cell
from models.enums import Symbol
from strategies.playing_strategy import BotPlayingStrategy


@dataclass
class RandomBotPlayingStrategy(BotPlayingStrategy):
    def play_next_move(self, board: Board, symbol: Symbol) -> Cell:
        cells: list[Cell] = board.find_all_available_cells()
        cell = choice(cells)
        cell.symbol = symbol
        return cell
