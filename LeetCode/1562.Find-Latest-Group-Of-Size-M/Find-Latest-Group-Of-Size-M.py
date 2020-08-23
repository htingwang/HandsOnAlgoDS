class Solution(object):
    def findLatestStep(self, arr, m):
        """
        :type arr: List[int]
        :type m: int
        :rtype: int
        """
        res = -1
        n = len(arr)
        bucket = [0] * (n + 2)
        count = collections.defaultdict(int)
        for j, i in enumerate(arr):
            if bucket[i - 1] != 0 and bucket[i + 1] != 0:
                count[i - 1 - bucket[i - 1] + 1] -= 1
                count[bucket[i + 1] - (i + 1) + 1] -= 1
                s, e = bucket[i - 1], bucket[i + 1]
                count[e - s + 1] += 1
                bucket[s], bucket[e] = e, s
            elif bucket[i - 1] != 0:
                count[i - 1 - bucket[i - 1] + 1] -= 1
                s, e = bucket[i - 1], i
                count[e - s + 1] += 1
                bucket[s], bucket[e] = e, s
            elif bucket[i + 1] != 0:
                count[bucket[i + 1] - (i + 1) + 1] -= 1
                s, e = i, bucket[i + 1]
                count[e - s + 1] += 1
                bucket[s], bucket[e] = e, s
            else:
                bucket[i] = i
                count[1] += 1
            #print(j, bucket)
            #print(count)
            if count[m] != 0:
                res = j + 1
        return res
                
