import random
from dataclasses import dataclass, field

from models.board import Board
from models.cell import Cell
from models.enums import GameStatus
from models.player import Player
from strategies.col_winning_strategy import ColumnWinningStrategy
from strategies.diagonal_winning_strategy import DiagonalWinningStrategy
from strategies.row_winning_strategy import RowWinningStrategy
from strategies.winning_strategy import WinningStrategy


@dataclass
class Game:
    board: Board
    players: list[Player] = field(default_factory=list)
    next_player_index: int | None = None
    winner: Player | None = None
    status: GameStatus = field(init=False)
    winning_strategy: list[WinningStrategy] = field(
        default_factory=lambda: [
            RowWinningStrategy(),
            ColumnWinningStrategy(),
            DiagonalWinningStrategy(),
        ]
    )

    def start(self):
        self.next_player_index = random.randint(0, len(self.players) - 1)
        self.status = GameStatus.IN_PROGRESS

    def get_current_player(self) -> Player:
        return self.players[self.next_player_index]

    def play(self):
        player: Player = self.get_current_player()
        selected_cell: Cell = player.make_move(self.board)
        self.validate_move(selected_cell)
        self.board.update(selected_cell, player.symbol)
        if self.has_won():
            self.winner = player
            self.status = GameStatus.FINISHED
        elif self.has_draw():
            self.status = GameStatus.DRAW
        else:
            self.next_player_index = (self.next_player_index + 1) % len(self.players)

    def validate_move(self, cell: Cell):
        if cell.x < 0 or cell.x > self.board.size:
            return False
        if cell.y < 0 or cell.y > self.board.size:
            return False
        return True

    def has_won(self):
        for strategy in self.winning_strategy:
            if strategy.has_won(self.board, self.get_current_player().symbol):
                return True
        return False

    def has_draw(self):
        if not self.board.find_all_available_cells():
            return True
        return False
