from dataclasses import dataclass, field

from models.cell import Cell
from models.enums import Symbol


@dataclass
class Board:
    cells: list[list[Cell]] = field(init=False)
    size: int

    def __post_init__(self):
        cells = []
        for row in range(self.size):
            row_cells: list[Cell] = []
            for col in range(self.size):
                row_cells.append(Cell(row, col))
            cells.append(row_cells)
        self.cells = cells

    def find_all_available_cells(self) -> list[Cell]:
        available_cells: list[Cell] = []
        for row_cells in self.cells:
            for col_cell in row_cells:
                if not col_cell.symbol:
                    available_cells.append(col_cell)
        return available_cells

    def update(self, cell: Cell, symbol: Symbol) -> None:
        cell = self.cells[cell.x][cell.y]
        cell.symbol = symbol

    def print(self):
        for row in self.cells:
            for cell in row:
                print(cell.symbol.value if cell.symbol else "_", end=" ")
            print()
