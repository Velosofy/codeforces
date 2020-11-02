#!/usr/bin/python3

n, k = map(int, input().split())
i = 0

while i < k:
    i = i + 1
    if n % 10 == 0:
        n = n / 10
    else:
        n = n - 1
print(int(n))
