class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1: return x

        l, r = 1, x // 2

        while l + 1 < r:
            mid = (l + r) // 2

            if mid * mid == x:
                return mid
            elif mid * mid > x:
                r = mid - 1
            else:
                l = mid

        return r if r * r <= x else l

if __name__ == '__main__':
    print(Solution().mySqrt(8))
