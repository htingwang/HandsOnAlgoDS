class Solution {
    public int numJewelsInStones(String J, String S) {
        int count = 0;
        Set Jset=new HashSet();
        for (char j:J.toCharArray()) Jset.add(j);
        for (char s:S.toCharArray()) if (Jset.contains(s)) count++;
        return count;
    }
}
