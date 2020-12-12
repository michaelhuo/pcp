using namespace std;
class Solution {
public:
    int divide(int dividend, int divisor) {
        const int HALF_INT_MIN = -1073741824;
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
        int factor = 1;
        int n = divisor;

        while (n >= dividend - n) {
            if (n == HALF_INT_MIN) {
                break;
            }
            n += n;
            factor <<= 1;
        }

        //cout << n << ',' << factor << endl;
        ans = 0;
        
        while (dividend < 0) {
            while (dividend <= n) {
                //cout << dividend << ',' << n << endl;
                dividend -= n;
                ans += factor;
            }
            n >>= 1;
            factor >>= 1;   
        }
//        while (dividend <= divisor) {
//            dividend -= divisor;
//            ans++;
//        }
        
        if (negated) {
            return -ans;
        } else {
            return ans;
        }
        
    }
};
