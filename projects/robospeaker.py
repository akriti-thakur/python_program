import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice") 
if __name__=="__main__":
    print("wlecome to robo speaker by akriti")
    while True:
      x=input("enter what you want to speak:-\n")
      if x=="q":
        print("thanku for using")
        break
      else:
       speaker.Speak(x) 
  
   
   
   
   
   
# ******************************************************************************************************* 
   