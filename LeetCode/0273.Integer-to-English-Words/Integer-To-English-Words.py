class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        ones = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        one_tens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tris = ["Hundred", "Thousand", "Million", "Billion"]
        res = []
        nums = [int(x) for x in str(num)]
        n = len(nums)
        for i in range(n):
            j = n - 1 - i
            if j % 3 != 1 and 1 <= nums[i] <= 9:
                if i == 0 or j % 3 != 0 or nums[i - 1] != 1:
                    res.append(ones[nums[i] - 1])
            if j % 3 == 0 and j // 3 and res[-1] not in set(tris[1:]): 
                res.append(tris[j // 3])
            if j % 3 == 1:
                if 2 <= nums[i] <= 9:
                    res.append(tens[nums[i] - 1])
                if nums[i] == 1:
                    res.append(one_tens[nums[i + 1]])
            if j % 3 == 2:
                if 1 <= nums[i] <= 9:
                    res.append(tris[0])

        return " ".join(res)
