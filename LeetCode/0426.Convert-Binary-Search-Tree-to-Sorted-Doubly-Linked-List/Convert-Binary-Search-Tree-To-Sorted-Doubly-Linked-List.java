/*
// Definition for a Node.
class Node {
    public int val;
    public Node left;
    public Node right;

    public Node() {}

    public Node(int _val,Node _left,Node _right) {
        val = _val;
        left = _left;
        right = _right;
    }
};
*/
class Solution {
    public Node treeToDoublyList(Node root) {
        if(root == null) return root;
        Node dummy = new Node(0, null, null);
        Node pre = dummy;
        Stack<Node> stack = new Stack<>();
        Node cur = root;
        while(cur != null || !stack.isEmpty()){
            while(cur != null){
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            pre.right = cur;
            cur.left = pre;
            pre = cur;
            cur = cur.right;
        }
        pre.right = dummy.right;
        dummy.right.left = pre;
        return dummy.right;
    }
}
