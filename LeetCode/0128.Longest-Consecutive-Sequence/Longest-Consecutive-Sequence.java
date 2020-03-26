class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i: nums){
            set.add(i);
        }
        int res = 0;
        for(int i = 0; i < nums.length; i++){
            if(!set.contains(nums[i])) continue;
            set.remove(nums[i]);
            
            int lower = nums[i] - 1;
            //ex: 4 -> 3
            while(set.contains(lower)){
            //find!!
            set.remove(lower);
            lower = lower - 1;
            }

            int upper = nums[i] + 1;
            //4 of upper is 5
            while(set.contains(upper)){
                //find!!!
                set.remove(upper);
                upper ++;
            }
            //lower = 3, 2, 1 -> 0(invalid)
            //upper = 5(invalid)
            //4, 3, 2, 1 
            res = Math.max(res, upper - lower - 1);
        }
        return res;
    }
}
