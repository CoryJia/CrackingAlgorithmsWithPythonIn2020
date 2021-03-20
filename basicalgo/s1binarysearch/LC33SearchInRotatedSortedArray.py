from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1
        if n == 0: return -1

        while left <= right:
            mid = left + (right - left) // 2

            temp = nums[mid]
            if temp == target: return mid

            # inflection point to the right. Left is strictly increasing
            if temp >= nums[left]:
                if nums[left] <= target < temp:
                    right = mid - 1
                else:
                    left = mid + 1
            # inflection point to the left of me. Right is strictly increasing
            else:
                if temp < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1