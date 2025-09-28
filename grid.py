from colors import Colors
from cell import Cell

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        self.grid = [[Cell(row, col, [], 0) for col in range(self.num_cols)] for row in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()
        self.score = 0

    def is_inside(self, row, col):
        return 0 <= row < self.num_rows and 0 <= col < self.num_cols

    def is_empty(self, row, col):
        return self.grid[row][col].is_empty()

    def connects_to_edge(self, row, col):
        if (col == 0) and ((0, -1) in self.grid[row][col].get_connections()):
            return True
        if (col == self.num_cols - 1) and ((0, 1) in self.grid[row][col].get_connections()):
            return True
        if (row == 0) and ((-1, 0) in self.grid[row][col].get_connections()):
            return True
        if (row == self.num_rows - 1) and ((1, 0) in self.grid[row][col].get_connections()):
            return True
        return False

    def path_search(self, row, col, used, is_first):
        if not self.is_inside(row, col):
            return False
        if self.is_empty(row, col):
            return False
        used[row][col] = True
        if (not is_first) and self.connects_to_edge(row, col):
            self.grid[row][col].clear_cell()
            self.score += 10
            return True
        cell_connections = self.grid[row][col].get_connections()
        for connection in cell_connections:
            row_delta, col_delta = connection
            if not self.is_inside(row + row_delta, col + col_delta):
                continue
            if self.is_empty(row + row_delta, col + col_delta):
                continue
            if used[row + row_delta][col + col_delta]:
                continue
            if not (-1 * row_delta, -1 * col_delta) in self.grid[row + row_delta][col + col_delta].get_connections():
                continue
            if self.path_search(row + row_delta, col + col_delta, used, False) == True:
                self.grid[row][col].clear_cell()
                self.score += 10
                return True
        return False

    def normalise_grid(self):
        for col in range(self.num_cols):
            found_empty = 0
            for row in range(self.num_rows - 1, 0, -1):
                if self.grid[row][col].is_empty():
                    found_empty += 1
                else:
                    if found_empty > 0:
                        self.grid[row + found_empty][col] = self.grid[row][col].move(found_empty, 0)
                        self.grid[row][col].clear_cell()

    def try_to_find_path(self):
        used = [[False for col in range(self.num_cols)] for row in range(self.num_rows)]
        for row in range(self.num_rows):
            if self.connects_to_edge(row, 0):
                if self.path_search(row, 0, used, True) == True:
                    self.normalise_grid()
                    return True
        for row in range(self.num_rows):
            if self.connects_to_edge(row, self.num_cols - 1):
                if self.path_search(row, self.num_cols - 1, used, True) == True:
                    self.normalise_grid()
                    return True
        for col in range(self.num_cols):
            if self.connects_to_edge(0, col):
                if self.path_search(0, col, used, True) == True:
                    self.normalise_grid()
                    return True
        for col in range(self.num_cols):
            if self.connects_to_edge(self.num_rows - 1, col):
                if self.path_search(self.num_rows - 1, col, used, True) == True:
                    self.normalise_grid()
                    return True

        return False

    def clear_grid(self):
        not_cleared = True
        combo = 1
        ans_score = 0
        while not_cleared:
            not_cleared = self.try_to_find_path()
            ans_score += self.score * combo
            self.score = 0
            combo += 1
        return ans_score

    def draw(self, screen):
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                self.grid[row][col].draw(screen)

    def reset(self):
        self.grid = [[Cell(row, col, [], 0) for col in range(self.num_cols)] for row in range(self.num_rows)]
