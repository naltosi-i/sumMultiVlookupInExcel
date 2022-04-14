import os

s= 'test'

path_l = 'log' + '.txt'

with open(path_l, mode='w') as f: # output text file
    f.write(s)
#this programm is End