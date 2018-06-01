#!/usr/bin/env python
# -*- coding: utf-8 -*-

class KeyException(Exception):
    pass


def is_in(dic, key):
    for k, _ in dic:
        if k == key:
            return True
    return False

def add(dic, k, v):
    if is_in(dic, k):
        drop(dic, k)
        dic.append((k, v))
    else:
        dic.append((k,v))


def index(dic, varg):
    for k,v in dic:
        if varg == v:
            return k
    raise KeyException


def get(dic, karg):
    for k, v in dic:
        if k == karg:
            return v
    raise KeyException()


def get_or_else(dic, karg, default):
    try:
        return get(dic, karg)
    except KeyException:
        return default


def length(dic):
    return len(dic)


def drop(dic, k):
    v = get(dic, k)
    dic.remove((k,v))
    return v


def values(dic):
    res = []
    for k, v in dic:
        res.append(v)
    return res

def keys(dic):
    res = []
    for k, v in dic:
        res.append(k)
    return res

def reverse(dic):
    res = []
    for k, v in dic:
        res.append((v, k))
    return res


if __name__ == '__main__':
    dic = []
    add(dic, 'Prenom', 'Adrien')
    add(dic, 'Nom', 'Lescourt')

    a = (keys(dic))
    print(reverse(dic))

