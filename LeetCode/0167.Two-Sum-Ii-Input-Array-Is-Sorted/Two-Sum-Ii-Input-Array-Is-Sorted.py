class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left,right = 0, len(numbers)-1;
        while (left < right):
            twosum = numbers[left] + numbers[right];
            if (twosum == target): break;
            elif (twosum < target): left += 1;
            else: right -= 1;
        return [left+1, right+1];
        
