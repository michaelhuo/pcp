class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size() == 0 || strs[0].size() == 0) {
            return "";
        }
        int count = strs.size();
        for (int i = 0; i < strs[0].size(); ++i) {
            for (int j = 1; j < count; ++j) {
                if (strs[j][i] != strs[0][i]) {
                    return strs[0].substr(0, i);
                }
            }
        }
        return strs[0];
    }
};
