n = int(input())
original = n
sum = 0
while n > 0:
    last_digit = n % 10
    n = n // 10
    sum = sum + last_digit ** 3
print(sum, end="")
if sum == original:
    print("Armstrong number")
else:
    print("Not Armstrong number")    