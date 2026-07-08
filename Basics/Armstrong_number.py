n = int(input())
original = n
sum = 0
digits = len(str(n))
while n > 0:
    last_digit = n % 10
    n = n // 10
    sum = sum + last_digit ** digits
print(sum, end="")
if sum == original:
    print("Armstrong number")
else:
    print("Not Armstrong number")    