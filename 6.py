__author__ = 'wardcoessens'
import pickle
from urllib import request


f = open('pickle.p', 'rb')
obj = pickle.load(f)

s = ""

for i in obj:
    for c, n in i:
        s += c * int(n)
    s += '\n'

print(s)