class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        pos = []
        ans = []
        for i in range(len(S)):
            if S[i] == C:
                pos.append(i)
        left = -1
        right = 0
        #print pos
        for i in range(len(S)):
            if S[i] == C:
                ans.append(0)
            else:
                #print left, right, i, pos[right]
                if left == -1 and i < pos[right]:
                    ans.append(pos[right] - i)
                elif right < len(pos) and pos[left] < i < pos[right]:
                    ans.append(min(i - pos[left], pos[right] - i))
                else:
                    while right < len(pos) and i  > pos[right]:
                        left += 1
                        right += 1
                    if right < len(pos):
                        ans.append(min(i - pos[left], pos[right] - i))
                    else:
                        ans.append(i - pos[left])
                
        return ans       
                
