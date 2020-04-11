print("Write a number:")
num = int(input())

res = 1;
if num <= 1: res = 0
else:
    if num == 2: res = 1
    else:
        for i in range(2, int(num/2) + 1):
            if num % i == 0:
                res = 0
                break
            res = 1

if res == 1:
    print("YES")
else:
    print("NO")
