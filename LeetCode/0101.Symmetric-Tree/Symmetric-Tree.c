/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
bool isTwoTreeSymmetric(struct TreeNode* a, struct TreeNode* b) {
    if (a==NULL && b==NULL) return true;
    if (a==NULL || b==NULL) return false;
    if (a->val == b->val) {
        return isTwoTreeSymmetric(a->left, b->right) && isTwoTreeSymmetric(a->right, b->left);
    }
    return false;
}
bool isSymmetric(struct TreeNode* root) {
    if (root) return  isTwoTreeSymmetric(root->left, root->right);
    return true;
}
