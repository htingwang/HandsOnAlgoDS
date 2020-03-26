class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        total = 0;
        ret = [];
        for i in range(len(A)):
            if (A[i] % 2 == 0): total += A[i];
        print(total)
        for query in queries:
            if (A[query[1]] % 2 == 0): total -= A[query[1]];
            A[query[1]] += query[0];
            if (A[query[1]] % 2 == 0): total += A[query[1]];
            ret.append(total);
        return ret
            
        
