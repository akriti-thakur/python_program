# stack=[]

# stack.append('a')
# stack.append('b')
# stack.append('v')
# print(stack)


# stack.pop()
# stack.pop()
# stack.pop()
# print(stack)

# # ---------------------------------------------------

# from collections import deque

# stack=deque()

# stack.append('a')
# stack.append('b')
# stack.append('c')

# print(stack)

# print(stack.pop())
# print(stack.pop())
# print(stack.pop())


# print("stack after poping the elemnt")
# print(stack)

# # ---------------------------------------------------------------------------------
# from queue import LifoQueue

# stack= LifoQueue(maxsize=4)

# print(stack.qsize)

# stack.put(1)
# stack.put(2)
# stack.put(3)

# print("full :", stack.full())

# print("elements poped out are ")
# print(stack.get())
# print(stack.get())
# print(stack.get())



# print("is stach empty : ",stack.empty())
# -----------------------------------------------------------------------------------

# class stack ():
#     def __init__(self):
#         self.item=[]
        
        
#     def isempty (self):
#         return self.item == []
    
#     def push(self,data):
#         self.item.append(data)
        
        
#     def pop(self):
#         return self.item.pop()
    
    
    
# s= stack()
# while True:
#     print('push <value>')
#     print('pop')
#     print('quit')
#     do = input("what would you like to do").split()
    
#     operation =do[0].strip().lower()
#     if operation == 'push':
#         num=int(input("what you want ot push?"))
#         s.push(num)
#     elif operation=='pop':
#         if s.isempty():
#             print( "stack is empty")
            
            
#         else:
#             print('poped value', s.pop())
            
            
#     elif operation == "quit":
#         break

# -------------------------------------------------------------------------


# Python Program to Implement Stack using Queue
# from queue import Queue

# class stack:
#     def __init__(self):
#         self.q= Queue()
        
#     def push(self,data):
#          self.size= self.q.qsize()
#          self.q.put(data)
#          for i in range(self.size):
#              self.q.put(self.q.get())
             
             
#     def pop(self):
#         if self.q.empty():
#             return None
#         else:
#             return self.q.get()
        
#     def top(self):
#         if self.q.empty():
#             return None
        
#         top_item= self.q.get()
#         self.q.put(top_item)
        
#         for i in range(self.size - 1):
#             self.q.put(self.q.get())
            
#         return top_item
    
#     def is_empty(self):
#         return self.q.empty()
    
    
# s=stack()

# s.push(1)
# s.push(2)
# s.push(3)
# # print(s.top())
# print(s.pop())
# print(s.pop())
# print(s.pop())


# with out using queue

class stack :
    def __init__(self):
        self.d=[]
        
    def push(self,data):
        self.d.sppend(data)
        for _ in range (len(self.d)):
            self.d.append(self.d.pop())        






------------------------------------------------------------------------------------------------
#  stack using list
# class stack:
#     def __init__(self):
#         self.stack=[]
        
#     def push(self,data):
#         self.stack.append(data)
        
#     def pop(self):
#         if len(self.stack)==0:
#             print("its empty")
#         else:
#             self.stack.pop()
            
#     def top(self):
#         if len(self.stack)==0:
#             print("its empty")
#         else:
#             return self.stack[-1]
        
#     def is_empty(self):
#         return len(self.stack)==0
    
#     def size(self):
#         return len(self.stack)
    
    
# a= stack()
# a.push(1)
# a.push(2)
# a.push(3)
# print(a.top())
# a.pop()

# a.pop()

# a.pop()
# print(a.top())
# print(a.is_empty())



