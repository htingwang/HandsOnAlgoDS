class Solution {
    public int search(ArrayReader reader, int target) {
int index = 0;
        while(reader.get(index) <= target){
            index = index * 2 + 1;
        }
        int start = 0;
        int end = index;
        int mid;
        while(start + 1 < end){
            mid = start + (end - start) / 2;
            if(reader.get(mid) == target){
                end = mid;
            }
            else if(reader.get(mid) < target){
                start = mid;
            }
            else{
                end = mid;
            }
        }
        if(reader.get(start) == target){
            return start;
        }
        else if(reader.get(end) == target){
            return end;
        }
        return -1;
    }
}
