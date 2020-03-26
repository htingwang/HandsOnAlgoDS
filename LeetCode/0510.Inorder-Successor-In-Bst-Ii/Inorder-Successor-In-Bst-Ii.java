/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
};
*/
class Solution {
    public Node inorderSuccessor(Node x) {
        if(x == null) return x;
        if(x.right != null){
            x = x.right;
            while(x.left != null){
                x = x.left;
            }
            return x;
        }
        else{
            while(x.parent != null && x == x.parent.right){
                x = x.parent;
            }
            return x.parent;
        }
    }
}
