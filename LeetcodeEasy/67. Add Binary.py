class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ''
        carry = 0

        maxLen = max(len(a), len(b))

        a = a.zfill(maxLen)
        b = b.zfill(maxLen)

        for i in range(maxLen - 1, -1, -1):
            sum = int(a[i]) + int(b[i]) + carry

            res += str(sum % 2)
            carry = sum // 2

        if carry:
            res += str(1)

        return res[::-1]
