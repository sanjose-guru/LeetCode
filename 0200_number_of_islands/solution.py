class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        lr = len(grid)
        lc = len(grid[0])

        def get_neighbours(r, c: int) -> List[List[int]]:
            neighbours = []
            nrc = [0, 1, 0, -1]
            ncc = [-1, 0, 1, 0]

            for i in range(4):
                nr = r + nrc[i]
                nc = c + ncc[i]

                if 0 <= nr < lr and 0 <= nc < lc:
                    neighbours.append((nr, nc))
            return neighbours

        visited = set()
        num_islands = 0
        q = deque()

        for r in range(lr):
            for c in range(lc):
                if (r, c) in visited or grid[r][c] == "0":
                    continue

                q.append((r, c))
                visited.add((r, c))
                num_islands += 1

                while q:
                    cr, cc = q.popleft()
                    for nr, nc in get_neighbours(cr, cc):
                        if (nr, nc) in visited or grid[nr][nc] == "0":
                            continue
                        visited.add((nr, nc))
                        q.append((nr, nc))

        return num_islands
