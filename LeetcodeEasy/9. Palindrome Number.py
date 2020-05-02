

class Solution:
    def isPalindrome1(self, x : int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        else:
            revnum = 0

            while revnum < x:
                revnum = revnum * 10 + x % 10
                x = x // 10

            return (x == revnum) or (x == revnum // 10) #case 12321, revnum = 123, x = 12

    def isPalindrome2(self, x: int) -> bool:
        if x < 0:
            return False
        return str(x) == str(x)[::-1]

if __name__ == "__main__":
    nums = [121, -121, 10, 12321]

    s = Solution()

    for n in nums:
        print('input %d' %n, 'is palindrome: ', s.isPalindrome2(n))