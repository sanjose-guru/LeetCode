#!/usr/bin/env python3


class MyCalendar:
    def __init__(self):
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        if len(self.events) == 0:
            self.events.append([startTime, endTime])
            return True

        idx = self._insertBefore(startTime)

        # previous event time end overlaps.
        # if idx is 0, idx-1 will throw error.
        if idx > 0 and self.events[idx - 1][1] > startTime:
            return False

        # if our end overlaps with next.
        # idx can be len of events, if it was never update, so check
        if idx < len(self.events) and endTime > self.events[idx][0]:
            return False

        self.events.insert(idx, [startTime, endTime])
        return True

    def _insertBefore(self, start: int) -> int:
        lh, rh, res = 0, len(self.events) - 1, len(self.events)
        while lh <= rh:
            mid = (lh + rh) // 2
            if start < self.events[mid][0]:
                res = mid
                rh = mid - 1
            else:
                lh = mid + 1
        return res
