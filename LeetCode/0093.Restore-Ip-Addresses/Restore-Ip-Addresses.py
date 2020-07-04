class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # Input: "010010"
        # Ouput: ["0.1.0.010","0.1.00.10","0.1.001.0","0.10.0.10","0.10.01.0","0.100.1.0","01.0.0.10","01.0.01.0","01.00.1.0","010.0.1.0"]
        # Expected: ["0.10.0.10","0.100.1.0"]
        res = []
        cur = []
        def dfs(s, cur, res):
            if len(cur) == 4:
                if not s: res.append(".".join(cur))
                return
            
            for i in range(3):
                if i < len(s) and int(s[: i + 1]) < 256:
                    cur.append(s[: i + 1])
                    dfs(s[i + 1 : ], cur, res)
                    cur.pop()    
                    if s[0] == "0": break
            
        dfs(s, cur, res)
        return res
        
