from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        queue = collections.deque()
        queue.append(beginWord)      
        wordSet = set(wordList)
        distance = {beginWord: 1}
        ans = 0
        while queue:
            cur = queue.popleft()
            #print(cur)
            d = distance[cur]
            if cur == endWord: return distance[cur] 
            for i in range(len(cur)):
                for char in "abcdefghijklmnopqrstuvwxyz":
                    if char != cur[i]:
                        target = cur[:i] + char + cur[i + 1:]
                        if target in wordSet and target not in distance:
                            queue.append(target)
                            #visited.add(target)
                            #wordSet.remove(target)
                            distance[target] = d + 1
        return 0
