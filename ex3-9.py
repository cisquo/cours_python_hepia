#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#s = input ("Entrez une valeur: ")

def serpent(i):
  s = 1
  print('0')
  while s > 0 :
    i = input("Direction: ")
    if i == '+':
      s = s+1
    else:
      s = s-1
      q = ('*'*(s-1))
    print('0' + q)

#print(est_numerique(s))
