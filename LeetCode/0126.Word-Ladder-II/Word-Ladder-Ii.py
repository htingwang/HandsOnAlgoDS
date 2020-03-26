import collections
class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        n = len(beginWord)
        word_set = set(wordList)
        transform = collections.defaultdict(set)
        queue = collections.deque([beginWord])
        while queue:
            cur_transform = collections.defaultdict(set)
            size = len(queue)
            for _ in range(size):
                cur_word = queue.popleft()
                for c in "abcdefghijklmnopqrstuvwxyz":
                    for i in range(n):
                        n_word = cur_word[:i] + c + cur_word[i + 1:]
                        if n_word not in transform and n_word in word_set:
                            cur_transform[n_word].add(cur_word)
                            queue.append(n_word)
            transform.update(cur_transform)
            if endWord in transform:
                break
       
        if endWord not in transform:
            return []
        res = [[endWord]]
        while res[0][0] != beginWord:
            res = [[p] + w for w in res for p in transform[w[0]]]
        return res
