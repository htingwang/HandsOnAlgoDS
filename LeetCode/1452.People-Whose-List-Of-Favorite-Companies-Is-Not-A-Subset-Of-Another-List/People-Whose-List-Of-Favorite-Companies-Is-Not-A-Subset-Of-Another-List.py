class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        cid = {}
        k = 0
        companyIds = []
        for i in range(len(favoriteCompanies)):
            cur = []
            for j in range(len(favoriteCompanies[i])):
                if favoriteCompanies[i][j] not in cid:
                    cid[favoriteCompanies[i][j]] = str(k)
                    k += 1
                cur.append(cid[favoriteCompanies[i][j]])
            companyIds.append(set(cur))
        #print(companyIds)
        res = []
        for i in range(len(companyIds)):
            is_sub = False
            for j in range(len(companyIds)):
                if i != j:
                    if companyIds[i].issubset(companyIds[j]): #s.issubset(t) s <= t
                        is_sub = True
                        break
            if not is_sub: res.append(i)
        return res
