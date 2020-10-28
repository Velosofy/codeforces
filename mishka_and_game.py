#!/usr/bin/python3

i = int(input())
j = 0
m = 0
c = 0

while i > j:
    j += 1
    x, y = map(int, input().split())
    if x > y:
        m += 1
    elif x < y:
        c += 1

if m > c:
    print("Mishka")
elif m < c:
    print("Chris")
else:
    print("Friendship is magic!^^")


