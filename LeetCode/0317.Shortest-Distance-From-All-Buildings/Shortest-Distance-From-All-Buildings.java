class Solution{
    class Point{
         int x;
         int y;
         public Point(int x,int y){
              this.x = x;
              this.y = y;
          }
    }
    public int shortestDistance(int[][] grid) {
           int m = grid.length;
           int n = grid[0].length;
           int [][] dist = new int [m][n];
           //dist[1][2] = 7
           int [][] num = new int [m][n];
           //num[1][2] = 3
           int totalBuilding = 0;
           for(int i = 0; i < m; i++){
                 for(int j = 0; j < n; j++){
                         if(grid[i][j] == 1){
                               totalBuilding++;
                               bfs(grid, i, j, dist, num);
                          }
                  }
            }
            int res = Integer.MAX_VALUE;
            for(int i = 0; i < m; i++){
                 for(int j = 0; j < n; j++){
                         if(num[i][j] == totalBuilding){
                                 res = Math.min(res, dist[i][j]);
                         }
                 }
             }
            if(res == Integer.MAX_VALUE) return -1;
            else return res;


    }
    public void bfs(int [][]grid, int row, int col, int [][]dist, int [][]num){

          Queue<Point> queue = new LinkedList<>();
          queue.offer(new Point(col, row));
          boolean [][] visited = new boolean[grid.length][grid[0].length];
          visited[row][col] = true;
          int [] dx = {1, -1, 0, 0};
          int [] dy = {0,  0, 1, -1};
          int distance = 0;
          while(!queue.isEmpty()){
                int size = queue.size();
                distance++;
                for(int i = 0; i < size; i++){
                      Point cur = queue.poll();
                      Point newP = new Point(0, 0);
                      for(int j = 0; j < 4; j++){
                            newP.x = cur.x + dx[j];
                            newP.y = cur.y + dy[j];
                            if(newP.x >= 0 && newP.x < grid[0].length && newP.y >= 0 && newP.y < grid.length && !visited[newP.y][newP.x] && grid[newP.y][newP.x] == 0){
                                    dist[newP.y][newP.x] += distance;
                                    visited[newP.y][newP.x] = true;
                                    num[newP.y][newP.x] ++;
                                    queue.offer(new Point(newP.x, newP.y));
                             }
                      }
                }
                
          }
     }
}

