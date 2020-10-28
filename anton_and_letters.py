#!/usr/bin/python3

s = input()
alphabets = "abcdefghijklmnopqrstuvwxyz"
result = 0

for i in alphabets:
    if i in s:
        result = result + 1
        
print(result)