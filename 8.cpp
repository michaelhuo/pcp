class Solution {
public:
    int myAtoi(string s) {
        if (s.size() == 0) {
            return 0;
        }
        bool has_sign = false, in_number = false;
        int result = 0, sign = 1;
        for (auto c : s) {
            if (!in_number && c == ' ') {
                continue;
            }
            if (c == '+' || c == '-') {
                if (!in_number && !has_sign) {
                    in_number = true;
                    has_sign = true;
                    if (c == '-') {
                        sign = -1;
                    }
                } else {
                    break;
                }
            } else if (c >= '0' && c <= '9') {
                if (!in_number) {
                    in_number = 1;
                    result = c - '0';
                } else {
                    if (result > INT_MAX / 10) {
                        if (sign == 1) {
                            return INT_MAX;
                        } else {
                            return INT_MIN;
                        }
                    } else if (result == INT_MAX / 10) {
                        int n = INT_MAX % 10;
                        int m = c - '0';
                        cout << m <<' ' << n << endl;
                        if (sign == 1) {
                            if (m > n) {
                                return INT_MAX;
                            } else {
                                result = result * 10 + m;
                            }
                        } else {
                            if (m > n) {
                                return INT_MIN;
                            } else {
                                result = result * 10 + m;
                            }
                        }
                    } else {
                        result = result * 10 + c - '0';
                    }
                }
            } else {
                break;
            }      
        }
        return sign * result;
    }
};
