public class Solution {
    /**
     * @param costs: n x k cost matrix
     * @return: an integer, the minimum cost to paint all houses
     */
    public int minCostII(int[][] costs) {
        // write your code here
        if(costs == null || costs.length == 0 || costs[0].length == 0) return 0;
        int m = costs.length;
        int n = costs[0].length;
        int [][]f = new int [m + 1][n];
        for(int i = 0; i < n; i++){
            f[0][i] = 0;
        }
        int a = -1;
        int b = -1;
        for(int i = 1; i <= m; i++){
            a = -1;
            b = -1;
            for(int j = 0; j < n; j++){
                if(a == -1 || f[i - 1][j] < f[i - 1][a]){
                    b = a;
                    a = j;
                }
                else{
                    if(b == -1 || f[i - 1][j] < f[i - 1][b]){
                        b = j;
                    }
                }
            }
            if(a == -1) a = 0;
            if(b == -1) b = 0;
            for(int j = 0; j < n; j++){
                if(j != a){
                    f[i][j] = f[i - 1][a] + costs[i - 1][j];
                }else{
                    f[i][j] = f[i - 1][b] + costs[i - 1][j];
                }
            }
        }
        int res = Integer.MAX_VALUE; 
        for(int i = 0; i < n; i++){
            res = Math.min(res, f[m][i]);
        }
        return res;
    }
}
