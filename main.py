#python3 sudoku.py
import pygame, sys
from sudoku_generator import *
from boardy import *
import copy

pygame.init()

width, height = 729, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sudoku Grid")
clock = pygame.time.Clock()


pygame.font.init()
font = pygame.font.Font(None, 50)
title_font = pygame.font.Font(None, 100)
subtitle_font = pygame.font.Font(None, 70)


class Title:
   def __init__(self, text, x, y, width, height, base_color,):
       self.text = text
       self.rect = pygame.Rect(x, y, width, height)
       self.base_color = base_color
   def draw(self, surface):
       text_surf = title_font.render(self.text, True, self.base_color)
       text_rect = text_surf.get_rect(center=(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2))
       surface.blit(text_surf, text_rect)


class Subtitle:
   def __init__(self, text, x, y, width, height, base_color):
       self.text = text
       self.rect = pygame.Rect(x, y, width, height)
       self.base_color = base_color
   def draw(self, surface):
       text_surf = subtitle_font.render(self.text, True, self.base_color)
       text_rect = text_surf.get_rect(center=(self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2))
       surface.blit(text_surf, text_rect)




class Button:
   def __init__(self, text, x, y, width, height, base_color, hover_color, action=None):
       self.text = text
       self.rect = pygame.Rect(x, y, width, height)
       self.base_color = base_color
       self.hover_color = hover_color
       self.action = action


   def draw(self, surface):
       mouse_pos = pygame.mouse.get_pos()
       if self.rect.collidepoint(mouse_pos):
           pygame.draw.rect(surface, self.hover_color, self.rect)
       else:
           pygame.draw.rect(surface, self.base_color, self.rect)


       text_surf = font.render(self.text, True, "black")
       text_rect = text_surf.get_rect(center=self.rect.center)
       surface.blit(text_surf, text_rect)


   def is_clicked(self, event):
       if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
           if self.rect.collidepoint(event.pos):
               return True
       return False


title = Title("Welcome to Sudoku!", 165, 100, 400, 50, "black")
subtitle = Subtitle("Choose your mode!", 165, 250, 400, 50, "black")


def draw_grid():
   screen.fill("lightskyblue1")
   for i in range(10):
       pos = i * 81
       if i % 3 == 0:
           pygame.draw.line(screen, "lightslateblue", (0, pos), (width, pos), 6)
           pygame.draw.line(screen, "lightslateblue", (pos, 0), (pos, height), 6)
       else:
           pygame.draw.line(screen, "lightslateblue", (0, pos), (width, pos), 1)
           pygame.draw.line(screen, "lightslateblue", (pos, 0), (pos, height), 1)




def draw_numbers(board):
   font = pygame.font.Font(None, 50)
   for i in range(9):
       for j in range(9):
           if board[i][j] != 0:  # Skip empty cells
               text_surf = font.render(str(board[i][j]), True, "black")
               text_rect = text_surf.get_rect(center=(j * 81 + 40, i * 81 + 40))
               screen.blit(text_surf, text_rect)


current_board = None


def easy_board_fill_action():
    bd = SudokuGenerator(1)
    bd.fill_values()
    key = copy.deepcopy(bd.board)
    bd.remove_cells()
    return key, bd.board

def medium_board_fill_action():
    bd = SudokuGenerator(40)
    bd.fill_values()
    key = copy.deepcopy(bd.board)
    bd.remove_cells()
    return key, bd.board

def hard_board_fill_action():
    bd = SudokuGenerator(50)
    bd.fill_values()
    key = copy.deepcopy(bd.board)
    bd.remove_cells()
    return key, bd.board


buttons = [
   Button("Easy", 268, 330, 200, 60, "cyan2", "green", easy_board_fill_action),
   Button("Medium", 268, 430, 200, 60, "cyan3", "yellow", medium_board_fill_action),
   Button("Hard", 268, 530, 200, 60, "cyan4", "red", hard_board_fill_action),
]


# def game_loop():
#    running = True
#    while running:
#        screen.fill("lightskyblue1")
#        draw_grid()
#
#        if current_board:
#            draw_numbers(current_board)
#
#        for event in pygame.event.get():
#            if event.type == pygame.QUIT:
#                pygame.quit()
#                sys.exit()
#        pygame.display.update()

def check(key, game_bd):
    for r in range(0, 9):
        for c in range(0, 9):
            if key[r][c] != game_bd[r][c]:
                return False
    return True

def win():
    screen.fill("lightskyblue1")
    end_text = f"You won!"
    end_surf = font.render(end_text, True, "black")
    end_rect = end_surf.get_rect(center=(364, 300))
    screen.blit(end_surf, end_rect)
def lose():
    screen.fill("lightskyblue1")
    end_text = f"You lost!"
    end_surf = font.render(end_text, True, "black")
    end_rect = end_surf.get_rect(center=(364, 300))
    screen.blit(end_surf, end_rect)

def main_menu():
   visual_board = None
   while True:
       screen.fill("lightskyblue1")
       title.draw(screen)
       subtitle.draw(screen)

       for button in buttons:
           button.draw(screen)

       if visual_board:
           visual_board.draw()

       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
           if event.type == pygame.MOUSEBUTTONDOWN:
               if visual_board == None:
                   for button in buttons:
                       if button.is_clicked(event):
                           key, game_bd = button.action()
                           print(key)
                           visual_board = Board(729, 729, screen)
                           for row in range(len(game_bd[0])):
                               for col in range(len(game_bd[0])):
                                   cell = Cell(game_bd[row][col], row, col, screen)
                                   visual_board.add_cell(cell)
               if visual_board:
                   x, y = event.pos
                   row = x // 81
                   col = y // 81
                   for cell in visual_board.cell_list:
                       if cell.select == True:
                           cell.select = False
                   for cell in visual_board.cell_list:
                       if row == cell.row and col == cell.col:
                           cell.select = True
                           sel_cell = cell
           if event.type == pygame.KEYDOWN:
               if sel_cell.value == 0:
                   if event.key == pygame.K_1:
                       sel_cell.set_sketched_value(1)
                   elif event.key == pygame.K_2:
                       sel_cell.set_sketched_value(2)
                   elif event.key == pygame.K_3:
                       sel_cell.set_sketched_value(3)
                   elif event.key == pygame.K_4:
                       sel_cell.set_sketched_value(4)
                   elif event.key == pygame.K_5:
                       sel_cell.set_sketched_value(5)
                   elif event.key == pygame.K_6:
                       sel_cell.set_sketched_value(6)
                   elif event.key == pygame.K_7:
                       sel_cell.set_sketched_value(7)
                   elif event.key == pygame.K_8:
                       sel_cell.set_sketched_value(8)
                   elif event.key == pygame.K_9:
                       sel_cell.set_sketched_value(9)
                   if sel_cell.sketch != 0:
                       if event.key == pygame.K_RETURN:
                           sel_cell.value = sel_cell.sketch
                           sel_cell.sketch = 0
                           game_bd[row][col] = sel_cell.value
       if visual_board:
           is_full = True
           for r in range(len(game_bd[0])):
               for c in range(len(game_bd[0])):
                   if game_bd[r][c] == 0:
                       is_full = False
           if is_full:
               result = check(key, game_bd)
               if result:
                   win()
               else:
                   lose()

       pygame.display.update()


main_menu()