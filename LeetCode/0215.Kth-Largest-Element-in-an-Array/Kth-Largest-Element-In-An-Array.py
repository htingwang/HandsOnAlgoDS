class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Kth Largets: reverse sort: from big to small
        def quickSelect(nums, start, end, k):
            #print start, end, k
            #print start, k
            if start >= end: return
            middle = (start + end) / 2;
            pivot = nums[middle];
            left, right = start, end;
            while left <= right:
                while nums[left] > pivot and left <= right:
                    left += 1;
                while nums[right] < pivot and left <= right:
                    right -= 1;
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left];
                    left += 1;
                    right -= 1;
            #print nums
            #print left, right
            if start + k - 1 >= left:
                return quickSelect(nums, left, end, k - (left - start));
            if start + k - 1 <= right:
                return quickSelect(nums, start, right, k);
            return
        quickSelect(nums, 0, len(nums) - 1, k);
        return nums[k - 1]
