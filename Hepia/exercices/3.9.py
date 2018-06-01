#!/usr/bin/env python
# -*- coding: utf-8 -*-

def snake1():
    serpent = '*'
    while serpent != '':
        print(serpent)
        resp = input('+ ou -:')
        if resp == '+':
            serpent += '*'
        elif resp == '-':
            serpent = serpent[:-1]


def snake2():
    tete = '8>'
    taille = 0
    while taille >= 0:
        print('*'*taille + tete)
        resp = input('+ ou -:')
        taille += resp == '+'
        taille -= resp == '-'
