class Solution:
    def reverse(self, x: int) -> int:
        while x > 0:
            last_digit = x % 10
            x = x // 10
            reverse_number = reverse_number * 10 + (last_digit)
        return reverse_number
