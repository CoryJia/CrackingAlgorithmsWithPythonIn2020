from typing import List


class Solution:

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        if nums is None or len(nums) <= 1:
            return []

        dict = {}

        for idx, n in enumerate(nums):
            if target - n in dict:
                return [dict[target - n], idx]
            dict[n] = idx


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 14
    res = Solution().twoSum2(nums, target)
    print(res)
