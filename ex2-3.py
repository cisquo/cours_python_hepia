#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = float(input ("Entrez x: "))
#y = float(input ("Entrez y: "))
#a  = True if x >=0 else False

def positif(x):
    return True if x >0 else False

#print (positif(x))

def maximum(x, y):
    return x if x > y else y

def minimum(x, y):
    if maximum(x, y) == x:
        return y
    else:
        return x

def negatif(x):
    return False if minimum(x, 0) >= 0 else True


def oppose(x):
    return -x

def absolu(x):
    return x if negatif(x) == False else oppose(x)

def algo(x):
    return maximum(-1, minimum(6, 2*x))

print (algo(x))
