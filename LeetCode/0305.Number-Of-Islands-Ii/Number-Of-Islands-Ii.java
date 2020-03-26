class Union{
    private int convert2ID(int x, int y, int m){
        return x*m + y;
    }
    private Map<Integer, Integer> map = new HashMap<>();
    Union(int n, int m){
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                int id = convert2ID(i, j, m);
                map.put(id, id);
            }
        }
    }
    public void union(int id1, int id2){
        int rootId1 = find(id1);
        int rootId2 = find(id2);
        if(rootId1 != rootId2){
            map.put(rootId1, rootId2);
        }
    }
    public int find(int id){
        while(id != map.get(id)){
            id = map.get(id);
        }
        return id;
    }
}
class Solution {
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
 Union un = new Union(n, m);
        int [][]islands = new int [n][m];
        int count = 0;
        List<Integer> ans = new ArrayList<>();
        if(positions == null || positions.length == 0 || positions[0].length == 0) return ans;
        int [] dx = {1, -1, 0,  0};
        int [] dy = {0, 0 , 1, -1};
        for(int i = 0; i < positions.length; i++){
            
            int curX = positions[i][1];
            int curY = positions[i][0];
            if(islands[curX][curY] != 1){
                islands[curX][curY] = 1;
                count++;
                    for(int j = 0; j < 4; j++){
                        int newX = curX + dx[j];
                        int newY = curY + dy[j];
                        if(newX >=0 && newX < n && newY < m && newY >= 0 && islands[newX][newY] == 1){
                            int curID = curX * m + curY;
                            int newID = newX * m + newY;
                            int rootCur = un.find(curID);
                            int rootNew = un.find(newID);
                            if(rootCur != rootNew){
                                count--;
                                un.union(curID, newID);
                            }
                        }
                    }
            }
            ans.add(count);    
        }
        return ans;        
    }
}
