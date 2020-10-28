#!/usr/bin/python

a, b = map(int, raw_input().split())
x = 0

while a<=b:
    x = x + 1
    a = x * (a*3)
    b = x * (b*2)

print(x)

