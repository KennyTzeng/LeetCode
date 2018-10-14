class Solution {
public:
    string toGoatLatin(string S) {
        
        string result = "";
        string temp = "";
        string temp2 = "";
        string append = "a";
        
        for (int i = 0; i <= S.length(); i++) {
            if (S[i] == ' ' || S[i] == '\0') {
                if (!(temp[0] == 'a' || temp[0] == 'e' || temp[0] == 'i' || temp[0] == 'o' || temp[0] == 'u' || temp[0] == 'A' || temp[0] == 'E' || temp[0] == 'I' || temp[0] == 'O' || temp[0] == 'U')) {
                    temp2 = temp[0];
                    temp.erase(0, 1);
                    temp += temp2;
                }
                result += temp + "ma" + append;
                if (S[i] == ' ') { result += ' '; }
                temp = "";
                append += "a";
                
            } else {
                temp += S[i];
            }
        }

        return result;
    }
};