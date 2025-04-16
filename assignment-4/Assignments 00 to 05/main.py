import pygame
import time


pygame.init()

canva_width = 400
canva_height = 400
cell_size = 40
eraser_size = 20

blue = (0,0,225)
white = (255, 255,255)
pink = (255,182,193)

screen = pygame.display.set_mode((canva_width, canva_height))
pygame.display.set_caption("Enter effect in pygame")

grid = []
for row in range(0,canva_height, cell_size):
    for col in range(0,canva_width, cell_size):
     rect = pygame.Rect(col,row,cell_size,cell_size)
     grid.append(rect)

eraser = pygame.Rect(200,200,eraser_size, eraser_size)

running = True
while running:
   screen.fill(blue)

   for rect in grid:
      pygame.draw.rect(screen,pink,rect)

      mouse_x, mouse_y = pygame.mouse.get_pos()
      eraser.topleft = (mouse_x, mouse_y)

   new_grid = []
   for rect in grid:
     if not eraser.colliderect(rect):
      new_grid.append(rect)
   grid = new_grid

   pygame.draw.rect(screen,white,eraser)

   for event in pygame.event.get():
       if event.type == pygame.QUIT:
          running = False

   pygame.display.flip()
   time.sleep(0.05)

pygame.quit()