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
#     print("failed to wriet the content",requests.status_codes)
    
    
# -------------------------------------------------------------------------------


import random
import numpy as np
import tensorflow as tf


filepath = "./output.txt"

text = open(filepath, 'rb').read().decode(encoding='utf-8')
if text:
    print("text is loaded")
    
else e.FileExistsError:
    print(e)