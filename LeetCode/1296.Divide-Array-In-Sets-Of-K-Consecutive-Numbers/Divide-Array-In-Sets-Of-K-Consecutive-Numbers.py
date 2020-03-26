class Solution(object):
    def isPossibleDivide(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if len(nums) % k != 0: return False
        nums.sort()
        count = collections.Counter(nums)
        for x in nums:
            if count[x] > 0:
                for i in range(k):
                    if count[x + i] > 0:
                        count[x + i] -= 1
                    else:
                        return False
        return True
        
        if self.dfs(nums, 0, count, k) == True:
            return True

                
            #print(count)
        return False
    def dfs(self, nums, start, count, k):
        #print(start, count)
        if sum(count.values()) == 0:
            return True
        for i in range(start, len(nums)):
            x = nums[i]
            if count[x] > 0:
                is_valid = True
                count_1 = copy.copy(count)
                for j in range(k):
                    if count_1[x + j] > 0:
                        count_1[x + j] -= 1
                    else:
                        is_valid = False
                        break
                if is_valid:
                    if self.dfs(nums, i + 1, count_1, k) == True:
                        return True
                is_valid = True
                count_2 = copy.copy(count)
                for j in range(k):
                    if count_2[x - j] > 0:
                        count_2[x - j] -= 1
                    else:
                        is_valid = False
                        break
                if is_valid:
                    if self.dfs(nums, i + 1, count_2, k) == True:
                        return True
        return False
                
                    
        
