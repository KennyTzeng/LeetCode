class Solution {
public:
    string toGoatLatin(string S) {

        string result, word;
        string append = "a";
        istringstream ss(S);

        while (ss >> word) {
            if (!isVow(word[0])) {
                word += word[0];
                word.erase(0,1);
            }
            result += " " + word + "ma" + append;
            append += "a";
        }

        return result.substr(1);
    }

    bool isVow(char c) {
        return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' || c == 'A' || c =='E' || c == 'I' || c == 'O' || c == 'U';
    }
};