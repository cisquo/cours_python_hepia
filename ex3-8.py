#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#s = input ("Entrez une valeur: ")

def est_numerique(s):
    if s[0] == '-':
      return s[1:].isnumeric()
    else:
      return s.isnumeric()pw

def double (l):
    l1 = []
    for x in l:
        if x.isnumeric() :
            l1.append(int(x)*2)
    return l1

def verifier (l):
    return len(l) == len(double(l))


def serpent(i):
  s = 1
  print('0', end="")
  while s > 0 :
    i = input("Direction: ")
    if i == '+':
      s += s
    else:
      s = s-1
    print('*'*s)

#print(est_numerique(s))
