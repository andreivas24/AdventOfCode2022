import os

maxi, sum, sumMax = 0, 0, 0
maxiNum = []

with open('./input.txt', 'r') as file:
    input = [i for i in file.read().strip().split("\n")]

#First part of problem
# for c in input:
#     if c == "":
#         if sum > maxi:
#             maxi = sum
#         sum = 0
#     else:
#         sum = sum + int(c)

# print("Number of calories:", maxi)

#First part of problem
    for c in input:
        if c == "":
            maxiNum.append(sum)
            sum = 0
        else:
            sum = sum + int(c)

    for c in range(3):
        sumMax = sumMax + max(maxiNum)
        maxiNum.remove(max(maxiNum))

print("First 3 numbers:", sumMax)