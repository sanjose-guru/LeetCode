class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boat, l, r = 0, 0, len(people) - 1

        # We have to account for the last one person <=
        while l <= r:
            # if we can fit both lite and heavy person in one boat
            # else we will send only the heavy person.
            if people[l] + people[r] <= limit:
                l += 1
            r -= 1
            boat += 1
        return boat
