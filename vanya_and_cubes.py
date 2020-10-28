#!/usr/bin/python3

n = int(input())
i = 0
j = 0

while i <= n:
    j += 1
    i += (j*(j+1))/2
print(j-1)
