
# from random import randint
# from collections import Counter
# import pandas as pd
# import matplotlib.pyplot as py


# def main():
#     fu= lambda x:'tails' if x else 'head'
#     n=int(input("enter the number of "))
#     arr=[fu(randint(0,1))for i in range (n)] 

#     print(arr)
#     print(Counter(arr))
#     colle=pd.DataFrame(arr,columns=['mole'])
#     colle=colle.value_counts()
#     colle.plot(kind='bar')
#     py.show()
  
     
# if __name__=="__main__":
#     main()
    
    
# arr = list(map(int , input().strip().split()))

# print(arr)

# class per:
#     def __init__(self,n):
#         self.n=n
# class A:
#     def __init__(self, something):
#         print("A init called")
#         self.something = something

# class B(A):
#     def __init__(self, something):
#         # A.__init__(self, something)
#         print("B init called")
#         self.something = something

# obj = B("s")







# Output:
# A init called
# B init called


# import random 
# from time import sleep
# import matplotlib.pyplot as plt

# name = lambda a : "tails" if a else "heads"

# n = int(input('Enter the number of cases : '))

# coins = int(input('Enter the number of coins : '))

# result =[]

# for i in range(n):
# 	arr = [name(random.randint(0,1)) for _ in range(coins)]
# 	result.append(arr)

# h = [0]*(coins+1)

# head_counts = [ trial.count('heads') for trial in result ]

# ans = [ head_counts.count(i) for i in range(coins + 1) ]

# print(ans)

# plt.bar( range(coins + 1) , ans )
# plt.xlabel('Number of Heads')
# plt.ylabel('Frequency')
# plt.title('Heads Distribution in Coin Flips')

# plt.show()

# import pandas as pd
# import random
# import matplotlib.pyplot as plt

# Function to simulate a coin toss
# def toss_coin():
#     return 'Head' if random.randint(0, 1) == 0 else 'Tail'

# Simulate 1000 tosses
# tosses = [toss_coin() for _ in range(1000)]
# print(tosses)

# Create a DataFrame
# df = pd.DataFrame(tosses, columns=['Outcome'])

# # Get the distribution of outcomes
# distribution = df['Outcome'].value_counts()
# print(distribution)

# # Plot the distribution
# distribution.plot(kind='bar')
# plt.show()

# def commonKey(dict1, dict2):
#      comman=set(dict1.keys())&set(dict2.keys())
#      print(comman)
#      di={}
#      for keys in comman:
#          di[keys] = dict1[keys]+dict2[keys]
  
#      return di

# def main():
#     dictonary={
#         'a':1,
#         'b':2,
#         'c':3
#     }
#     mm={
#         'c':4,
#         'd':5,
#         'e':6
#     }
#     result=commonKey(dictonary,mm)
#     print(f"{result}")
    
        
        
# if __name__=="__main__":
#     main()

# -----------------------------------------------------------------------------

# class Text(object):
#     def __init__(self, text):
#         self.text = text
        
#     def non(self):
#         formattedText = self.text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')
#         formattedText = formattedText.lower()
#         self.m = formattedText

#     def mm(self):
#         self.non()  # Ensure the text is formatted before splitting
#         listo = self.m.split()
        
#         fre = {}
#         for word in set(listo):
#             fre[word] = listo.count(word)
            
#         return fre
    
#     def mmmm(self, word):
#         freqDict = self.mm()
        
#         if word in freqDict:
#             return freqDict[word]
#         else:
#             return 0
        
# def main():
#     givenstring = "Lorem ipsum dolor! diam amet, consetetur Lorem magna. sed diam nonumy eirmod tempor. diam et labore? et diam magna. et diam amet."
#     text_instance = Text(givenstring)
    
#     # Print the frequency dictionary
#     freq_dict = text_instance.mm()
#     print("Frequency dictionary:", freq_dict)
    
#     # Print the frequency of a specific word
#     word = "diam"
#     word_freq = text_instance.mmmm(word)
#     print(f"The frequency of the word '{word}' is:", word_freq)

# if __name__ == "__main__":
#     main()


# --------------------------------------------------------------------------
# from collections import Counter 

# a="aaaaaabbcccccc"
# m=Counter(a)

# print(m.items())
# my=[1,1,23,4,21,1,1,1,23,23,4]
# m=Counter(my)
# print(m)


# for keys in m.keys():
#     print(f"{keys}: {m[keys]}")


