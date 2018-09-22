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
        vector<int> leaf_val_seq1 = get_leaf_val_seq(root1);
        vector<int> leaf_val_seq2 = get_leaf_val_seq(root2);

        return leaf_val_seq1 == leaf_val_seq2;
    }

private:
    vector<int> get_leaf_val_seq(TreeNode* node) {
        vector<int> leaf_val_seq;
        
        if(node) {
            if(node->left) {
                vector<int> temp = get_leaf_val_seq(node->left);
                leaf_val_seq.insert(leaf_val_seq.end(), temp.begin(), temp.end());
            }
            if(node->right) {
                vector<int> temp = get_leaf_val_seq(node->right);
                leaf_val_seq.insert(leaf_val_seq.end(), temp.begin(), temp.end());
            }
            if(!(node->left || node->right)) {
                leaf_val_seq.push_back(node->val);
            }
        }
        return leaf_val_seq;
    }

};