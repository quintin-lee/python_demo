#!/usr/bin/env python
# coding=utf-8

class Animal:
    '''
    This is a class of Animal 
    '''
    name = ""

    def __init__(self, name):
        self.name = name

    def display(self):
        print "name:", self.name

a = Animal("mouse")
a.display()
