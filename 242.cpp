class Solution {
public:
    bool isAnagram(string s, string t) {
        if ((s.size() == 0) && (t.size() == 0)) {
            return true;
        }
        if (s.size() != t.size()) {
            return false;
        }
        std::sort(s.begin(), s.end());
        std::sort(t.begin(), t.end());
        return (s == t);
    }
};
