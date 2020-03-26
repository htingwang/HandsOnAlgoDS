class Solution(object):
    def findAndReplacePattern(self, words, patterns):
        res = []
        for word in words:
            w2p = {}
            p2w = {}
            is_valid = True
            for i, w in enumerate(word):
                p = patterns[i]
                if w in w2p and w2p[w] != p:
                    is_valid = False
                    break
                if p in p2w and p2w[p] != w:
                    is_valid = False
                    break
                w2p[w] = p
                p2w[p] = w
            if is_valid == True:
                res.append(word)
        return res

