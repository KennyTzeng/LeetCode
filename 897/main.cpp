// #include <stdlib.h>
// #include <queue>
// #include <stack>

// using namespace std;

// Definition for a binary tree node.
/*
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};
*/

class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        if(!root) { return NULL; }

        queue<TreeNode*> que;
        stack<TreeNode*> stk;

        // put TreeNode to queue in-order 
        while(root != NULL || !stk.empty()) {
            while(root != NULL) {
                stk.push(root);
                root = root->left;
            }
            if(!stk.empty()) {
                que.push(stk.top());
                root = stk.top()->right;
                stk.pop();
            }
        }

        // create the increasing BST
        root = que.front();
        root->left = NULL;
        root->right = NULL;
        que.pop();
        TreeNode* node = root;
        TreeNode* child;
        while(!que.empty()) {
            child = que.front();
            child->left = NULL;
            child->right = NULL;
            que.pop();
            node->right = child;
            node = node->right;
        }

        return root;
    }
};