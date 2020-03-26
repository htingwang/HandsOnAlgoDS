class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        A = list(map(int, list(str(num))))
        pos = {x: i for i, x in enumerate(A)}
        for i, x in enumerate(A):
            for j in range(9, x, -1):
                if pos.get(j, 0) > i:
                    A[i], A[pos[j]] = A[pos[j]], A[i]
                    return int("".join(list(map(str, A))))
        return num
