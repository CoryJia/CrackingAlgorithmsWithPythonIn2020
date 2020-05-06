from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums is None or len(nums) == 0: return []

        res = list()
        res.append([])


        for n in nums:
            size = len(res)
            for i in range(size):
                one = list(res[i])
                one.append(n)
                res.append(one)

        return res


if __name__ == '__main__':
    subsets = Solution().subsets([1, 2, 3])
    print(subsets)
