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
     * @param root: the given BST
     * @param target: the given target
     * @return: the value in the BST that is closest to the target
     */
    public int closestValue(TreeNode root, double target) {
        // write your code here
        if(root == null) return -1;
        TreeNode lower = root;
        TreeNode upper = root;
        while(root != null){
            if(target == root.val){
                return root.val;
            }
            else if(target > root.val){
                lower = root;
                root = root.right;
            }
            else{
                upper = root;
                root = root.left;
            }
        }
        if(Math.abs(upper.val - target) > Math.abs(target - lower.val)){
            return lower.val;
        }else{
            return upper.val;
        }
    }
}
