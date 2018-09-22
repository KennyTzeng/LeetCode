// #include <vector>
// using namespace std;
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<int> result;

    vector<int> postorder(Node* root) {
        
        if(root) {
            visit(root);
        }
        return result;
    }

private:
    void visit(Node* node) {

        for(Node* child : (node->children)) {
            visit(child);
        }
        result.push_back(node->val);
    }

};