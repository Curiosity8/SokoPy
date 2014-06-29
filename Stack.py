# My implementation of Stacks, using linked list. 
# Not 100% complete, yet sufficient for our needs.

class NodeStack:
    def __init__(self, item):
        self.item = item
        self.next = None

class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.N = 0

    def __len__(self):
        return self.N

    def isEmpty(self):
        # Is stack empty?
        return self.first == None

    def push(self, x):
        oldfirst = self.first
        self.first = NodeStack(x)
        self.first.next = oldfirst
        self.N += 1
        
    def pop(self):
        if self.isEmpty():
            return "Can't delete anymore!"
        
        item = self.first.item
        self.first = self.first.next
        self.N -= 1
        
        return item
