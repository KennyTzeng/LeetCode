#include <string>

using namespace std;

class Solution {
public:
    string toLowerCase(string str) {
        string l_str = "";
        for(int i=0; i<str.length();i++) {
            l_str += tolower(str[i]);
        }
        return l_str;
    }
};