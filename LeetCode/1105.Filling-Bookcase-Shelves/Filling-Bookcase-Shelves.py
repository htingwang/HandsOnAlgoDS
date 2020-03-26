import sys
class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        ans = 0
        n = len(books)
        f = [0] * (n + 1)
        #f[1] = books[0][1]
        
        for i in range(1, n + 1):
            j = i
            w = cur_max_h = 0
            min_h = sys.maxsize
            while j > 0:
                w += books[j - 1][0]
                if w <= shelf_width:
                    #print(i, j, books[j - 1])
                    cur_max_h = max(cur_max_h, books[j - 1][1])
                    min_h = min(min_h, f[j - 1] + cur_max_h)
                else: break
                j -= 1
            f[i] = min_h       
        #print(f)
        return f[n]
