
# n=0
# mm=open("mm.txt","r")
# lines= mm.read().split()

# for a in lines:
#     if (a.startswith=="M" or a.startswith=="i"):
#        n += 1
       
# print("the number iss ",n) 
# mm.close()


# class s(object):
#     def __init__(self):
#         self.a=1
#         self.b=2
# obj=s()
# print(obj.__dict__)




# name=["ankita","rohini","sristi"]
# letter =  '''hello  </name>
#             we inform you that dur to your poor performane in academics you are ,
#             hereby  told that you have stay at school for extra classes.
            
#             date: </date>
            
# '''



# while (i<len[name]):
# {
#     i=i+1
#       letter=letter.replace
    
    
# }
# class aa():
#       def __init__(self):
#             self.a=1
#             self.b=3

# a=aa()
# print(a.__dict__)    
        
        
        
        
    
# d={'a':"1",
#    'b':"2",
#    'c':"3"}
# key=input("Enter key to check:")
# if key in d.keys():
#       print("Key is present and value of the key is:")
#       print(d[key])
# else:
#       print("Key isn't present!") 
       

# patterns question

# def f(n):
#     for i in range (0,n):
#         for j in range (0,i+1):
#             print("*",end="")
            
            
#         print("\r")
        
        
# d=f(5)
# print(d)     




# by list


# def f(n):
#     list=[]
#     for i in range(0,n):
#         list.append("*"*i)
#     print("\n".join(list))


# /////////////////////////////////////////////////////////////////////////////////////////////////////////////

    
# n=5
# f(n)
# a=1
# b=4
# n="my name is akriti "
# print(n[a:b])


# def main():
#    str1 = "Hello"
#    str2 = "World"
#    print(str1+str2)
   
#    return 0
# if __name__=="__main__":
    
    
# class Solution:
   
#     def solve(self, A, B, C):
     

#        print(A[B:C])

# mm=Solution()
# mm.solve("rishabh",1,2)




# def f(n):
#     for i in range (n,0,-1):
#         for j in range (1,i+1):
#             print(j,end="")
            
            
#         print("\r")
        
        
        
# m=f(5)
# # m


# def test(t,n):
#     t=2
#     n[0]=3
# x=3
# nums=[1,2,3]
# test(x,nums)
# print(nums)
# print(x)


# ture or false

# ********************************************************************************************

# n=[1,2,3]
# n+=[4,5]    how to append
# print(n)

# n=[1,2,3]
# n[len(n):]=[4,5]
# print(n)

# import math
# def volume_sphere(r):
#     '''input: r = Input in integer format
#        output:return Vol of sphere upto two decimals'''
#     # YOUR CODE GOES HERE
#     pie=22/7;  
#     m=(4.0/3.0)*pie*(r*r*r); 
#     vol= math.ceil(m)
    
    
    
#     return vol



# print(volume_sphere(8))


# class Solution:
#     # @param A : string
#     # @param B : string
#     # @return a strings
#     def solve(self, A, B):
       
#         print(A+B)


# mm=Solution()
# mm.solve("interview","bit")

# to find the highest from the array

# marks=[10,70,80,90,55,95,88]
# high=marks[0]
# # print(high)

# for i in marks:
#     if i > high:
#         high=i
        
        
# print(high)


# row=int(input("enter the number of rows:-"))

# col=int(input("enter the number of col:-"))
# c=[[0]*row]*col
# print(c)
# for i in range(col):
#     for j in range(row):
#      print("[0]")
  
  
# print("\n")


# student=[]
# maths=[]
# science=[]
# hindi=[]
# percentage=[]


# a=input("enter the name")
# b=int(input("enter the marks "))
# c=int(input("enter the marks "))
# d=int(input("enter the marks "))

# student.append(a)
# maths.append(b)
# science.append(c)
# hindi.append(d)

# marks=(maths+science+hindi/300)*100










# Given a positive integer A, return an array of strings with all the integers
# from 1 to N. But for multiples of 3 the array should have “Fizz” 
# instead of the number. For the multiples of 5, 
# the array should have “Buzz” instead of the number. 
# For numbers which are multiple of 3 and 5 both, the array should have 
# "FizzBuzz" instead of the number.

# def fizz_buzz(A):
#     result = []
#     for i in range(1, A+1):
#         if i % 3 == 0 and i % 5 == 0:
#             result.append("FizzBuzz")
#         elif i % 3 == 0:
#             result.append("Fizz")
#         elif i % 5 == 0:
#             result.append("Buzz")
#         else:
#             result.append(i)
            
            
#     print(str(result))


# fizz_buzz(15)


# even number 

# def star_pattern(n):
#     '''input: n = An Integer value defines number of rows
#        output: print triangle star pattern'''
#     # YOUR CODE GOES HERE
#        # number of spaces
#     for i in range(n):
#        print(' ' * (n - i - 1) + '*' * (2 * i + 1))

