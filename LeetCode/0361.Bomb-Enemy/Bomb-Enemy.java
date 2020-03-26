public class Solution {
    /**
     * @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
     * @return: an integer, the maximum enemies you can kill using one bomb
     */
    public int maxKilledEnemies(char[][] grid) {
        // write your code here
        if(grid == null || grid.length == 0 || grid[0].length == 0) return 0;
        int [][] upp = new int [grid.length][grid[0].length];
        int [][] down = new int [grid.length][grid[0].length];
        int [][] left = new int [grid.length][grid[0].length];
        int [][] right = new int [grid.length][grid[0].length];
        int m = grid.length;
        int n = grid[0].length;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                upp[i][j] = 0;
                if(grid[i][j] == 'W') continue;
                if(grid[i][j] == 'E'){
                    upp[i][j]++;
                }
                if(i > 0){
                    upp[i][j] += upp[i - 1][j];
                }
            }
        }
        //down
        for(int i = m - 1 ; i >= 0; i--){
            for(int j = 0; j < grid[0].length; j++){
                down[i][j] = 0;
                if(grid[i][j] == 'W') continue;
                if(grid[i][j] == 'E'){
                    down[i][j]++;
                }
                if(i < m - 1){
                    down[i][j] += down[i + 1][j];
                }
            }
        }      
      
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                left[i][j] = 0;
                if(grid[i][j] == 'W') continue;
                if(grid[i][j] == 'E'){
                    left[i][j]++;
                }
                if(j > 0){
                    left[i][j] += left[i][j - 1];
                }
            }
        }
        
        for(int i = 0; i < grid.length; i++){
            for(int j = n - 1; j >= 0; j--){
                right[i][j] = 0;
                if(grid[i][j] == 'W') continue;
                if(grid[i][j] == 'E'){
                    right[i][j]++;
                }
                if(j < n - 1){
                    right[i][j] += right[i][j + 1];
                }
            }
        }
        int  res = 0;
        for(int i = 0; i < grid.length; i++){
            for(int j = 0; j < grid[0].length; j++){
                if(grid[i][j] == '0') {
                    res = Math.max(res, upp[i][j] + down[i][j] + left[i][j] + right[i][j]);
                }
            }
        }
        return res;
    }
}
