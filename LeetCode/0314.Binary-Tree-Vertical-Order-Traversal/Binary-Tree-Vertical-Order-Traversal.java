/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public List<List<Integer>> verticalOrder(TreeNode root) {
        int min = 0;
        int max = 0;
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        Queue<TreeNode> queue = new LinkedList<>();
        Queue<Integer> col = new LinkedList<>();
        List<List<Integer>> res = new ArrayList<>();
        if(root == null) return res;
        queue.offer(root);
        col.offer(0);
        while(!queue.isEmpty()){
            TreeNode cur = queue.poll();
            int colNum = col.poll();
            if(!map.containsKey(colNum)){
                map.put(colNum, new ArrayList<>());
            }
            map.get(colNum).add(cur.val);
            if(cur.left != null){
                queue.offer(cur.left);
                col.offer(colNum - 1);
                min = Math.min(min, colNum - 1);
            }
            if(cur.right != null){
                queue.offer(cur.right);
                col.offer(colNum + 1);
                max = Math.max(max, colNum + 1);
            }
        }
        for(int i = min; i <= max; i++){
            res.add(map.get(i));
        }
        return res;
    }
}
