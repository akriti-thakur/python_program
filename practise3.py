
# class node:
#    def __init__(self,value):
#      self.data=value
#      self.next=None
     



# class ll():
#   def __init__(self):
#     self.head=None
#     self.n=0
    
#   def insert_head(self,value):
#       new_node=node(value)
#       new_node.next=self.head
#       self.head= new_node
#       self.n=self.n+1
      
      
      
#   def __len__(self):
#     return self.n
      
      
# a= ll(insert_head(1))
# print(a)

# --------------------------------------------------------

# Python – Extract words starting with K in String List

# test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]
# print("the original string is: ",str(test_list))

# k="g"
# res=[]
# x=[]
# for i in test_list:
#     x.extend(i.split()) 
#     print(x)
# for i in x:
#     if i.startswith(k)or i.startswith(k.lower())or i.startswith(k.upper()):
#         res.append(i)
        
#  Time Complexity: O(n*n) where n is the number of elements in the list “test_list”. 
# Auxiliary Space: O(n*n) where n is the number of elements in the list “test_list”.        
        
# print(f"the result is {res}")
# -------------------------or -------------------------

# initializing list
test_list = ["Gfg is best", "Gfg is for geeks", "I love G4G"]
 
# printing original list
print("The original list is : " + str(test_list))
 
# initializing K
K = "g"
 
res = []
for i in test_list:
    words = i.split()
    startWords = list(filter(lambda x: x[0].lower() == K.lower(), words))
    res.extend(startWords)
 
# printing result
print("The filtered elements : " + str(res))