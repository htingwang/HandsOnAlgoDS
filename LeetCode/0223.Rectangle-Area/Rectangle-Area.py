class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        left = max(A, E)
        right = max(left, min(C, G))
        bottom = max(B, F)
        top = max(bottom, min(D, H))

        return (C - A) * (D - B) + (G - E) * (H - F) - (right - left) * (top - bottom)
