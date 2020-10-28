#!/usr/bin/python

text = raw_input()
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
result = ''

for letter in text.lower():
    if letter not in vowels:
        result = result + '.' + letter

print(result)
