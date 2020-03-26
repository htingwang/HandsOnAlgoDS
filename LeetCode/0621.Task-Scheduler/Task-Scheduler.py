class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        exists = {};
        total = len(tasks);
        for task in tasks:
            exists[task] = exists.get(task, 0) + 1;
        exists = sorted(exists.values(), reverse=True)
        #print exists
        idleslots = (exists[0]-1) * n;
        for i in range(1, len(exists)):
            idleslots -= min(exists[0]-1, exists[i]);
        return max(total, total + idleslots);
            
            
            
        
