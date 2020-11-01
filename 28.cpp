class Solution {
public:
    int strStr(string haystack, string needle) {
        if (needle.size() == 0) {
            return 0;
        }
        if (haystack.size() == 0) {
            return -1;
        }

        int n = haystack.size();
        int l = needle.size();
        if (l > n) {
            return -1;
        }
        int i = 0;
        while (i < n - l + 1) {
            if (haystack[i] != needle[0]) {
                i++;
                continue;
            }
            int j = 1;
            while ((j < l) && (i + j < n) && (haystack[i + j] == needle[j])) {
                j++;
            }
            if (j == l) {
                return i;
            } else if (i + j == n - l + 1) {
                return -1;
            } else {
                i += j - 1;
            }
        }
        return -1;
    }
};
