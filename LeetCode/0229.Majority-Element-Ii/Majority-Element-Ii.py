class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = b = cnt1 = cnt2 = 0
        res = []
        for num in nums:
            if num == a: cnt1 += 1
            elif num == b: cnt2 += 1
            elif cnt1 == 0:
                a = num
                cnt1 += 1
            elif cnt2 == 0:
                b = num
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = cnt2 = 0
        for num in nums:
            if num == a: cnt1 += 1
            elif num == b: cnt2 += 1
        print(a, b, cnt1, cnt2)

        if cnt1 > len(nums) // 3: res.append(a)
        if cnt2 > len(nums) // 3: res.append(b)
        return res
