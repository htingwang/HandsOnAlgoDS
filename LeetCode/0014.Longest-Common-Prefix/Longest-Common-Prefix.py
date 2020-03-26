class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs, key=len)
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]

        prefix = ''
        for index, char in enumerate(strs[0]):
            for compare_word in (strs[1:]):
                is_match = True
                if char != compare_word[index]:
                    is_match = False
                    break
            if is_match:
                prefix += char
            else:
                break
        return prefix
