from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(res, [], n, 1, 0, k)
        return res

    def dfs(self, res, path, n, curVal, curSize, k):
        if curSize == k:
            res.append(list(path))
            return

        if curVal > n or curSize > k: return

        # not add curVal
        self.dfs(res, path, n, curVal + 1, curSize, k)

        # add curVal
        path.append(curVal)
        self.dfs(res, path, n, curVal + 1, curSize + 1, k)
        path.pop()


if __name__ == '__main__':
    print(Solution().combine(4, 2))
