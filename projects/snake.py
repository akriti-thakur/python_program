# creating python game  
import random

def game(): 
    print("!!!!!!!!!!!!!!!!!!!!!welcome!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
    you=input("your turns : snakw(s) \nwater(w) \n gun(g)\n")
    
    print("computer turns : snake(1) \n water(2) \n gun(3)\n")
    
    r = random.randint(1,3)
   
    print(r)  
    if r == 1:
      c = "s"
      
    elif r ==2:
        c="w"
    elif r== 3:
        c ="g"
        
      
        
    if c == you:
        return False
    elif c ==  's':
        if you== 'w':
            return False
        elif you == 'g':
            return True
        
    elif c == 'w' :
        if you == 'g':
            return False
        elif you == 's':
            return True
    elif c =='w':
        if you == 'g':
            return False
        elif you == 's':
            return True 
    
      
def head():
       print("--------welccome     to      the      game ------ \n")
    
       m = input("enter : \n(s) to start \n(e) to exit \n")
       if m == "s":
        game()
        
     
     
       if m =="e":
         print("*********thank you for coming here*********")
         exit
  
 
 
 
head() 

    


def m ():
   
        
    
      a = game()
      if a == None:
       print("the game is a tie!!!!!!!!!!")
    
      elif a :
        print("you win !!!")
    
      else:
        print('you lose!')   
m() 





