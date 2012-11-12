#!/usr/bin/env python
import sys, random, time
import math

W = 120
H = 20


for i in range(1000):
  x = random.randint(0, W-1);
  y = random.randint(0, H-1);
  cmd = "{} {}".format(x,y)
  print cmd

