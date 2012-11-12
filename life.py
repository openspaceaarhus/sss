#!/usr/bin/env python
import sys, random, time
import math

W = 120
H = 20
generations = 100
def idx(x,y):
  y = y % H
  x = x % W
  return W*y + x

last = []
cells = []
for y in range(H):
  for x in range(W):
    cells.append(random.randint(0,1) == 0)
    last.append(False)

def write_state():
  for y in range(H):
    for x in range(W):
      i = idx(x,y)
      if not cells[i] == last[i]:
        print x,y
      last[i] = cells[i]

def neigbors(x,y):
  #above
  mx = x -1 if x > 0 else W-1
  my = y -1 if y > 0 else H-1
  cnt = 0
  for i in range(3):
    for j in range(3):
      if cells[idx(i+x, j+y)]:
        cnt = cnt + 1
  return cnt

def update_cells():
  for y in range(H):
    for x in range(W):
      n = neigbors(x,y)
      i = idx(x,y)
      if n < 2 or n > 3:
        cells[i] = False
      elif n == 3:
        cells[i] = True

def show_state():

  for y in range(H):
    s = ""
    for x in range(W):
      k = idx(x,y)
      s = s + ("*" if cells[k] else " ")
    print s

for i in range(generations):

  update_cells()
  write_state()
      
  time.sleep(.7)
#  print i, ": done"
  
