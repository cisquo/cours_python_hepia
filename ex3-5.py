#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
#n = int(input ("Entrez x: "))
n = random.randint(0,1000)
def mysterieux ( n ):
  cpt = 0
  x = ' '
  while x != n :
    x = int(input ("Devinez le nombre mysterieux: "))
    cpt += 1
    if x > n :
      print('trop grand !')
    else:
      print('trop petit !')
  return cpt

res = mysterieux(n)
print('Vous avez trouvé en',res,'fois')
