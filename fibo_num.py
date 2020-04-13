#!/usr/bin/python3

num = int(input("Which Fibonacci sequence do you wnat to generate: "))

a = 1
b = 1
tmp = 0
cnt = 0

while cnt<num:
    if cnt == 0:
        print(a, end='')
    elif cnt == 1:
        print(b, end='')
    else:
        print(a+b, end='')
        tmp = a
        a = b
        b = tmp+b

    cnt+=1

    if cnt==num:
        break

    print(", ", end='')

print("")
print("F{} = {}".format(num, b))
