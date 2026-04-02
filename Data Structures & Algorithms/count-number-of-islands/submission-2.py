class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        
        def dfs(r, c):
            #check if we are out of bounds or if the current square we are on is water(0); if yes return
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == "0"):
                return 
        
            # We are on an island(1) so we need to mark it as seen by setting it to 0 and then dfs in all directions from there
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)


        for r in range(ROWS):
            for c in range(COLS):
                # If we found an island we dfs in all directions from there
                if grid[r][c] == "1":
                    dfs(r, c)
                    # add to to the total number of islands
                    islands += 1 
        return islands 