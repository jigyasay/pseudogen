#!/usr/bin/env python

'''
AST node class definitions and properties
'''



class Assignment:
    __slots__ = ('op','dType','lvalue','rvalue')
    
    def __init__(self, op, dType, lvalue, rvalue):
        self.op = op
        self.lvalue = lvalue
        self.rvalue = rvalue
        self.dType =  dType
        
    def children(self):
        nodelist = (self.lvalue, self.rvalue)
        return nodelist
    
class BinaryOp:
    __slots__ = ('op','left','right','dType','length')
    
    def __init__(self, op, left, right, dType, length):
        self.op = op
        self.left = left
        self.right = right
        self.dType = dType
        self.length = length
    
    def children(self):
        nodelist = (self.left, self.right)
        return nodelist
    
class UnaryOp:
    __slots__ = ('dType','op','right','length')
    
    def __init__(self, dType, op, right, length):
        self.dType = dType
        self.op = op
        self.right = right
        self.length = length
    
    def children(self):
        return (self.right)
    
class Constant:
    __slots__ = ('dType','value','length')
    
    def __init__(self, dType, value, length):
        self.dType = dType
        self.value = value
        self.length = length
        
    def children(self):
        return None
    
class Variable:
    __slots__ = ('dType','name','length')
    
    def __init__(self, dType, name, length):
        self.name = name
        self.dType = dType
        self.length = length
        
    def children(self):
        return None
    
class Output:
    __slots__ = ('data')
    
    def __init__(self, data):
        self.data = data
        
    def children(self):
        return (self.data)
    
class Input:
    __slots__ = ('variable', 'dType')
    
    def __init__(self, variable, dType):
        self.variable = variable
        self.dType = dType
        
    def children(self):
        return None
    
class If:
    __slots__ = ('condition', 'if_true', 'if_false')
    
    def __init__(self, condition, if_true, if_false):
        self.condition = condition
        self.if_true = if_true
        self.if_false = if_false
        
    def children(self):
        return (self.condition, self.if_true, self.if_false)
    
class While:
    __slots__ = ('condition', 'body')
    
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body
        
    def children(self):
        return (self.condition, self.body)

class Array_Declaration:
    __slots__ = ('dType','name','elements')
    
    def __init__(self, dType, name, elements):
        self.dType = dType
        self.name = name
        self.elements = elements
        
    def children(self):
        return (self.elements)
    
class Array_Element:
    __slots__ = ('dType', 'name', 'index', 'length')
    
    def __init__(self, dType, name, index, length):
        self.dType = dType
        self.name = name
        self.length = length
        self.index = index
        
    def children(self):
        return (self.index)
    
class For:
    __slots__ = ('assignment','final','body')
    
    def __init__(self, assignment, final, body):
        self.assignment = assignment
        self.final = final
        self.body = body
        
    def children(self):
        return (self.assignment, self.final, self.body)

class Function_Decl:
    __slots__ = ('name','args','body','dType')
    
    def __init__(self, name, args, body, dType):
        self.name = name
        self.args = args
        self.body = body
        self.dType = dType
    
    def children(self):
        return None
    
class Function_Call:
    __slots__ = ('name', 'args', 'dType', 'length')

    def __init__(self, name, args, dType, length):
        self.name = name
        self.args = args
        self.dType = dType
        self.length = length
    
    def children(self):
        return self.args
    
class Return:
    __slots__ = ('data')
    
    def __init__(self, data):
        self.data = data
    
    def children(self):
        return self.data
