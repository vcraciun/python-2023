import os

def name():
    return "Marius"

def solutie(fname):
    f = open(fname, 'r')
    data = f.read()
    return data.count(' ')
