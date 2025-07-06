class Solution:
    def minSwaps(self, data: list[int]) -> int:
        total_ones = data.count(1)

        if total_ones == 0 or total_ones == 1 or total_ones == len(data):
            return 0

        # ones_count in the window size (all ones in one place)
        # find the window of ones_count size which has number of one
        #
        # 1st window count size
        ones_in_win = sum(data[:total_ones])
        max_ones_win = ones_in_win
        win_size = total_ones

        # slide the fixed window to right and get count on 1s in each window
        # update the max
        for i in range(total_ones, len(data)):
            ones_in_win = ones_in_win + data[i] - data[i - win_size]
            max_ones_win = max(max_ones_win, ones_in_win)

        return total_ones - max_ones_win
