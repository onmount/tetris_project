from colors import Colors

class Block:
    def __init__(self):
        self.cells = {}
        self.cell_size = 30
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()
        self.row_offset = 0
        self.col_offset = 0

    def move(self, rows, cols):
        self.row_offset += rows
        self.col_offset += cols

    def rotate(self, turns):
        self.rotation_state = (self.rotation_state + turns) % 4

    def get_cells(self):
        old_cells = self.cells[self.rotation_state]
        new_cells = []
        for cell in old_cells:
            new_cells.append(cell.move(self.row_offset, self.col_offset))
        return new_cells


    def draw(self, screen):
        cells = self.get_cells()
        for cell in cells:
            cell.draw(screen)

    def draw_shifted(self, screen, delta_rows, delta_cols):
        self.move(delta_rows, delta_cols)
        cells = self.get_cells()
        for cell in cells:
            cell.draw(screen)
        self.move(-1 * delta_rows, -1 * delta_cols)