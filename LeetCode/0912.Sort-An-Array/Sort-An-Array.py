class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #return sorted(nums)
        quick = False;
        def quickSort(nums, start, end):
            if end <= start: return;
            middle = (start + end) / 2;
            pivot = nums[middle];
            left, right = start, end;
            while left <= right:
                #print left, right, nums[left], nums[right], pivot
                while nums[left] < pivot and left <= right:
                    left += 1;
                while nums[right] > pivot and left <= right:
                    right -= 1;
                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left];
                    #print nums
                    left += 1;
                    right -= 1;
            #print nums
            quickSort(nums, start, right);
            quickSort(nums, left, end);

        def merge(nums, start, end, tmp):
            middle = (start + end) / 2;
            i, j, k = start, middle + 1, start;
            #print start, end
            while (i <= middle or j <= end):
                #print i, j, k
                if (j > end) or (i <= middle and nums[i] < nums[j]):
                    tmp[k] = nums[i];
                    i += 1;
                else:
                    tmp[k] = nums[j];
                    j += 1;
                k += 1;
            for i in range(start, end + 1):
                nums[i] = tmp[i];
            #print nums
            
        def mergeSort(nums, start, end, tmp):
            if start >= end: return;
            mergeSort(nums, start, (start + end) / 2, tmp);
            mergeSort(nums, (start + end) / 2 + 1, end, tmp);
            merge(nums, start, end, tmp);
        
        if quick: # Quick Sort
            quickSort(nums, 0, len(nums) - 1);
            return nums;
        else: # Merge Sort
            tmp = [0] * len(nums);
            mergeSort(nums, 0, len(nums) - 1, tmp);
            return nums;
        
