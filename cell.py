from colors import Colors
import pygame

class Cell:
    def __init__(self, row, col, connections, new_id):
        self.row = row
        self.col = col
        self.connections = connections
        self.id = new_id
        self.cell_size = 30
        self.colors = Colors.get_cell_colors()

    def clear_cell(self):
        self.connections = []
        self.id = 0

    def is_empty(self):
        return len(self.connections) == 0

    def get_connections(self):
        ans_connections = []
        if 0 in self.connections:
            ans_connections.append((-1, 0))
        if 1 in self.connections:
            ans_connections.append((0, 1))
        if 2 in self.connections:
            ans_connections.append((1, 0))
        if 3 in self.connections:
            ans_connections.append((0, -1))
        return ans_connections

    def move(self, row, col):
        return Cell(self.row + row, self.col + col, self.connections, self.id)

    def draw(self, screen):
        rect = pygame.Rect(self.col * self.cell_size, self.row * self.cell_size, self.cell_size - 1, self.cell_size - 1)
        pygame.draw.rect(screen, self.colors[self.id], rect)
        if 0 in self.connections:
            direction_rect = pygame.Rect(self.col * self.cell_size + (self.cell_size // 2) - 1, self.row * self.cell_size, 2, 15)
            pygame.draw.rect(screen, Colors.white, direction_rect)
        if 1 in self.connections:
            direction_rect = pygame.Rect(self.col * self.cell_size + (self.cell_size // 2) - 1, self.row * self.cell_size  + (self.cell_size // 2) - 1, 15, 2)
            pygame.draw.rect(screen, Colors.white, direction_rect)
        if 2 in self.connections:
            direction_rect = pygame.Rect(self.col * self.cell_size + (self.cell_size // 2) - 1, self.row * self.cell_size + (self.cell_size // 2) - 1, 2, 15)
            pygame.draw.rect(screen, Colors.white, direction_rect)
        if 3 in self.connections:
            direction_rect = pygame.Rect(self.col * self.cell_size, self.row * self.cell_size + (self.cell_size // 2) - 1, 15, 2)
            pygame.draw.rect(screen, Colors.white, direction_rect)