# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:43:02 2017

@author: harne
"""

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """
    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s
    
class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        count = self.vals[e]
        return count
    def __add__(self, other):
        b = self.vals
        a = other.vals
        tup = ''
        for key in self.vals:
            if key in other.vals:
                b[key] += a[key]
        for item in b:
            tup += str(item) + ":" + str(b[item]) + "\n"
        return tup
            

a = Bag()
a.insert(4)
a.insert(3)
b = Bag()
b.insert(4)
print(a+b)