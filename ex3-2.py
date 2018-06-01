#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input ("Entrez x: "))

def py ( n ):
  res = 0
  for i in range(1, n+1):
    res += 1 / i**4
  return (90*res)**(1/4)

res = py(n)
print(res)
