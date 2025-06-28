class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix_sum = [0]  # base case

        for i, num in enumerate(nums):
            self.prefix_sum.append(self.prefix_sum[i] + num)
        print(f"{self.prefix_sum}")

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right + 1] - self.prefix_sum[left]
