from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits)-1, -1, -1):
            digits[i] += 1

            if digits[i] <= 9:
                return digits
            else:
                digits[i] = 0
                carry = 0

        if i == 0 and carry:
            digits.insert(0, 1)
            return digits
