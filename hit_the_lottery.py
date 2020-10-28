#!/usr/bin/python3

i = int(input())
k = 0

while i % 1:
    k = k + 1
    if i % 100 == 0:
        i = i / 100
    elif i % 20 == 0:
        i = i / 20
    elif i % 10 == 0:
        i = i / 10
    elif i % 5 == 0:
        i = i / 5
    elif i % 1 == 0:
        i = i / 1

print(i)