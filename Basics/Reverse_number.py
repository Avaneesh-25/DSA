class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)

        reverse_number = 0

        while x > 0:
            last_digit = x % 10
            x = x // 10
            reverse_number = reverse_number * 10 + last_digit

        if negative:
            reverse_number = -reverse_number

        if reverse_number < -2**31 or reverse_number > 2**31 - 1:
            return 0

        return reverse_number
