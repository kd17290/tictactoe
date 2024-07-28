from models.board import Board
from models.bot_player import BotPlayer
from models.enums import Symbol, DifficultyLevel, GameStatus
from models.game import Game
from models.human_player import HumanPlayer
from models.user import User


def create_game():
    board = Board(3)
    user = User(
        email="<EMAIL>",
        username="Username",
        password="<PASSWORD>",
    )
    players = [
        HumanPlayer(symbol=Symbol.O, user=user),
        BotPlayer(symbol=Symbol.X, difficulty_level=DifficultyLevel.medium),
    ]
    game = Game(board=board, players=players)
    game.start()

    while game.status == GameStatus.IN_PROGRESS:
        print(f"Next player turn: {game.get_current_player()}")
        game.play()
        game.board.print()
        if game.status == GameStatus.FINISHED:
            print(f"{game.winner.symbol} has won!")
            break
        if game.status == GameStatus.DRAW:
            print("Game over, drawn")
            break


if __name__ == "__main__":
    create_game()
