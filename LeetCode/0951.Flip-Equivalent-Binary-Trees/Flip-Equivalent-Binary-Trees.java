// 1. BFS 
// 2. if root1.left == root2.right && root1.right == root2.left 
class Solution {
    public boolean flipEquiv(TreeNode root1, TreeNode root2) {
        Queue<TreeNode> queue = new LinkedList<>();
        queue.offer(root1);
        queue.offer(root2);
        while(!queue.isEmpty()){
              TreeNode cur1 = queue.poll();
              TreeNode cur2 = queue.poll();
              if(cur1 == null && cur2 == null) continue;
              if(!isEqual(cur1, cur2)) return false;
              //if(//no swap)
             if(isEqual(cur1.left, cur2.left) && isEqual(cur1.right, cur2.right)) {
                      queue.offer(cur1.left);
                      queue.offer(cur2.left);
                      queue.offer(cur1.right);
                      queue.offer(cur2.right);
              }
              //else if(//needs to swap)
              else if(isEqual(cur1.right, cur2.left) && isEqual(cur1.left, cur2.right)) {
                      queue.offer(cur1.left);
                      queue.offer(cur2.right);
                      queue.offer(cur1.right);
                      queue.offer(cur2.left);
              }
              else{
                    return false;
              }
        }
        return true;
    }
    public boolean isEqual(TreeNode root1, TreeNode root2){
         if(root1 == null && root2 == null){
                 return true;
         }
         else if(root1 != null && root2 != null && root1.val == root2.val){
                 return true;
         }
         else{
                return false;
         }

    }
}

