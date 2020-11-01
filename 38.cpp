class Solution {
public:
    string countAndSay(int n) {
        if (n == 0) {
            return "";
        }
        string s = "";
        for(int i = 0; i < n; i++) {
            s = countAndSay(s);
        }
        return s;
    }
    string countAndSay(string& s) {
        string output;
        if (s.size() == 0){
            return "1";
        }
        int count = 0;
        char prev = s[0];
        for (char c : s) {
            if (prev == c) {
                count ++;
            } else {
                output += char(count + '0');
                output += prev;
                prev = c;
                count = 1;
            }
        }
        output += char(count + '0');
        output += prev;
        return output;
    }
};
