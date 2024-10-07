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

# class stack:
#     def __init__(self):
#         self.q = Queue()

