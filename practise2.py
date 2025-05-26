# a=[0,1,0,0]
# count=0
# i=0

# for i in range (len(a)):
#     if a[i]==1:
#        continue
   
#     elif a[i]==0:
#         # print(i)
#         count += 1
        
        
# print(f"the total number of switches required are {count}")
# for i in range (len(a)):
#     if a[i]==0:
#       a[i]= 1
#       count -=1
#       print(a)
#       print(count)


# class exa:
#     @staticmethod 
    
#     def bulb (a,n):
#         count=0
#         i=0
#         while i>n:
#             if a[i]==0:
#                 a[i]=1
#                 j=i+1
#             while  j>n:
#                 if a[j]==1:
#                     a[j]=0
#                 else:
#                     a[j]=1
#             j +=1
                
#         count +=1
#         i +=1
        
#         return count
#     @staticmethod
#     def main(args):
#         state=[0,1,1,1,0,0,0,0]
#         n=len(state)
#         print("the min number of switches required is "+str(exa.bulb(state,n)), end="")
        
        
# if __name__=="__main__":
#          exa.main([])



# class a(object):
#      def __init__(self,something):
#          print("a is called")
#          self.something= "nameis" 
         
         
# class b(a):
#     def __init__(self, something):
#         super().__init__(self)
#         print("b is called0")
#         self.something=something
        
        
# obj = b("something")


# Python3 program to find theSum of all 
# minimum occurring elements in an array
# Python3 program to find theSum of all 
# minimum occurring elements in an array
# from collections import Counter
# def sum_of_min_occurrences(arr):
#     # Count the frequency of each element
#     fre= Counter(arr)
#     # print(fre)
#     # print(fre.values())
#     min_fre=min(fre.values())
    
#     return sum(item for item, count in fre.items() if count == min_fre)
# # Example usage:
# arr = [1, 2, 2, 3, 1, 3, 5, 1, 3,4]
# print(sum_of_min_occurrences(arr))
# OR
# def sum_of_min_occurrences(arr):
   
#     frequency = {}
#     for item in arr:
#         if item in frequency:
#             frequency[item] += 1
#         else:
#             frequency[item] = 1
#     print(frequency)
   
#     min_frequency = min(frequency.values())
    
   
#     return sum(item for item, count in frequency.items() if count == min_frequency)

# arr = [1, 2, 2, 3, 1, 3, 5, 1, 3]
# print(sum_of_min_occurrences(arr))


# i={1,2,3}
# m={1,5,6}
# m=m.union(i)
# print(m)
# sets = {3, 4, 5} 
# sets.update([1,2,3])
# sets = sets.union([1, 2, 3])

# print(sets)
# from collections import Counter
# def unique_count(tup):

#    counting=Counter(tup)
#    for item , count in counting.items():
#      print(f"{item}:{count}")


   
# m=(10, 8, 5, 2, 10, 15, 10, 8, 5, 8, 8, 2)
# unique_count(m)

# _---------------------------------------------------------------------------------------------------
# def unique_count(tup):
#     counts = {}
#     for item in tup:
#         # Convert unhashable types (like lists) to a hashable type (like a tuple)
#         if isinstance(item, list):
#             item = tuple(item)
#         if item in counts:
#             counts[item] += 1
#         else:
#             counts[item] = 1
    
#     for item, count in counts.items():
#         # Convert tuples back to lists for printing
#         if isinstance(item, tuple):
#             print(f"{list(item)}: {count}")
#         else:
#             print(f"{item}: {count}")

# m = (1, 2, 3, 2, "Hello", [4, 8, 16], "Hello")
# unique_count(m)




    

# from collections import Counter

# def h(tup):
#     # Convert lists within the tuple to tuples
#     tup = tuple(tuple(item) if isinstance(item, list) else item for item in tup)
#     m = Counter(tup)

#     # Print the counts
#     for item, count in m.items():
#         # Convert tuples back to lists for printing
#         if isinstance(item, tuple):
#             print(f"{list(item)}: {count}")
#         else:
#             print(f"{item}: {count}")

# mm = (1, 2, 3, 2, "Hello", [4, 8, 16], "Hello")
# h(mm)

# ----------------------------------------------------------------------------------------
# This code defines a function called climbStairs that calculates the number of distinct ways to climb a staircase with A steps. It uses dynamic programming to efficiently compute the result. Here’s how it works:
    
    
    
# def climbStairs(A):
#     if A == 1:
#         return 1
#     if A == 2:
#         return 2

#     # Start with base cases
#     one_step_before = 2
#     two_steps_before = 1

#     # Calculate all other steps
#     for i in range(3, A + 1):
#         all_ways = one_step_before + two_steps_before
#         two_steps_before = one_step_before
#         one_step_before = all_ways

#     return all_ways

# # Example usage:
# A = 6
# print(climbStairs(A))  # Output will be the number of distinct ways to climb A steps


# def check(n):

#    if n<2:
#      return False
    
    
#    for i in range(2,n):
#        if n%i==0:
#            return False
       
       


