from collections import deque
class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        old_color = image[sr][sc]
        if old_color == newColor: return image
        
        def dfs(sr, sc):
            image[sr][sc] = newColor
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = sr + dr, sc + dc
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == old_color:
                    dfs(nr, nc)
                    
        dfs(sr, sc)
        return image
