/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int getTreeDepth(struct TreeNode* root) {
    if (root == NULL) return 0;
    int leftDepth = getTreeDepth(root->left);
    int rightDepth = getTreeDepth(root->right);
    if (leftDepth > rightDepth) return leftDepth+1;
    return rightDepth+1;
}
bool isBalanced(struct TreeNode* root) {
    if (root==NULL) return true;
    //if ((root->left==NULL) ^ (root->right==NULL)) return true;
    int leftDepth = getTreeDepth(root->left);
    int rightDepth = getTreeDepth(root->right);
    if (leftDepth > rightDepth && leftDepth != rightDepth+1) return false;;
    if (rightDepth > leftDepth && rightDepth != leftDepth+1) return false;;
    
    return isBalanced(root->left) & isBalanced(root->right);
}
