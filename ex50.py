#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#s = input ("Entrez une valeur: ")

def longueur(l1):
    nb = 0
    for x in l1:
        nb += 1
    return nb

def moyenne(l1):
    total = 0
    for x in l1:
        total = total + x
    return total / longueur(l1) if l1 else 0

def plus_grand_ou_egal (l1, n):
    res = []
    for x in l1:
        if x >= n :
            res.append(x)
    return res

def plus_petit_ou_egal (l1, n):
    res = []
    for x in l1:
        if x <= n :
            res.append(x)
    return res

def minimum (l1):
    res = l1[0]
    for x in l1:
        if x < res :
            res = x
    return res

def positive (l1):
    return plus_grand_ou_egal(l1,0)

def dans(l1, n):
    return True if (set(l1) & set({n})) == {n} else False

def binaire(l1):
    res = 0
    for i, elem in enumerate(reversed(l1)):
#        print(i,':',elem)
#        print(elem*(2**i))
        res += int(elem)*(2**i)
    return(res)

def and_lst(lst):
    for elem in lst:
        if not elem:
            return False
    return True


def zip(l1, l2):
    l3 = []
    if len(l1) == len(l2):
        for i in range(len(l1)):
            l3.append((l1[i], l2[i]))
        return l3
    return l3

# [(A,B]] -> ([A],[B])
def unzip(l1):
    l3 = []
    l2 = []
    for i, j in l1:
        l3.append(i)
        l2.append(j)
    return l2, l3


def f(x):
    return 2*x+2

def transform(lst,f):
    l2 = []
    for elem in lst:
        l2.append( f(elem) )
    return l2

def majeur(age):
    return age >= 18

def mineur(age):
    return age < 18

def filter(lst,f):
    l2 = []
    for elem in lst:
        if f(elem):
            l2.append( (elem) )
    return l2


def remove_duplicates(lst):
    l2 = []
    for elem in lst:
        if f(elem)
            l2.append( (elem) )
    return l2
