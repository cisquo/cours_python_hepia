#!/usr/bin/env python3
# -*- coding: utf-8 -*-

x = int(input ("Entrez x: "))

for i in range(1, x+1, 1):
    print (((2*x-i)-x)*" ", end="")
    print ((2*i-1)*"*")
