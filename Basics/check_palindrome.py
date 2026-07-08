n =int(input())
reverse_num = 0
dup = n
while n > 0:
    last_digit = n % 10
    n = n // 10
    reverse_num = reverse_num * 10 + last_digit
print(reverse_num, end="")
 
if reverse_num == dup:
    print("palindrome")
else:
    print("not palindrome")