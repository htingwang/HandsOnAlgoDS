class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        orderdict = collections.defaultdict(dict)
        foodset = set()
        for name, table, food in orders:
            tid = int(table)
            if food in orderdict[tid]: orderdict[tid][food] += 1
            else: orderdict[tid][food] = 1
            foodset.add(food)
        firstrow = ["Table"]
        foodlist = sorted(foodset)
        f2idx = {}
        for i, food in enumerate(foodlist): 
            firstrow.append(food)
            f2idx[food] = i
        res = [firstrow]
        #print(orderdict)
        #print(sorted(orderdict.keys()))
        #print(foodset)
        for tid in sorted(orderdict.keys()):
            row = [str(tid)] + [0] * len(foodset)
            for i in range(1, len(foodset) + 1):
                food  = res[0][i]
                if food in orderdict[tid]: row[f2idx[food] + 1] = str(orderdict[tid][food])
                else: row[f2idx[food] + 1] = "0"
            res.append(row)
        return res
        
        
