class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        counter = {}
        for cpdomain in cpdomains:
            cur_count, domain = cpdomain.split(" ")
            counter[domain] = counter.get(domain, 0) + int(cur_count)
            dot_pos = domain.find(".")
            while dot_pos != -1:
                #domain = domain[dot_pos + 1:]
                #print domain, dot_pos
                counter[domain[dot_pos + 1:]] = counter.get(domain[dot_pos + 1:], 0) + int(cur_count)
                tmp = domain[dot_pos + 1:].find(".")
                #print tmp
                if tmp < 0: break
                dot_pos += tmp + 1
        #print counter   
        ans = []
        for domain in counter:
            string = str(counter[domain])
            string += " "+domain
            ans.append(string)
        return ans
            
        
