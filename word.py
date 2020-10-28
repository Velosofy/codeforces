#!/usr/bin/python3

s = input()
lc = 0
uc = 0

for i in s:
    if(i.islower()):
        lc=lc+1
    elif(i.isupper()):
        uc=uc+1

if lc < uc:
    s = s.upper()
else:
    s = s.lower()

print(s)
