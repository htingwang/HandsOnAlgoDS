class TimeMap {
    class Obj{
        int timestamp;
        String value;
        public Obj(int time, String val){
            this.timestamp = time;
            this.value = val;
        }
    }
    Map<String, List<Obj>> map;
    /** Initialize your data structure here. */
    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if(!map.containsKey(key)){
            map.put(key, new ArrayList<>());
        }
        List<Obj> list = map.get(key);
        list.add(new Obj(timestamp, value));
        map.put(key, list);
    }
    
    public String get(String key, int timestamp) {
        if(!map.containsKey(key)){
            return "";
        }
        String res = bs(map.get(key), timestamp);
        return res;
    }
    public String bs(List<Obj> list, int timestamp){
        int left = 0;
        int right = list.size() - 1;
        while(left + 1 < right){
            int mid = left + (right - left) / 2;
            if(list.get(mid).timestamp == timestamp){
                return list.get(mid).value;
            }
            else if(list.get(mid).timestamp > timestamp){
                right = mid ;
            }
            else{
                left = mid ;
            }
        }
        if(list.get(right).timestamp <= timestamp){
            return list.get(right).value;
        }
        else if(list.get(left).timestamp <= timestamp){
            return list.get(left).value;
        }
        else{
            return "";
        }
        // if(left >= list.size()){
        //     if(right < 0){
        //         return "";
        //     }
        //     else{
        //         return list.get(right).value;
        //     }
        // } 
        // if(list.get(left).timestamp > timestamp && list.get(right).timestamp > timestamp){
        //     return "";
        // }
        // else if (list.get(left).timestamp > timestamp && list.get(right).timestamp < timestamp){
        //     return list.get(right).value;
        // }
        // else if(list.get(left).timestamp < timestamp && list.get(right).timestamp < timestamp){
        //     return list.get(left).value;
        // }
        // else{
        //     return "";
        // }
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */
