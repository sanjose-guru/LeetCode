#!/usr/bin/env python3

"""

**Logic**: The solution uses binary search, leveraging the property that before
the single element, pairs start at even indices, and after the single element,
pairs start at odd indices.


All new numbers should start at an even index (since array index starts from 0)

When a non duplicate number comes it will mess up the order and after that
point onwards new number's index will be on odd index.

Do a binary search to find the left half where the index started messing up.
"""


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        lh, rh, res = 0, len(nums) - 1, -1

        while lh <= rh:
            mid = (lh + rh) // 2
            if self._onTheLeft(nums, mid):
                res = mid
                rh = mid - 1
            else:
                lh = mid + 1
        return nums[res]

    def _onTheLeft(self, nums: list[int], idx) -> bool:
        # If the index in last element, the bad number should be to left only.
        if idx == len(nums) - 1:
            return True

        if idx % 2 == 0:
            return nums[idx] != nums[idx + 1]
            # if nums[idx] == nums[idx + 1]:
            #     return False  # starting number if even, so non duplicate is not on left side.
            # else:
            #     return True
        else:
            return nums[idx] == nums[idx + 1]
            # if nums[idx] == nums[idx + 1]:
            #     return True  # start num is not in even index, got messed up, non duplicate is to our left.
            # else:
            #     return False


if __name__ == "__main__":
    sol = Solution()
    print(f"{sol.singleNonDuplicate([1, 1, 2, 3, 3, 4, 4, 8, 8]) == 2}")
    print(f"{sol.singleNonDuplicate([3, 3, 7, 7, 10, 11, 11]) == 10}")

"""
**** Cleaner code ****
def singleNonDuplicate(self, nums: list[int]) -> int:
        lh, rh = 0, len(nums) - 1
        while lh < rh:
            mid = (lh + rh) // 2
            # Ensure mid is even for comparison with next index
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lh = mid + 2
            else:
                rh = mid
        return nums[lh]
"""
