/**
 * Definition of TreeNode:
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left, right;
 *     public TreeNode(int val) {
 *         this.val = val;
 *         this.left = this.right = null;
 *     }
 * }
 */

public class Solution {
    /**
     * @param root: The root of binary tree.
     * @return: An integer
     */
    public int res; 
    public int maxPathSum(TreeNode root) {
        // write your code here
        if(root == null )return 0;
        res = Integer.MIN_VALUE;
        helper(root);
        return res;
    }
    public int helper(TreeNode root){
        if(root == null) return 0;
        int left = Math.max(0, helper(root.left));
        int right = Math.max(0, helper(root.right));
        
        res = Math.max(res, left + right + root.val);
        return Math.max(left, right) + root.val;
    }
}
