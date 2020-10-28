#!/usr/bin/python3

n = int(input())
s = input()
i = s.count("A")

if i > n/2:
    print("Anton")
elif i < n/2:
    print("Danik")
elif i == n/2:
    print("Friendship")
