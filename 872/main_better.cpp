// #include <vector>
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
    bool leafSimilar(TreeNode* root1, TreeNode* root2) {
        vector<int> leaf_val_seq1, leaf_val_seq2;
        get_leaf_val_seq(root1, leaf_val_seq1);
        get_leaf_val_seq(root2, leaf_val_seq2);
        return leaf_val_seq1 == leaf_val_seq2;
    }

private:
    void get_leaf_val_seq(TreeNode *node, vector<int> &leaf_val_seq)
    {
        if(!node) {
            return;
        }
        if(!(node->left || node->right)) {
            leaf_val_seq.push_back(node->val);
            return;
        }
        get_leaf_val_seq(node->left, leaf_val_seq);
        get_leaf_val_seq(node->right, leaf_val_seq);
    }
    
};