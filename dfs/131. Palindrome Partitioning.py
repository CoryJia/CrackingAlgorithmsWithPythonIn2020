from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s is None or len(s) == 0:
            return []

        res = []
        self.dfs(res, s, 0, [])
        return res


    def dfs(self, res, s, idx, path):
        if idx == len(s):
            res.append(list(path))
            return

        for i in range(idx, len(s)):
            if self.isPalindrome(s, idx, i):
                path.append(s[idx:i + 1])
                self.dfs(res, s, i + 1, path)
                path.pop()


    def isPalindrome(slef, s, start, end):
        while start <= end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True


if __name__ == '__main__':
    s = 'aab'
    print(Solution().partition(s))
