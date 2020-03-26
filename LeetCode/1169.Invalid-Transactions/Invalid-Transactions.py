class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        res = set()
        transactions.sort(key = lambda x:(x.split(",")[0],int(x.split(",")[1])))
        #print(transactions)
        anchor = 0
        for i in range(len(transactions)):
            name, time, amount, city = transactions[i].split(",")
            #print(amount)
            if int(amount) > 1000: res.add(transactions[i])
            #if i > 0:
            pname, ptime, pamount, pcity = transactions[anchor].split(",")
            if name != pname: anchor = i
            while anchor < i and int(time) - int(ptime) > 60:
                anchor += 1
                pname, ptime, pamount, pcity = transactions[anchor].split(",")
            #print(name, pname, city, pcity, time, ptime,int(time) - int(ptime))
            left = anchor
            while left < i:
                if name == pname and city != pcity:
                    res.add(transactions[left])
                    res.add(transactions[i])
                left += 1
                pname, ptime, pamount, pcity = transactions[left].split(",")
                        
        #print(len(res))
        return list(res)
