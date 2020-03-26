class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def is_valid(s):
            cnt = 0
            for c in s:
                if c == "(": cnt += 1
                if c == ")":
                    if cnt <= 0: return False
                    cnt -= 1
            return cnt == 0
        
        def bfs(s):
            visited = set([s])
            queue = collections.deque([s])
            found = False
            ans = []
            while queue:
                cur = queue.popleft()
                #print cur
                if is_valid(cur):
                    ans.append(cur)
                    found = True
                if found == True:
                    continue
                for i in range(len(cur)):
                    if cur[i] != "(" and cur[i] != ")":
                        continue
                    new = cur[:i] + cur[i + 1:]
                    #print new, visited
                    if new not in visited:
                        queue.append(new)
                        visited.add(new)
            return ans
        
        def dfs(s, start, left, right, ans):
            if left == 0 and right == 0 and is_valid(s):
                ans.append(s)
                return
            for i in range(start, len(s)):
                if i > start and s[i] == s[i - 1]: continue
                if left > 0 and s[i] == "(":
                    dfs(s[:i] + s[i + 1:], i, left - 1, right, ans)
                if right > 0 and s[i] == ")":
                    dfs(s[:i] + s[i + 1:], i, left, right - 1, ans)
        #return bfs(s)
        left = right = 0
        for c in s:
            if c == "(": left += 1
            if c == ")":
                if left: left -= 1
                else: right += 1
        ans = []
        dfs(s, 0, left, right, ans)
        return ans
    
        #return bfs(s)
