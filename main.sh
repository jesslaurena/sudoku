#python3 sudoku.py
import pygame, sys
from sudoku_generator import *

pygame.init()

width, height = 729, 729
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
   global current_board
   current_board = easy_board_fill(board)




def medium_board_fill_action():
   global current_board
   current_board = medium_board_fill(board)




def hard_board_fill_action():
   global current_board
   current_board = hard_board_fill(board)




buttons = [
   Button("Easy", 268, 330, 200, 60, "cyan2", "green", easy_board_fill_action),
   Button("Medium", 268, 430, 200, 60, "cyan3", "yellow", medium_board_fill_action),
   Button("Hard", 268, 530, 200, 60, "cyan4", "red", hard_board_fill_action),
]




def game_loop():
   running = True
   while running:
       screen.fill("lightskyblue1")
       draw_grid()


       if current_board:
           draw_numbers(current_board)


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()


       pygame.display.update()


def main_menu():
   running = True
   while running:
       screen.fill("lightskyblue1")
       title.draw(screen)
       subtitle.draw(screen)


       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()


           for button in buttons:
               if button.is_clicked(event):
                   button.action()
                   running = False
                   break


       for button in buttons:
           button.draw(screen)


       pygame.display.update()


   game_loop()


main_menu()
