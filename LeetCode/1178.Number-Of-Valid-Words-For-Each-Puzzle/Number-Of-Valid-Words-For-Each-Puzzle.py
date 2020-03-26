class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        """
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        """
        res = []
        wordsmap = collections.defaultdict(int)
        for word in words:
            if len(set(word)) <= 7:
                wordsmap["".join(sorted(set(word)))] += 1
        #print(wordsmap)
        for p in puzzles:
            cur = 0
            for i in range(len(p)):
                for sub in itertools.combinations(p[1 : ], i):
                    #print(p[0])
                    s = p[0] + "".join(sub)
                    #print(s)
                    cur += wordsmap["".join(sorted(s))]
            res.append(cur)
        return res
