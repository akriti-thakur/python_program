# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     global n 
#     def solve(self, A,a):
#         n=len(a)
#         for i in range(n):
#          A.append(a)
#          A.sort()
         
#         print("the 2nd highest elemet is ",A[n-1])  
       
# objec=Solution()
# A=[]
# a=input("enter the elements:\n")

    

# objec.solve(A,a)








# import random  
# n=int(input("enter the number of time you want to flip coin"))

# head =0
# tail =0
# flip=random.randint(0,1)
# for flip in range (0,n):
#     if flip==1 : 
#         print("its tail")
#         tail = tail+1
        
#     else :
#         print("its head")
#         head =head+1
    
    
# print(f"the number of head are {head} and the number of tail is {tail}")


# import random
# def heads_or_tails():
#     result = random.randint(0, 1)
#     if result == 0:
#         return "Heads"
#     else:
#         return "Tails"
# Run the function 10 times and count the number of heads and tails
# num_heads = 0
# num_tails = 0
# for _ in range(10):
#     result = heads_or_tails()
#     if result == "Heads":
#         num_heads += 1
#     else:
#         num_tails += 1
# print(f"Heads: {num_heads}")
# print(f"Tails: {num_tails}")
# class e():
#     def __init__(self,*args):
#         # self.speed=args[0]
#         # self.color=args[1]
#         self.nun=n
        
        
# audi=e(20,"flor") 
# print(audi.color)
# import pandas as pd

# # Create a sample DataFrame
# df = pd.DataFrame({
#     'Cntr_No': ['HLBU 1234567', 'HLBU 1234567'],
#     'Total_Amount': [100, 100]
# })

# # Identify duplicates and create a new column
# df['Duplicate'] = df.duplicated(keep=False).map({True: 'Yes', False: 'No'})

# print(df)

# Python program to Sort square
# of the numbers of the array
# Function to sort an square array


# def sortSquare(arr, n):
    
#     for i in range(n):
#        arr[i]= arr[i] * arr[i]
#     arr.sort()
#     # Driver code
# sortSquare([-6, -3, -1, 2, 4],5)

# def main():
#     num= int(input("enter the length of array"))
#     x=int(input("enter the position"))
    
#     a=[]
#     for _ in range(num):
#         num= input("enter the elemets ")
#         a.append(num)
#         print(a)   
        
        
#     m(x,a)  
     
# def m(n,arr):    
#     if n<1 or n>len(arr):
#          print("invalid ")
    
    
#     else:
#         arr.pop(n)
#         print(arr)
     

# if __name__=="__main__":
#     main()




# def lar(a,n):
#     first_largest = 0
#     second_largest = -1
    
    
#     for i in range(n):
#        if a[i]>a[first_largest]:
#           second_largest =first_largest
           
#           first_largest=i
          
          
#        elif a[i]<a[first_largest]:
#            if second_largest == -1 or a[second_largest] < a[i]:
#                second_largest =i 
    
#     print(a[first_largest])           
#     print  (a[second_largest])
    
   
           
           
           
           
# def main():
#     arr=[3,5,1,5,6,2]
 
#     m=len(arr)
#     lar(arr,m)
    
    
# if __name__=="__main__":
#     main()


# import numpy as np

# def ma(mat):
    
#     a=np.array(mat)
#     n,m= a.shape

#     if n!=m:
#         print("matrix should be square")
#     else:
#         for i in range(n):
#             for j in range(m):
#                 if i == j:
#                     if a[i, j] != 1:
#                         return False
#                 else:
#                     if a[i, j] != 0:
#                         return False
                       
#     return True


# x=[
#          [1, 0, 0],
#     [0, 1, 0],
#     [0, 0, 1]
#      ]
# result=ma(x)

# if result:
#     print("true")
    
# else:
#     print("false")

# def get_index(tup,elem):
#     try:
#         index=tup.index(elem)
#         return index
        
#     except ValueError:
#         return -1
    
    
# def main():
#     my_t=(10, 20, 30, 40, 50)
#     element=15
#     result=get_index(my_t,element)
#     if result != -1:
#         print(result)    
        
#     else:
#        print("not found ")
    
# if __name__=="__main__":
#     main()




# input_tuple = ("9"," 2", "3", "7"," 5", "4")
# # t=tuple(int(x) for x in input_tuple)
# p=[]
# m=[]
# for i in range(input_tuple):
#     if input_tuple.index(i) %2 ==0:
#         p.append(i)
        
#     else:
#         m.append(i)
        
# print(p)


# def odd_even_split_tuple(tup):
    
#     even=tup[1::2]
#     odd=tup[::2]
    
#     print(f"Odd:{odd}")
#     print(f"Even: {even}")
  

# def main():
#    tupw=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
#    odd_even_split_tuple(tupw)
    
# if __name__=="__main__":
#     main()




# class node :
#     def __init__(self,value):
#         self.data=value 
#         self.next=None
        
# a=node(1) 
# print(a.data



# # --------------------------------------------------------------------------
# Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.

# In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.



# class mm:
#     def m(self, arr, n):
#         sum = 0
#         start = 0
        
#         for i in range(len(arr)):
#             sum += arr[i]
            
#             while sum > n and start < i:
#                 sum -= arr[start]
#                 start += 1
            
#             if sum == n:
#                 return [start, i]  # 1-based indexing
        
#         return [-1]

# # Example usage
# arra = [15, 2, 4, 8, 9, 5, 10, 23]
# s = 23   
# obj = mm()
# result = obj.m(arra, s)
# print(result)  # Output: [2, 5]
