from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        :param nums: [3,2,2,3]
        :param val: 3
        :return: 2

        after removing val(3): [2,2,3,3]
        """

        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return i

if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3

    print(Solution().removeElement(nums,3))
