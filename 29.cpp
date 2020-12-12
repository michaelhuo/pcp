using namespace std;
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0) {
            return 0;
        }
        
        if (divisor == 1) {
            return dividend;
        }
        if (divisor == -1) {
            if (dividend == INT_MIN) {
                return INT_MAX;
            }
            return -dividend;
        }
        
        int ans = 0;
        bool negated = false;
        if (dividend > 0) {
            negated = true;
            dividend = - dividend;
        }
        
        if (divisor > 0) {
            negated = !negated;
            divisor = - divisor;
        }
        
        while (dividend <= divisor) {
            dividend -= divisor;
            ans++;
        }
        
        if (negated) {
            return -ans;
        } else {
            return ans;
        }
        
    }
};
