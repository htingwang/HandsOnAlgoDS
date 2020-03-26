class Solution {
    public String alienOrder(String[] words) {
        if(words == null || words.length == 0) return "";
        int []degree = new int[26];
        Map<Character, HashSet<Character>> map = new HashMap<>();
        int count = 0;
        for(String cur: words){
            for(char c: cur.toCharArray()){
                if(degree[c - 'a'] == 0){
                    degree[c - 'a'] = 1;
                    count++;
                }
            }
        }
        for(int i = 0; i < words.length - 1; i++){
            String cur = words[i];
            String next = words[i + 1];
            int len = Math.min(cur.length(), next.length());
            for(int j = 0; j < len; j++){
                if(cur.charAt(j) != next.charAt(j)){
                    
                    if(!map.containsKey(cur.charAt(j))){
                        map.put(cur.charAt(j), new HashSet<Character>());
                    }
                    HashSet<Character> tmp = map.get(cur.charAt(j));
                    tmp.add(next.charAt(j));
                    map.put(cur.charAt(j), tmp);
                    // if(map.get(cur.charAt(j)).add(next.charAt(j))){
                    //     degree[next.charAt(j) - 'a']++;
                    // }
                    break;
                }
            }

        }
            for(char i : map.keySet()){
                for(char neighbor: map.get(i)){
                    degree[neighbor - 'a']++;
                }
            }        
        Queue<Character> queue = new LinkedList<>();
        for(int i = 0; i < 26; i++){
            if(degree[i] == 1){
                queue.offer((char) ('a' + i));
            }
        }
        StringBuilder sb = new StringBuilder();
        while(!queue.isEmpty()){
            char cur = queue.poll();
            sb.append(cur);
            if(map.containsKey(cur)){
                  for(char neighbor: map.get(cur)){
                    degree[neighbor - 'a']--;
                    if(degree[neighbor - 'a'] == 1){
                        queue.offer(neighbor);
                    }
                  }  
            }
            
        }
        if(sb.length() != count){
            return "";
        }
        else{
            return sb.toString();
        }
        
    }
}
