#!/usr/bin/python

s = raw_input()
u = set(s)
u_len = len(u)

if u_len % 2 == 0 :
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
