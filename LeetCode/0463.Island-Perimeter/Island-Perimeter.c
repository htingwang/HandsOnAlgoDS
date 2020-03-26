int islandPerimeter(int** grid, int gridRowSize, int gridColSize) {
    int i, j, land=0, common=0;
    for (i=0; i<gridRowSize; i++) {
        for (j=0; j<gridColSize; j++) {
            if (grid[i][j]) {
                land++;
                if (j>0 && grid[i][j]==grid[i][j-1]) common++;
                if (i>0 && grid[i][j]==grid[i-1][j]) common++;
            }
        }
    }
    return land*4-common*2;
}
