

# a=input("enter the string \n")
# b=a.split()
# z=b.find("akriti")
# if (z==True) :
#     print("akriti is present \n")
    
# else:
    
#     print("akriti is not present ")



    
# to find if a substring is present in a string 
# a=input("enter the string \n")
# s=input("enter the substring \n")
# w=a.split()

# if s in w:
#     print("yes")
    
# else:
#     print("no")



# # a= "hello"
# z=len[a]


# for i in range (0,z):
#     print(a[i],"\n") 

#to find if a word is present in a string 
# string=input("enter the string \n")
# sub=input("enter the word \n")
# if(string.find(sub)==-1) :
#     print("the word is not   present ")
    
    
# else:
#     print("the word is present")



#to find the common alphabets in strings 
# s=input("enter the string \n")
# r=input("enter the string \n")
# a=list(set(s)&set(r))
# print("common letter are ")
# for i in a :
#     print(i)
# print(type(a))


# person={
#     "name":"rohin",
#     "class":"btech",
#     "age":"12"
    

# }

# t=" " 
# for  keys in person:
#     t += person[keys]+" "
    
# print(t)
# print (person.keys())

# to check palindrom or reverse the string
# 1
# a=input("enter the string\n")
# rever=""


# for i in a:
#     rever = i+rever
# print("reversed stiring is",rever)


# if a==rever:
#     print("yes")
    
# else:
#     print("no")

# 2
# def pal(string):
#     rev=''.join(reversed(string))
#     if string==rev:
#       return "yes"
      
#     else:
#        return "no"
       
       
# string=input("enter the string")

# print(pal(string))

# 3 for number 
# n=int(input("enter the number\n"))
# tem=n
# rev=0
# while(n>0):
#     dig=n%10
#     rev=rev*10+dig
#     n=n//10
    
# if(tem==rev):
#     print("yes")
    
# else:
#     print("no")

# print(rev)





# revrese a number

# n=int (input("enter the number"))
# num=int(str(n)[::-1])

# print(num)

# to print the number not divisible by 2 and 3

# for i in range(0,51):
#     if(i%2!=0 and   i%3!=0):
#         print(i)


# numbers in a range divisible by a given number

# l=int(input("enter the lower limit range\n"))
# u=int(input("enter the upper limit range\n"))
# n=int(input("enter the number to be divided by \n"))

# for i in range(l,u+1):
#     if(i%n):
#         print(i)




# find the sum of digits in a number
# n=int(input("enter the number : "))
# tot=0
# while(n>0):
#     dig=n%10
#     tot=tot+dig
#     n=n//10
    
# print("the total is ",tot)



# by using flags
# r=int(input("enter the upper limit:- \n"))

# flag=False
# if r==1:
#   print("its not a prime number")
  
# elif r>1:
#   for i in range(2,r):
#     if (r%i) ==0:
#       flag=True
#       break
    
    
    
    
# if flag :
#   print(r,"its  not a prime number")
# else:
#   print(r,"is  a prime number")

# -----------------------------------------------------------------------------------

# Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
# For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

# Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".

# def ma(exp):
#     stack=[]
#     bra={')':'(','{':'{','[':'[','<':'<'}
#     for char in exp:
#         if char in bra.values():
#             stack.append(char)
            
#         elif char in bra.keys():
#             if stack ==[] or bra[char] != stack.pop ():
#                 return False
            
#         else :
           
#            continue
    
       
#     return stack ==[]
    

# exp ="}"
# if ma(exp):
#     print("balanced")
# else:
#     print("not balanced")
        
# --------------------------------------------------------------------------     
        
