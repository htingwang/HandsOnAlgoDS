from collections import deque
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = [];
        if not nums or not k: return None;
        if k > len(nums): return None;
        queue = deque([]);
        for i in range(len(nums)):
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop();
            queue.append(i)
            if i >= k - 1:
                ans.append(nums[queue[0]]);
                if queue[0] == i - k + 1:
                    queue.popleft();
        return ans;
            
        
