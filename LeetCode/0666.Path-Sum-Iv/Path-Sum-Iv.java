class Solution {
    int sum = 0;
    Map<Integer, Integer> map = new HashMap<>();
    public int pathSum(int[] nums) {
        for(int num : nums){
            int key = num / 10;
            int val = num % 10;
            map.put(key, val);
        }
        traverse(nums[0] / 10, 0);
        return sum;
    }
    public void traverse(int key, int pre){
        int level = key / 10;
        int pos = key % 10;
        int left = (level + 1) * 10 + pos * 2 - 1;
        int right = (level + 1) * 10 + pos * 2;
        int curSum = pre + map.get(key);
        if(!map.containsKey(left) && !map.containsKey(right)){
            sum += curSum;
            return;
        }
        if(map.containsKey(left)) traverse(left, curSum);
        if(map.containsKey(right)) traverse(right, curSum);
        
    }
}
