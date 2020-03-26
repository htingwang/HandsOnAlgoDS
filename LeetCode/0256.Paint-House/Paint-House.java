class Solution {
    public int minCost(int[][] costs) {
        if(costs == null || costs.length == 0 || costs[0].length == 0) return 0;
        for(int i = 1; i < costs.length; i++){
            costs[i][0] += Math.min(costs[i - 1][1], costs[i - 1][2]);
            costs[i][1] += Math.min(costs[i - 1][0], costs[i - 1][2]);
            costs[i][2] += Math.min(costs[i - 1][1], costs[i - 1][0]);
        }
        int m = costs.length - 1;
        return Math.min(costs[m][0], Math.min(costs[m][1], costs[m][2]));
    }
}
