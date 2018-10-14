// #include <vector>
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
    vector<int> largestValues(TreeNode* root) {
        
        vector<int> result;
        queue<TreeNode*> q;

        if (!root) {
            return result;
        }

        q.push(root);
        while (!q.empty()) {
            int max = q.front()->val;
            int n = q.size();
            for (int i = 0; i < n; i++) {
                TreeNode* node = q.front();
                q.pop();
                if (node->left) { q.push(node->left); }
                if (node->right) { q.push(node->right); }
                if (node->val > max) { max = node->val; }
            }
            result.push_back(max);
        }

        return result;

    }
};