from typing import Dict, List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo: Dict[int, int] = {}

        def backtrack(remaining_amount: int) -> int:
            # short circuit
            if remaining_amount in memo:
                return memo[remaining_amount]

            # Base cases:
            # zero coin needed for 0
            if remaining_amount == 0:
                return 0

            # we have no solution.
            if remaining_amount < 0:
                return -1

            min_coins = float("inf")
            for coin in coins:
                res = backtrack(remaining_amount - coin)

                # if we have a solution.
                if res >= 0 and res < min_coins:
                    min_coins = res + 1

            if min_coins != float("inf"):
                memo[remaining_amount] = int(min_coins)
            else:
                memo[remaining_amount] = -1

            return memo[remaining_amount]

        return backtrack(amount)
