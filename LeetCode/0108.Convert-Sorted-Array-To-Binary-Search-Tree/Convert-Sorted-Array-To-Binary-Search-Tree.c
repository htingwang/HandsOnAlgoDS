/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 *           7
 *      3         11
 *    1   5     9     13
 *   0 2 4 6  8  10 12 14
 */
 
struct TreeNode* sortedArrayToBST(int* nums, int numsSize) {
    //return buildTree(nums, 0, numsSize);
    if (numsSize==0) return NULL;
    int mid = numsSize/2;
    struct TreeNode* root = malloc(sizeof(struct TreeNode));
    root->val = nums[mid]; 
    root->left = sortedArrayToBST(nums, mid);
    root->right = sortedArrayToBST(nums+mid+1, numsSize-mid-1);
    return root;
}
