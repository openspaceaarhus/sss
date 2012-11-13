#!/usr/bin/env python 
import sys, random, time
import math

W = 120
H = 20
generations = 100

def idx(x,y):
  return W*y + x

last = []
cells = []
for y in range(H):
  for x in range(W):
    cells.append(random.randint(0,1) == 0)
#    cells.append( x > 10 and x < 20 and y > 4 and y < 14);
    last.append(False)

def write_state():
  changes = []
  for y in range(H):
    for x in range(W):
      i = idx(x,y)
      if not cells[i] == last[i]:
        cmd = "{} {}".format(x,y)
        changes.append(cmd)
      last[i] = cells[i] 
  return changes

def wrap(i, bound):
  if i >= bound:
    return i - bound
  if i < 0:
    return bound + i
  
  return i


def neigbors(x,y):
  mx = x - 1 if x > 0 else W-1
  my = y - 1 if y > 0 else H-1
  cnt = 0
  for j in range(3):
    for i in range(3):
      if i == 1 and j == 1:
        continue
      x = (mx + i) % W
      y = (my + j) % H
      if last[idx(x,y)]:
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


fixed_cmd_cnt = 1000

for i in range(generations):

  changes = write_state()
  cnt = fixed_cmd_cnt - len(changes)
    
  random.shuffle(changes)
  for cmd in changes:
    print cmd

  sys.stdout.flush()
  #busy loop
  for b in range(cnt):
    print "#", i, ": busy ", (fixed_cmd_cnt - b)

  update_cells()



  