#        return True



# num=5
# print(check(num))   

# class Solution:
# 	# @param A : integer
# 	# @return an integer
#     def __init__(self, A):
#          self.A=A

#     def prime(self):
         
#          if self.A<2:
#            return False
          
          
#          for i in range(2,self.A):
#              if self.A%i==0:
#                  return False
             
             
      
      
#              return True
         
         
# m=Solution(12)
# print(m.prime())



# class Solution:
# 	# @param A : integer
# 	# @return an integer
#     def __init__(self, A):
#          self.A=A

#     def prime(self):
         
#          if self.A<2:
#            return False
          
          
#          for i in range(2,self.A):
#              if self.A%i==0:
#                  return 1
             
             
      
      
#              return 0
         
         
# m=Solution(84923)
# print(m.prime())

# ṁnbvc---------------------------------------------------------------------------:
#0.0 def missing ( arr):
#     a=[]
#     arr.sort()
#     for i in range(len(arr)-1):
#         dif=arr[i+1]-arr[i]
        
#         if dif>1:
#             for num in range(arr[i]+1,arr[i+1]):
#                 a.append(num)
#     return a

# ar=[8,1,2,9,10,4,5]             
# m=missing(ar)
# print(m)


# multiple array elemnt find 
# single array elemet

# def missing ( arr):
#     a=[]
#     arr.sort()
#     N=len(arr)+1
#     total=(N*(N+1))//2
#     arr_sum=sum(arr)
#     missing=total-arr_sum
#     a.append(missing)
#     return a

# ar=[1,2,5,4,6]             
# m=missing(ar)
# print(m)


# or other by using xor

# def mi(arr):
#     N=len(arr) +  1
   
#     total=  0
#     arr_xor= 0
#     for i in range(1,N+1):
#         total ^=i
        
        
#     for num in arr:
#         arr_xor ^= num
        
#     missing=total ^ arr_xor
#     return missing

# ar=[2, 3, 7, 6, 8, 1, 5]
# m=mi(ar)
# print(m)

# -------------------------------------------------------------------------------
# ------------------------------------------------------------------------------------------

# to find non repetaive element in the array 


# from collections import Counter

# def find_unique_elements(arr):
#      s=Counter(arr)
#      print(s)
#      a=[]
     
#      for item,count in s.items() :
#          if (count==1):
#         #   print(item)
#           a.append(item)
#           print(a)
         
         
     
     
     
     
# my_array = [1, 2, 3, 2, 4, 5, 1, 6]
# unique_elements = find_unique_elements(my_array)
# print(unique_elements)
# ------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------

# Given an unsorted array arr of size n that contains only non negative integers, find a sub-array (continuous elements) that has sum equal to s. You mainly need to return the left and right indexes(1-based indexing) of that subarray.

# In case of multiple subarrays, return the subarray indexes which come first on moving from left to right. If no such subarray exists return an array consisting of element -1.

# def find_subarray_with_sum(arr, s):
#     left, right = 0, 0
#     current_sum = arr[0]

#     while right < len(arr):
#         if current_sum == s:
#             return [left + 1, right + 1]  # 1-based indexing
#         elif current_sum < s:
#             right += 1
#             if right < len(arr):
#                 current_sum += arr[right]
#         else:
#             current_sum -= arr[left]
#             left += 1

#     return [-1]  # No valid subarray found

# # Example usage:
# arr = [1, 4, 20, 3, 10, 5]
# target_sum = 33
# result = find_subarray_with_sum(arr, target_sum)
# print(result)  # Output: [2, 4] (subarray [4, 20, 3] has sum 33)

# ------------------------------------------------------------------------------------------------/

# ----------------------binary_search----------------------------------------------------------------

# def binary_serach (arr,low,high,x):
#     while low<= high :
#         mid = low +(high-low)//2
#         if arr[mid] ==x:
#             return mid
        
#         elif arr[mid]< x :
#             low = mid+1
            
            
#         else:
#             high =mid-1
            
            
            
#     return -1



# if __name__=="__main__":
#     arr=[2,3,4,5,6]
#     x=10
    
    
    
    
# result = binary_serach(arr,0,len(arr)-1,x)
# if result!= -1:
#     print(result)
    
    
    
# else:
#     print("element is  not present in array ")

# --------------------------------------------------------------------------------------------------------------------

# def minDaysWork(n, day1, day2):
#     ans = 0
 
#     # List to store the pair of day1(i) and day2(i)
#     combined = [[] for i in range(n)]
 
#     for i in range(len(day1)):
#         combined[i] = [day1[i], day2[i]]
 
#     # Sort the array
#     combined.sort()
#     for i in range(len(day1)):
#         if (combined[i][1] >= ans):
#             ans = combined[i][1]
#         else:
#             ans = combined[i][0]
 
#     return ans
 
 
# # Driver Code
# # Input taken
# N = 3
# D1 = [6, 5, 4]
# D2 = [1, 2, 3]
# print(minDaysWork(N, D1, D2))

# ---------------------------------------------

print("hello")









