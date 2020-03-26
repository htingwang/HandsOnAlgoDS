class Solution(object):
    def parseBoolExpr(self, expression):
        """
        :type expression: str
        :rtype: bool
        """
        op = []
        b = []
        ans = False
        for exp in expression:
            if exp == "|" or exp == "&" or exp == "!":
                op.append(exp)
            elif exp == ")":
                #print(op, b)
                t_cnt = f_cnt = 0
                while b and b[-1] != "(":
                    cur_b = b.pop()
                    if cur_b == "t": t_cnt += 1
                    if cur_b == "f": f_cnt += 1
                    
                b.pop()
                cur_op = op.pop()
                if cur_op == "&":
                    if f_cnt > 0: b.append("f")
                    else: b.append("t")
                if cur_op == "|":
                    if t_cnt > 0: b.append("t")
                    else: b.append("f")
                if cur_op == "!":
                    if t_cnt > 0: b.append("f")
                    else: b.append("t")
            else:
                b.append(exp)
        if b[-1] == "t":
            return True
        return False
        
