#!/usr/bin/env python

import  pygame
pygame.init() #do it early and only call once?

import sys, random, time
import math

W = 120
H = 20
cell_size = 12


#COLORS
black = [0,0,0]
red = [255,0,0]
green = [0,255,0]
blue = [0,0,255]
white = [255,255,255]
yellow = [255,165, 0]
purple = [102, 0, 172]
grey = [120,120,120]

pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
#modified from http://www.freesound.org/people/Koops/sounds/20258/
flip_snd = pygame.mixer.Sound("flip.ogg")
pygame.mixer.set_num_channels(W*H)
print  "ther are ", pygame.mixer.get_num_channels()

screen = pygame.display.set_mode((W*cell_size,H*cell_size), pygame.NOFRAME)
clock = pygame.time.Clock()
screenCenter = screen.get_rect().center

def idx(x,y):
  return W*y + x

def draw_cell(screen, x,y):
  
  r = pygame.Rect((x * cell_size, y*cell_size), (cell_size, cell_size))
  pygame.draw.rect(screen, black, r)
  width = 0 if cells[idx(x,y)] else 1
  pygame.draw.circle(screen, white, r.center, (cell_size / 2) - 1, width)
  # chn  =  pygame.mixer.find_channel()
  # if chn:
  #   chn.play(flip_snd)


#init
pygame.draw.rect(screen, black, pygame.Rect( (0,0), (W, H)))
cells = []
for y in range(H):
  for x in range(W):
    cells.append(False)
    draw_cell(screen, x, y)



for line in sys.stdin:
  clock.tick(10000)	
  
  coords = line.split()
  x = int(coords[0])
  y = int(coords[1])
  cells[idx(x,y)] = not cells[idx(x,y)] 
  draw_cell(screen, x,y)

  pygame.display.update()
  pygame.display.flip()
  
 
pygame.quit()
