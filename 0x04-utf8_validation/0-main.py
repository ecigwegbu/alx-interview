#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))

data = [0b11110000, 0b10010101, 0b10011010, 0b10011010]
print(validUTF8(data))

data = [0b11110000, 0b10010101, 0b10011010, 0b00011010]
print(validUTF8(data))

data = []
print(validUTF8(data))

data = [0]
print(validUTF8(data))
