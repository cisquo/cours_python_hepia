#!/usr/bin/env python3
# -*- coding: utf-8 -*-

n = int(input ("Entrez x: "))

def fibonacci(n):
  a, b = 0, 1
  for i in range(1, n+1):
    a,b = b, a + b
  return a

a = fibonacci(n)
print(a)