# from collections import Counter

# def min_sum_after_removal(arr):
#     # Count occurrences of each element
#     counts = Counter(arr)
#     # Calculate initial sum of array
#     total_sum = sum(arr)
    
#     # Initialize minimum sum as the initial sum
#     min_sum = total_sum
    
#     # Iterate over each unique element
#     for num in counts:
#         # Calculate what the sum would be if we removed all occurrences of this element
#         current_sum = total_sum - (num * counts[num])
#         # Update min_sum if current_sum is smaller
#         min_sum = min(min_sum, current_sum)
    
#     return min_sum

# # Example usage:
# arr = [4, 5, 6, 6 ]
# print(min_sum_after_removal(arr))  # Output should be the minimum sum possible




# Remove all occurrences of any element for min array sum
# from collections import Counter

# def m(arr):
#     counts= Counter(arr)
#     total=sum(arr)
    
    

#     m=total
#     for num in counts:
#         curr= total-(num*counts[num])
        
#         m=min(m,curr)
        
#     return m 
     
# def main():
#     ar=[1,1,5,6,6,7,8]
#     print(m(ar))
  
    
# if __name__=="__main__":
#     main()



# class Solution:
#     def __init__(self, arr):
#         self.arr = arr

#     def find_majority_element(self):
#         candidate = None
#         count = 0
        
#         for num in self.arr:
#             if count == 0:
#                 candidate = num
#                 count +=1
#             else:
            
#              count += (1 if num == candidate else -1)
        
#         return candidate

# # Example usage:
# A = [ 1, 1, 2 ,3,3,3]
# finder = Solution(A)
# print(finder.find_majority_element())
# boyer-moore voting algo


# from collections import Counter

# class solu:
#      def __init__(self,arr):
#          self.arr=arr
         
         
#      def  find(self):
#          m=Counter(self.arr)
#          print(m)
#          print(m.items())
#          maj=max(m.values())
#          print(maj)
#          for item,count in m.items():
#              if count== maj:
#                  return item
# A=[1,2,3,3,1,1,1,1]
# f=solu(A)
# print(f.find()) 

# Remove an occurrence of most frequent array element exactly K times
# from collections import Counter
# a=[1,1,1,1,2,2,3,3]

# m=Counter(a)
# print(m)

    

# most=m.most_common(1)[0][0]
# print(most)

# k=2
# tota=0
# m[most]=m[most]-1
# # m[most]=max(0 ,m[most]-k)
# print(m)
# for i,count in m.items():
#     tota +=i*count
    
# print(tota)
# --------------------------------------------------------
# ---------------------------------------------------------------------------------

# Find a peak element which is not smaller than its neighbours

# def find_element(arr, no):
#     sorted_arr = sorted(arr)  
#     print(sorted_arr)
#     print("The element is", sorted_arr[no-1])

#     max_value = max(arr)
#     index = arr.index(max_value)
#     print("The index of the max element is", index)

# def main():
#     arrr = [1, 3, 4, 90, 69]
#     noo = len(arrr)
#     find_element(arrr, noo)

# if __name__ == "__main__":
#     main()

# import timeit
# setup_code = """
# from __main__ import main
# """

# test_code = """
# main()
# """

# execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1)
# print("Execution time in seconds:", execution_time)



# OR-----------------------------



# def peak(arr,n):
    
#     if n==1:
#         return 0
    
#     elif arr[0]>= arr[1]:
#         return 0
    
#     elif arr[n-1] >= arr[n-2]:
#         return n-1
 
#     else:
#         for i in range(1,n-1):
#             if arr[i]>=arr[i-1] and arr[i]>=arr[i+1]:
#                 return i
            
            
      

            

# def main():
#     array=[1,3,20,4,1,0]
#     length=len(array)
#     peak_index=peak(array,length)
#     print(f"the index of peak element is {peak_index}, and the lement is {array[peak_index]}")
    
# if __name__=="__main__":
#     main()


# import timeit

# setup_code = """
# from __main__ import peak
# array = [1, 3, 20, 4, 1, 0]
# length = len(array)
# """

# test_code = """
# peak(array, length)
# """

# execution_time = timeit.timeit(stmt=test_code, setup=setup_code, number=1000)
# print("Execution time in seconds:", execution_time)


# Time complexity: O(n), One traversal is needed so the time complexity is O(n)
# Auxiliary Space: O(1), No extra space is needed, so space complexity is constant



