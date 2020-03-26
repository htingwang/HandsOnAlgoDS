class Vector2D {
    int row, col;
    int [][] list;
    public Vector2D(int[][] v) {
        // list = new int [v.length][v[0].length];
        list = v;
        row = 0;
        col = 0;
    }
    
    public int next() {
        update();
        int val = list[row][col];
        col++;
        return val;

    }
    
    public boolean hasNext() {
        update();
        return row != list.length;

    }
    public void update(){
        while(row < list.length && col == list[row].length){
            row++;
            col = 0;
        }
    }
}

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D obj = new Vector2D(v);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */
