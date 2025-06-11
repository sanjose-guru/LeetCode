#!/usr/bin/env python3


class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        res = []
        candles = []

        # Find the candle locations.
        for i, c in enumerate(s):
            if c == "|":
                candles.append(i)

        for l_edge, r_edge in queries:
            # left and right most candles to the query edges.
            l_candle, r_candle = -1, -1

            # find left most candle from left edge.
            lp, rp = 0, len(candles) - 1
            while lp <= rp:
                mid = (lp + rp) // 2
                if candles[mid] >= l_edge:
                    l_candle = mid
                    rp = mid - 1
                else:
                    lp = mid + 1

            # find the right most candle from right edge.
            lp, rp = 0, len(candles) - 1
            while lp <= rp:
                mid = (lp + rp) // 2
                if candles[mid] <= r_edge:
                    r_candle = mid
                    lp = mid + 1
                else:
                    rp = mid - 1

            if l_candle == -1 or r_candle == -1 or l_candle > r_candle:
                res.append(0)
            else:
                res.append(
                    (candles[r_candle] - candles[l_candle]) - (r_candle - l_candle)
                )

        return res

    def platesBetweenCandlesOptimized(
        self, s: str, queries: list[list[int]]
    ) -> list[int]:
        s_len = len(s)
        plate_c = [0] * (s_len + 1)  # Number of plates seen so far at each index
        l_candle = [-1] * s_len  # closets candle to left for each index
        r_candle = [-1] * s_len  # closets candle to right for each index
        lc, rc = -1, -1

        # Build prefix plate counts (sum) and nearest candle in one pass
        for i in range(len(s)):
            # Number of plates seen so far (prefix sum)
            plate_c[i + 1] = plate_c[i] + (1 if s[i] == "*" else 0)

            # Nearest candle to left
            if s[i] == "|":
                lc = i
            l_candle[i] = lc

            # Nearest candle to right
            ri = s_len - i - 1
            if s[ri] == "|":
                rc = ri
            r_candle[ri] = rc

        # print(f"s:{s}\npc:{plate_c}\nlc:{l_candle}\nrc:{r_candle}")
        res = []
        for le, re in queries:
            # for left edge find the candle to right, for right edge find to left
            lc, rc = r_candle[le], l_candle[re]
            if lc != -1 and rc != -1 and lc < rc:
                res.append(plate_c[rc] - plate_c[lc])
            else:
                res.append(0)

        return res


if __name__ == "__main__":
    s = Solution()
    print(s.platesBetweenCandles("**|**|***|", [[2, 5], [5, 9]]))
    print(s.platesBetweenCandlesOptimized("**|**|***|", [[2, 5], [5, 9]]))
    print(
        s.platesBetweenCandles(
            "***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
        )
    )
    print(
        s.platesBetweenCandlesOptimized(
            "***|**|*****|**||**|*", [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
        )
    )
