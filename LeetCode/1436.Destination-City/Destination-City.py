class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        t = {}
        c = set() 
        for src, dst in paths:
            t[src] = dst
            c.add(src)
            c.add(dst)
        for city in c:
            if city not in t:
                return city
        return ""
        
