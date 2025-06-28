#!/usr/bin/env python3


class SnapshotArray:
    def __init__(self, length: int):
        self.array = [[[0, 0]] for _ in range(length)]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.array[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        """
        Use binary search to speed up retrieval. Bi-sect can be used to be more
        efficient.
        """
        lh, rh, res = 0, len(self.array[index]) - 1, 0
        while lh <= rh:
            mid = (lh + rh) // 2
            if self.array[index][mid][0] <= snap_id:
                res = mid
                lh = mid + 1
            else:
                rh = mid - 1
        return self.array[index][res][1]
