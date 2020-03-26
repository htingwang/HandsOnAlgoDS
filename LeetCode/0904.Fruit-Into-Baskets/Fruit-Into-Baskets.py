class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        n = len(tree)
        if n <= 1: return n
        i, j, ans = 0, 1, 0
        x = y = tree[0]
        while i < n and j < n:
            #print(i, j, tree[j], x, y)
            if tree[j] == x or tree[j] == y:
                j += 1
            elif tree[j] != x and x == y:
                y = tree[j]
                j += 1
            else:
                i = j - 1
                while tree[i - 1] == tree[i]:
                    i -= 1
                x, y = tree[i], tree[j]
                #print(i, j, x, y)
            ans = max(ans, j - i)
        #print(i, j)
        return ans
