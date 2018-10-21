# Lets understand what do you mean by list comprehension
class IntSet(object):
"""An intSet is a set of integers"""
#Information about the implementation (not the abstraction)
#Value of the set is represented by a list of ints, self.vals.
#Each int in the set occurs in self.vals exactly once.
def __init__(self):
"""Create an empty set of integers"""
self.vals = []
def insert(self, e):
"""Assumes e is an integer and inserts e into self"""
if e not in self.vals:
self.vals.append(e)
def member(self, e):
"""Assumes e is an integer
Returns True if e is in self, and False otherwise"""
return e in self.vals
def remove(self, e):
"""Assumes e is an integer and removes e from self
Raises ValueError if e is not in self"""
try:
self.vals.remove(e)
except:
raise ValueError(str(e) + ' not found')
def getMembers(self):
"""Returns a list containing the elements of self.
Nothing can be assumed about the order of the elements"""
return self.vals[:]
def __str__(self):
"""Returns a string representation of self"""
self.vals.sort()
result = ''
for e in self.vals:
result = result + str(e) + ','
return '{' + result[:-1] + '}' #-1 omits trailing comma

# instantiation is used to create instances of the class
s = IntSet() # creates a new object of type intSet. 's' object is called instance of IntSetself.
#Attribute references use dot notation to access attributes associated with the
#class. For example, s.member refers to the method member associated with the instance
#s of type IntSet.