# star_pattern(5)


# n=5
# for i in range (0,n):
#     print((n-i-1))



# a=[]
# n=int(input("enter the number of elements: \n"))
# for i in range (n+1):
#     b=input(f"enter the elements  {i+1}\n")
#     a.extend(b)
#     a.append(b)
    
    

#     a.sort()
# print(a)

# print ("the largest element",a[n-0])

# def fac(n):
#     if n==1:
#         return 1
    
#     else:
#         return n*fac(n-1)

    
    
    
# print(fac(5))

# year=2024
# if (year%4 ==0 and year%100 != 0 ):
#     print("its a leap year")
    
    
# else:
#     print("its not a leap year")






# a= input("enter the sentence ")
# b=a.split()
# print(b)
# c=set(b)
# print(c)

# print(len(c))



# def mm(sen1,sen2):
#     one=sen1.split()
#     two=sen2.split()
    
#     u=set(one)
#     w=set(two)
#     print(u,w)
#     return len(u)+len(w)



# d=mm("hello my name is called out","bye my name is called out ")
# print(d)
  
  
# for i in range(0,200):
#     print("hmmm")
# 
# import math

# def min_steps_to_turn_on_bulbs(A):
#     # Find the largest perfect square less than or equal to A
#     largest_perfect_square = int(math.sqrt(A))
    
#     # The answer is the square root of the largest perfect square
#     return largest_perfect_square

# # Example usage
# A = int(input("Enter the number of bulbs (A): "))
# result = min_steps_to_turn_on_bulbs(A)
# print(f"Minimum steps to turn on all bulbs: {result}")


# class solution:
#     def solve(self,A):
#        A= int (input("enter the number of bulbes:-")) 
        
        
# class s(solution):
#     def m():
       
#         largest = int(math.sqrt(A))
         
#         return largest
        
# mm= m()
# mm()




# print(f"Minimum steps to turn on all bulbs: {largest_perfect_square}")
# Function to demonstrate printing pattern of alphabets




# def first_unique_char(s):
#     # Dictionary to store the frequency of each character
#     char_count = {}
    
#     # Count the frequency of each character
#     for char in s:
#         char_count[char] = char_count.count()
    
#     # Find the index of the first unique character
#     for index, char in enumerate(s):
#         if char_count[char] == 1:
#             return index
    
#     # If there are no unique characters
#     return -1

# # Example usage
# s = "swiss"
# print(f"The index of the first unique character is: {first_unique_char(s)}")
# ---------------------------------------------------------------------------------------------------


# # Python3 code to validate a password

# # A utility function to check
# # whether a password is valid or not
# def isValid(password):

# 	# for checking if password length
# 	# is between 8 and 15
# 	if (len(password) < 8 or len(password) > 15):
# 		return False

# 	# to check space
# 	if (" " in password):
# 		return False

# 	if (True):
# 		count = 0

# 		# check digits from 0 to 9
# 		arr = ['0', '1', '2', '3', 
# 		'4', '5', '6', '7', '8', '9']

# 		for i in password:
# 			if i in arr:
# 				count = 1
# 				break

# 		if count == 0:
# 			return False

# 	# for special characters
# 	if True:
# 		count = 0

# 		arr = ['@', '#','!','~','$','%','^',
# 				'&','*','(',',','-','+','/',
# 				':','.',',','<','>','?','|']

# 		for i in password:
# 			if i in arr:
# 				count = 1
# 				break
# 		if count == 0:
# 			return False

# 	if True:
# 		count = 0

# 		# checking capital letters
# 		for i in range(65, 91):

# 			if chr(i) in password:
# 				count = 1

# 		if (count == 0):
# 			return False

# 	if (True):
# 		count = 0
# 		# checking small letters
# 		for i in range(97, 123):

# 			if chr(i) in password:
# 				count = 1

# 		if (count == 0):
# 			return False

# 	# if all conditions fails
# 	return True

# # Driver code
# password1 = "GeeksForGeeks"

# if (isValid([i for i in password1])):
# 	print("Valid Password")
# else:
# 	print("Invalid Password!!!")

# password2 = "Geek$ForGeeks7"
# if (isValid([i for i in password2])):
# 	print("Valid Password")
# else:
# 	print("Invalid Password!!!")

# --------------------------------------------------------------------------------
# def  printnum(n,m):
#    if  n== 0:
#        return m
#    return printnum(n-1,n+m)


# s=printnum(4,5)
# print(s)

# -------------------------------------------------------------------------

# def fun(n):
#     if n > 1:
#         fun(n - 1)
#     for i in range(n):
#         print(" * ", end='')

# # Example call
# if __name__ == "__main__":
#     fun(4)

# import required modules


# ---------------------------------------------------


