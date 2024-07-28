from dataclasses import dataclass


# Flyweight pattern to separate out the intrinsic data(reusable) from HumanPlayer for better memory management
@dataclass
class User:
    email: str
    username: str
    password: str
    profile_picture: str | None = None
