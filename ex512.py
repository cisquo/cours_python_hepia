#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#s = input ("Entrez une valeur: ")

def add(dic,k,v):
    dic.append((k,v))

def index(dic,val):
    for k,v in dic:
        if v == val:
            return k


def lenght(dic):
    return len(dic)


def is_in(dic, cle):
    for k,v in dic:
        if k == cle:
            return True
    return False


def val(dic):
    print (dic)


def key(dic):
    for k,v in dic:
        print (k)

def reverse(dic):
    for k,v in dic:
        print (v,k)


try:
    res =
