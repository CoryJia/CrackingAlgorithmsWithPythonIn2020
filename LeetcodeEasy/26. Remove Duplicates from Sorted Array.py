from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2: return len(nums)

        j = 0

        for n in nums[1:]:
            if n != nums[j]:
                j += 1
                nums[j] = n

        print(nums)
        return j + 1


if __name__ == "__main__":
    l = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]

    for nums in l:
        print(Solution().removeDuplicates(nums))
