#!/usr/bin/python

n, k = map(int, raw_input().split())
i = 0

while i < k:
    i = i + 1
    if n % 10 == 0:
        n = n / 10
    else:
        n = n - 1
print(n)
