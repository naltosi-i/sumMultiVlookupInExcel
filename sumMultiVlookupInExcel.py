import os
from datetime import datetime

now = datetime.now()
str_now = f'{now:%Y-%m-%d_%H:%M:%S}

s = 'test'

log_path = '\log' + str_now +'.txt'

with open(log_path, mode='a', encoding='utf-8') as f: # output text file
    f.write(s)

print("End")

#this programm is End