class Solution(object):
    def maxFreq(self, s, maxLetters, minSize, maxSize):
        """
        :type s: str
        :type maxLetters: int
        :type minSize: int
        :type maxSize: int
        :rtype: int
        """
        count_1 = collections.defaultdict(int)
        count_2 = []
        for i in range(maxSize - minSize + 1):
            count_2.append(collections.defaultdict(int))
        for i, c in enumerate(s):
            for j in range(maxSize - minSize + 1):
                count_2[j][c] += 1
                if i >= minSize + j - 1:
                    if len(count_2[j]) <= maxLetters:
                        count_1[s[i - minSize - j + 1 : i + 1]] += 1
                    count_2[j][s[i - minSize - j + 1]] -= 1
                    if count_2[j][s[i - minSize - j + 1]] == 0:
                        del count_2[j][s[i - minSize - j + 1]]
            #print(i, count_2[0], count_2[1])
        #print(count_1)
        return max(count_1.values()) if count_1 else 0
                
