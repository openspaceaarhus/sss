#!/usr/bin/env python

import  pygame
pygame.init() #do it early and only call once?

import sys, random, time
import math
import threading


W = 120
H = 20
cell_size = 12


#COLORS
black = [0,0,0]
white = [255,255,255]

screen = pygame.display.set_mode((W*cell_size,H*cell_size), pygame.NOFRAME)
clock = pygame.time.Clock()
screenCenter = screen.get_rect().center
changes = pygame.Surface((W*cell_size,H*cell_size))

def idx(x,y):
  return W*y + x

def draw_cell(surface, x,y):
  r = pygame.Rect((x * cell_size, y*cell_size), (cell_size, cell_size))
  pygame.draw.rect(surface, black, r)
  width = 0 if cells[idx(x,y)] else 1
  pygame.draw.circle(surface, white, r.center, (cell_size / 2) - 1, width)


#init
pygame.draw.rect(screen, black, pygame.Rect( (0,0), (W, H)))
cells = []
for y in range(H):
  for x in range(W):
    cells.append(False)
    draw_cell(screen, x, y)

def read_cmds():
  for line in sys.stdin:
    #  print line
    if line.startswith("#"):
      continue
    coords = line.split()
    x = int(coords[0])
    y = int(coords[1])
    cells[idx(x,y)] = not cells[idx(x,y)]
    draw_cell(screen, x,y)
    time.sleep(.00005);          # the flip time aproximation

t = threading.Thread(target=read_cmds)
t.start()


done = False
while not done:
  clock.tick_busy_loop(1500);
  pygame.event.pump()
  for event in pygame.event.get():
    if  event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
      done = True


  pygame.display.update()
  pygame.display.flip()

  
pygame.quit()
