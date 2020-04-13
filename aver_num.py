#!/usr/bin/python3

num = int(input("How many number: "))

tmp = 0
cnt = 0
sum_num = 0

while num > cnt:
    tmp = int(input("number input: "))
    sum_num += tmp
    cnt+=1

average = sum_num / num

print("average: ", average)

