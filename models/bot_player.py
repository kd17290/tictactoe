from dataclasses import dataclass, field

from models.board import Board
from models.cell import Cell
from models.enums import DifficultyLevel
from models.player import Player
from strategies.playing_strategy import BotPlayingStrategy
from strategies.random_playing_strategy import RandomBotPlayingStrategy


@dataclass
class BotPlayer(Player):
    difficulty_level: DifficultyLevel
    playing_strategy: BotPlayingStrategy = field(
        default_factory=lambda: RandomBotPlayingStrategy()
    )

    def make_move(self, board: Board) -> Cell:
        return self.playing_strategy.play_next_move(board, self.symbol)
