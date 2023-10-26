class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        
        # Idea is try to find the index of monotone and once found try decreasing it and get the next values
        
        digits = list(str(n))
        n = len(digits)
        idx_to_modify = n  

        for i in range(n - 1, 0, -1):
            if digits[i] < digits[i - 1]:
                idx_to_modify = i
                digits[i - 1] = str(int(digits[i - 1]) - 1)
        
        for i in range(idx_to_modify, n):
            digits[i] = '9'
        
        return int("".join(digits))
        
        
        
        