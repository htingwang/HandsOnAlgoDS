/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
/**
 * Return an array of arrays of size *returnSize.
 * The sizes of the arrays are returned as *columnSizes array.
 * Note: Both returned array and *columnSizes array must be malloced, assume caller calls free().
 */


struct TreeQueue {
    int val;
    int level;
    struct TreeQueue *next;
};

struct QueueNode {
    int val;
    struct QueueNode *next;
};

struct LevelHead {
    int count;
    struct QueueNode* head;
};

struct TreeResult {
    int levelLimit;
    int levelCount;
    struct LevelHead* levelHead;
};

void BuildTree(struct TreeNode* root, struct TreeResult* result, int level) {
    if (root == NULL) return;
    
    if (level > (result->levelLimit-1)) {
        struct LevelHead* newLevel = malloc((level+10)*sizeof(struct LevelHead));
        memset(newLevel, 0, (level+10)*sizeof(struct LevelHead));
        memcpy(newLevel, result->levelHead, (result->levelLimit)*sizeof(struct LevelHead));
        free(result->levelHead);
        result->levelHead = newLevel;
        result->levelLimit = level+10;
    }
    
    if (level >= (result->levelCount))
        result->levelCount = level+1;

    struct QueueNode *node = malloc(sizeof(struct QueueNode));
    node->val = root->val;
    node->next = result->levelHead[level].head;
    result->levelHead[level].head = node;
    result->levelHead[level].count++;
    
    BuildTree(root->left, result, level+1);
    BuildTree(root->right, result, level+1);
    return;
}

int** levelOrderBottom(struct TreeNode* root, int** columnSizes, int* returnSize) {
    if (root==NULL) return NULL;
    int levelMax=0;
    struct TreeResult *result = malloc(sizeof(struct TreeResult));
    result->levelLimit = 200;
    result->levelCount = 0;
    result->levelHead = malloc((result->levelLimit)*sizeof(struct LevelHead));
    memset(result->levelHead, 0, (result->levelLimit)*sizeof(struct LevelHead));

    BuildTree(root, result, 0);

    int** ret = (int**)malloc((result->levelCount)*sizeof(int*));;
    memset(ret, 0, (result->levelCount)*sizeof(int*));
    *columnSizes=(int*)malloc((result->levelCount)*sizeof(int));
    memset(*columnSizes, 0, (result->levelCount)*sizeof(int));
    //*columnSizes=(int*)malloc((10)*sizeof(int));
//*returnSize = result->levelHead[2].count;
//return ret;
//if (result->levelCount==751)
 //   return ret;
    
    struct QueueNode *node;
    int level;
    for (int i=0; i<(result->levelCount); i++) {
        level = (result->levelCount)-1-i;
        ret[i] = (int*)malloc((result->levelHead[level].count)*sizeof(int));
        (*columnSizes)[i] = (result->levelHead[level].count);
        node = result->levelHead[level].head;
        for (int j=(result->levelHead[level].count)-1; j>=0; j--) {
            ret[i][j] = node->val;
            node = node->next;
        }
        
    }

    *returnSize = result->levelCount;
    return ret;
}
