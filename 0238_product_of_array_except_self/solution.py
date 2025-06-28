class Solution:
    def productExceptSelf_old(self, nums: List[int]) -> List[int]:
        left_prods, right_prods = [1], [1]
        a_len = len(nums)

        # find product of all left to my left and to my right.
        for i in range(a_len):
            left_prods.append(left_prods[i] * nums[i])
            right_prods.append(right_prods[i] * nums[a_len - i - 1])

        res = []
        for i in range(a_len):
            res.append(left_prods[i] * right_prods[a_len - i - 1])

        return res

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        a_len = len(nums)
        res = [1] * a_len

        # Store product of numbers to left.
        left = 1
        for i in range(a_len):
            res[i] = left  # store left product
            left *= nums[i]

        # multiply it with right side product.
        right = 1
        for i in range(a_len - 1, -1, -1):
            res[i] *= right  # multiple num with already stored left side product
            right *= nums[i]

        return res
