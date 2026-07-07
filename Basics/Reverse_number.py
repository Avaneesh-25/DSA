class Solution:
    def reverse(self, x: int) -> int:
        reverse_number = 0
        negative= x < 0
        x = abs(x)

        while x > 0:
            last_digit = x % 10
            x = x // 10
            reverse_number = reverse_number * 10 + (last_digit)
        
        if negative:
            reverse_number =  -reverse_number

        return reverse_number


