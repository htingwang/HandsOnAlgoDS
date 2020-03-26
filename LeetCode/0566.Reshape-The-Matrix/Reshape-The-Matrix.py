class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        o_r, o_c = len(nums), len(nums[0]);
        if (r * c != o_r * o_c): return nums;
        
        ret = [];
        row = [];
        ret_r, ret_c = 0, 0;
        for ir in range(o_r):
            for ic in range(o_c):
                #print(nums[ir][ic])
                #ret[ret_r][ret_c] = nums[ir][ic];
                ret_c += 1;
                row.append(nums[ir][ic]);
                if (ret_c >= c): 
                    ret_c = 0;
                    ret.append(row); 
                    row = [];
          
        return ret;
                
        
        
        
