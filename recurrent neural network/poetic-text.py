# import requests
# from bs4 import BeautifulSoup


# url="https://storage.googleapis.com/download.tensorflow.org/data/shakespeare.txt"

# response = requests.get(url)

# if response.status_code==200:
#     soup = BeautifulSoup(response.content,"html.parser")
#     text= soup.get_text()
#     with open("output.txt",'w',encoding='utf-8') as f:
#         f.write(text)
        
#     print("text has been written")
    
# else:
#     print("failed to write the content",requests.status_codes)
    
    
# -------------------------------------------------------------------------------


import random
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.layers import Activation, Dense, LSTM


filepath = "./output.txt"
try:
    with open(filepath,'rb') as f:
        
        text = f.read().lower()
        print("the file was read")
        
except FileNotFoundError:
    print("the file was not found")
    
except Exception as e :
    print(f"an error has occured: {e}")



te= text[300:800000]
character = sorted(set(te))


char_to_index = dict((c,i) for i ,c in enumerate(character))
index_to_char= dict((i,c) for i ,c in enumerate(character))

# print(char_to_index)
# print(index_to_char)
# for character in character:
#     print(f"Unicode: {character}, Character: {chr(character)}")
#     print(character)

# seq_lenght= 40
# step_size =3

# sentence=[]
# next_char=[]


# for i in range (0,len(te)-seq_lenght,step_size):
#     sentence.append(te[i:i+seq_lenght])
#     next_char.append(te[i+seq_lenght])

