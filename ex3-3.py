#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
n = int(input ("Entrez x: "))

def py ( n ):
  cpt = 0

  for i in range(1, n+1):
    if i % 10000 == 0:
        print(i)
    x = random.random()
    y = random.random()
    if x**2 + y**2 <=1:
        cpt += 1
  return (4*cpt)/n

res = py(n)
print(res)
