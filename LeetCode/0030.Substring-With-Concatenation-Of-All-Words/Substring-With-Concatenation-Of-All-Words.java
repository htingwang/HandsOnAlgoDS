class Solution {
    public List<Integer> findSubstring(String s, String[] words) {
         Map<String, Integer> string_to_freq = new HashMap<>();
         if(s == null || s.length() == 0 || words.length == 0 || words == null){
               return new ArrayList<>();
         }
         int m = words.length;
         int n = words[0].length();
         for(String word: words){
             string_to_freq.put(word, string_to_freq.getOrDefault(word, 0) + 1);
         }
         List<Integer> res = new ArrayList<>();
         for(int i = 0; i <= s.length() - m * n; i++){
              int k = m;
              Map<String, Integer> copy = new HashMap<>(string_to_freq);
              int j = i;
              while(k > 0){
                    String cur = s.substring(j, j + n);
                    if(!copy.containsKey(cur) || copy.get(cur) < 1){
                         break;
                    }
                    j = j + n;
                    k = k -1;
                    copy.put(cur, copy.get(cur) - 1);
              }
              if(k == 0){
                  res.add(i);
              }
         } 
         return res;
    }
}

