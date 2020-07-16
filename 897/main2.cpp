/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* increasingBST(TreeNode* root) {
        if(root == NULL) { return NULL; }

        TreeNode* head ;
        TreeNode* left = increasingBST(root->left);
        if(left != NULL) {
            head = left;
            TreeNode* temp = left;
            while(temp->right != NULL) {
                temp = temp->right;
            }
            temp->right = root;    
        }else {
            head = root;
        }

        root->left = NULL;
        TreeNode* right = increasingBST(root->right);
        if(right != NULL) {
            root->right = right;
        }else {
            root->right = NULL;
        }

        return head;
    }
};