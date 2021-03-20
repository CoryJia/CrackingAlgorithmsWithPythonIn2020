from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]

        res[0] = self.findStartingIndex(nums, target)
        res[1] = self.findEndingIndex(nums, target)

        return res

    def findStartingIndex(self, nums, target):
        index = -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) / 2

            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return index

    def findEndingIndex(self, nums, target):
        index = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) / 2

            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid - 1

        return index