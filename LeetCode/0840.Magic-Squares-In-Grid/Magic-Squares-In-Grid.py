class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0;
        for row in range(len(grid)-2):
            checkcol = 0;
            checksum = 0;
            for col in range(len(grid[0])-1):
                # check col
                checksum = grid[row][col]+grid[row+1][col]+grid[row+2][col];
                #print([row, col, checksum])
                if (checksum == (grid[row][col+1]+grid[row+1][col+1]+grid[row+2][col+1])):
                    checkcol += 1;
                else:
                    checkcol = 0;
                if checkcol >= 2:
                    #print(checkcol)
                    #print(grid[row][col-1]+grid[row][col]+grid[row][col+1])
                    #print(grid[row+1][col-1]+grid[row+1][col]+grid[row+1][col+1])
                    #print(grid[row+2][col-1]+grid[row+2][col]+grid[row+2][col+1])
                    #print(grid[row][col-1]+grid[row+1][col]+grid[row+2][col+1])
                    #print(grid[row][col+1]+grid[row+1][col]+grid[row+1][col-1])
                    grid00 = grid[row][col-1];
                    grid01 = grid[row][col];
                    grid02 = grid[row][col+1];
                    grid10 = grid[row+1][col-1];
                    grid11 = grid[row+1][col];
                    grid12 = grid[row+1][col+1];
                    grid20 = grid[row+2][col-1];
                    grid21 = grid[row+2][col];
                    grid22 = grid[row+2][col+1];
                    if (grid00 + grid01 + grid02 == grid10 + grid11 + grid12 == grid20 + grid21 + grid22 == grid00 + grid11 + grid22 == grid02 + grid11 + grid20 == checksum and sorted([grid00, grid01, grid02, grid10, grid11, grid12, grid20, grid21, grid22]) == range(1, 10)):
                        ans += 1;
        return ans;
                    
                
