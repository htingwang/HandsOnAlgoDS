class Solution(object):
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        m, n = len(image), len(image[0])
        up = self.bs(image, 0, x, 0, n, True, True)
        down = self.bs(image, x + 1, m, 0, n, True, False)
        left = self.bs(image, 0, y, up, down, False, True)
        right = self.bs(image, y + 1, n, up, down, False, False)
        return (right - left) * (down - up)
        
    def bs(self, image, i, j, low, high, h, opt):
        while i < j:
            mid = (i + j) // 2
            k = low
            if h: 
                while k < high and image[mid][k] == "0": k += 1
            else: 
                while k < high and image[k][mid] == "0": k += 1

            if (k < high) == opt: j = mid
            else: i = mid + 1

        return i
