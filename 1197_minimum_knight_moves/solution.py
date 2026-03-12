class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        q = deque()
        q.append((0, 0))

        visited = set()
        visited.add((0, 0))

        turns = 0
        while q:
            for _ in range(len(q)):
                cr, cc = q.popleft()
                if x == cr and y == cc:
                    return turns

                for mr, mc in moves:
                    nr, nc = cr + mr, cc + mc
                    if (nr, nc) in visited:
                        continue

                    q.append((nr, nc))
                    visited.add((nr, nc))
            turns += 1

        return -1
