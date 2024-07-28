from dataclasses import dataclass

from models.enums import Symbol


@dataclass
class Cell:
    x: int
    y: int
    symbol: Symbol = None
