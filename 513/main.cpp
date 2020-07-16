// #include <queue>

// using namespace std;

// Definition for a binary tree node.
// struct TreeNode {
//     int val;
//     TreeNode *left;
//     TreeNode *right;
//     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
// };

class Solution {
public:
    int findBottomLeftValue(TreeNode* root) {
        
        int bl_val;
        queue<TreeNode*> q;

        q.push(root);
        while (!q.empty()) {
            bl_val = q.front()->val;
            int n = q.size();
            for(int i = 0; i < n; i++) {
                TreeNode* node = q.front();
                q.pop();
                if(node->left) { q.push(node->left); }
                if(node->right) { q.push(node->right); }
            }
        }

        return bl_val;

    }
};