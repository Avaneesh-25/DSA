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

#leetcode problem
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        original = x
        reverse_num = 0

        while x > 0:
            last_digit = x % 10
            x = x // 10
            reverse_num = reverse_num * 10 + last_digit

        return reverse_num == original
'''        