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

class Stack:
    def __init__(self):
        self.item = []

    def is_empty(self):
        return self.item == []

    def push(self, value):
        self.item.append(value)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            return "stack is empty"

s = Stack()
running = True

def push_value(value):
    s.push(value)
    print(f"Pushed {value}")

def pop_value():
    print(s.pop())

def quit_program():
    global running
    running = False

operations = {
    'push': push_value,
    'pop': pop_value,
    'quit': quit_program
}

while running== True:
    print('push <value>')
    print('pop')
    print('quit')
    do = input("What would you like to do? ").split()
    
    operation = do[0].lower()
    if operation in operations:
        if operation == 'push' and len(do) > 1:
            operations['push']
        elif operation != 'push':
            operations['pop']
        else:
            print("Please provide a value to push.")
    else:
        print("Invalid operation. Please try again.")
