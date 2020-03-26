class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        word_to_idx = {}
        for i, word in enumerate(words):
            word_to_idx[word] = i
        
        res = []
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                left = word[: j]
                right = word[j : ]
                left_rev = left[:: - 1]
                right_rev = right[:: -1]
                if left_rev in word_to_idx and word_to_idx[left_rev] != i and self.is_valid(right):
                    res.append([i, word_to_idx[left_rev]])
                    #print(i, j, [i, word_to_idx[left_rev]])
                if len(left) > 0 and right_rev in word_to_idx and word_to_idx[right_rev] != i and self.is_valid(left):
                    res.append([word_to_idx[right_rev], i])
                    #print(i, j, [word_to_idx[right_rev], i])
        return res
    
    def is_valid(self, words):
        for i in range(len(words) // 2):
            if words[i] != words[-i - 1]:
                return False
        return True
        
