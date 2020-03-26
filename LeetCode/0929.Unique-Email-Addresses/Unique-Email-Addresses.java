class Solution {
    public int numUniqueEmails(String[] emails) {
        Set<String> emailSet = new HashSet();
        for (String email: emails) {
            int i = email.indexOf("@");
            String local = email.substring(0, i);
            String rest = email.substring(i);
            if (local.contains("+")) {
                local = local.substring(0, local.indexOf("+"));
            }
            
            local = local.replace(".", "");
            //System.out.println(local);
            emailSet.add(local + rest);
        }
        //System.out.println(emailSet);
        return emailSet.size();
    }
}
