class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        li, ri = 0, len(numbers) - 1

        while li < ri:
            s = numbers[li] + numbers[ri]
            if s == target:
                return [li + 1, ri + 1]
            elif s < target:
                li += 1
            else:
                ri -= 1
        return [li, ri]  # should never happen
