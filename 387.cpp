#include <unordered_map>

class Solution {
public:
    int firstUniqChar(string s) {
        if (s.size() < 1) {
            return -1;
        }
        int length = s.size();
        unordered_map<char,int> ss;
        for(int i = 0; i < length; ++i) {
            char c = s[i];
            if (ss.count(c) > 0) {
                ss[c] = length;
            } else {
                ss[c] = i;
            }
        }
        int result = length;
        for (const auto & it : ss) {
            int i = it.second;
            if (i < result) {
                result = i;
            }
        }
        if (result == length) {
            return -1;
        } else {
            return result;
        }
    }
};
