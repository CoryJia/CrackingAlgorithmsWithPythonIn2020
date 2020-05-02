class LSolution:
    def reverse(self, x:int) ->int:
        flag = -1 if x < 0 else 1
        n = x * flag

        res = 0

        while n != 0:
            rem = n % 10
            n = n // 10
            res = res * 10 + rem

        res = res * flag

        return 0 if res > (2**31 - 1) or res < -2**31 else res


if __name__ == "__main__":
    nums = [123, -123, 120]

    for x in nums:
        print('input %d' % x, '\treversed is: ', LSolution().reverse(x))