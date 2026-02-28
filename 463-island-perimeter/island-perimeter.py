class Solution:
    def islandPerimeter(self, grid):
        rows = len(grid)
        cols = len(grid[0])
        
        land = 0
        shared = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    land += 1
                    
                    # Check right neighbor
                    if j + 1 < cols and grid[i][j + 1] == 1:
                        shared += 1
                        
                    # Check down neighbor
                    if i + 1 < rows and grid[i + 1][j] == 1:
                        shared += 1
                        
        return 4 * land - 2 * shared