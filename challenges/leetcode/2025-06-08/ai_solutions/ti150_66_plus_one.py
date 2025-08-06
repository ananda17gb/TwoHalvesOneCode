class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        
        for i in range(n - 1, -1, -1):  # Start from the least significant digit
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # Carry over
        
        # If we're here, all digits were 9 (e.g., 999 → 1000)
        return [1] + digits  # Or [1] + [0] * n
