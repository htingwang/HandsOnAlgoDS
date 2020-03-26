/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isLeaf(struct TreeNode* root) {
    return (root->left == NULL) && (root->right == NULL);
}
int minDepth(struct TreeNode* root) {
    if (root == NULL) return 0;
    if (isLeaf(root)) return 1;
    //if ((root->left) && (root->right==NULL) && isLeaf(root->left)) return 2;
    //if ((root->right) && (root->left==NULL) && isLeaf(root->right)) return 2;
    int leftMinDepth = minDepth(root->left);
    int rightMinDepth = minDepth(root->right);
    if (leftMinDepth == 0 ) return rightMinDepth+1;
    if (rightMinDepth == 0 ) return leftMinDepth+1;
    if (leftMinDepth<rightMinDepth) return leftMinDepth+1;
    return rightMinDepth+1;
}
