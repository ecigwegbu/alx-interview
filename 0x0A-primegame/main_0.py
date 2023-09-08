#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


# print("Winner: {}".format(isWinner(5, [1, 1, 1, 0, 0])))
nums = [0] * 10000
for i in range(10000):
    nums[i] = i

print("Winner: {}".format(isWinner(10000, nums)))
