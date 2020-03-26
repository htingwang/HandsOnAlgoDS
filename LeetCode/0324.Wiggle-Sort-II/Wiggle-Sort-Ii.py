class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        median = self.find_kth_smallest(nums, 0, n - 1, (n - 1) // 2)
        
        def mapping(i):
            mid = (n + 1) // 2
            if i < mid :
                return n - i * 2 - 1 - (n + 1) % 2
            return n - (i % mid) * 2 - 1 - n % 2
        
        left, i, right = 0, 0, n - 1
        while i <= right:
            if nums[mapping(i)] > median:
                nums[mapping(i)], nums[mapping(right)] = nums[mapping(right)], nums[mapping(i)]
                right -= 1
            elif nums[mapping(i)] < median:
                nums[mapping(i)], nums[mapping(left)] = nums[mapping(left)], nums[mapping(i)]
                left += 1
                i += 1
            else:
                i += 1
        
    def find_kth_smallest(self, nums, start, end, k):
        mid = nums[(start + end) // 2]
        left, right = start, end
        while left <= right:
            while left <= right and nums[left] < mid:
                left += 1
            while left <= right and nums[right] > mid:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            
        if k <= right:
            return self.find_kth_smallest(nums, start, right, k)
        elif k >= left:
            return self.find_kth_smallest(nums, left, end, k)
        return nums[k]
