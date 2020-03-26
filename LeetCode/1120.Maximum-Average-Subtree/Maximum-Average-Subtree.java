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
    class ResultType{
        public int sum, size;
        ResultType (int sum, int size){
            this.sum = sum;
            this.size = size;
        }
    }
    private TreeNode subtree;
    private ResultType subtreeResult;
    public double maximumAverageSubtree(TreeNode root) {
         subtree = null;
        subtreeResult = null;
        helper(root);
        return (double) subtreeResult.sum / subtreeResult.size;
    }
    public ResultType helper(TreeNode root){
        if(root == null){
            return new ResultType(0, 0);
        }
        ResultType left = helper(root.left);
        ResultType right = helper(root.right);
        ResultType result = new ResultType(
            left.sum + right.sum + root.val,
            left.size + right.size + 1
            );
        if(subtree == null || subtreeResult.sum * result.size < result.sum * subtreeResult.size){
            subtree = root;
            subtreeResult = result;
        }    
        return result;
    }
}
