import pygame, sys

class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.select = False
        self.sketch = 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketch = value

    def draw(self):
        pygame.font.init()
        font = pygame.font.SysFont("Times New Roman", 65)
        if self.value != 0:
            cell_surf = font.render(str(self.value), True, "black")
            cell_rect = cell_surf.get_rect(topleft=(self.row * 81 + 25, self.col * 81 + 10))
            self.screen.blit(cell_surf, cell_rect)
        if self.select == True:
            pygame.draw.rect(self.screen, "red", pygame.Rect( self.row * 81, self.col * 81, 81, 81), 2)
        if self.sketch != 0:
            cell_surf = font.render(str(self.sketch), True, "lightskyblue4")
            cell_rect = cell_surf.get_rect(topleft=(self.row * 81 + 25, self.col * 81 + 10))
            self.screen.blit(cell_surf, cell_rect)


class Board:

    def __init__(self, width, height, screen):
        self.width = width
        self.height = height
        self.screen = screen
        self.cell_list = []

    def add_cell(self, cell):
        self.cell_list.append(cell)


    def draw(self):
        self.screen.fill("lightskyblue1")
        for i in range(10):
            pos = i * 81
            if i % 3 == 0:
                pygame.draw.line(self.screen, "lightslateblue", (0, pos), (self.width, pos), 6)
                pygame.draw.line(self.screen, "lightslateblue", (pos, 0), (pos, self.height), 6)
            else:
                pygame.draw.line(self.screen, "lightslateblue", (0, pos), (self.width, pos), 1)
                pygame.draw.line(self.screen, "lightslateblue", (pos, 0), (pos, self.height), 1)
        for cell in self.cell_list:
            cell.draw()