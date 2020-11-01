
class Solution {
public:
    int reverse(int x) {
        if(!x) {
            return 0;
        }
        int sign = 1;
        if (x < 0 and x > INT_MIN) {
            sign = -1;
            x = -x;
        }
        unsigned long int result = 0UL;
        unsigned long int q = x;
        //cout << std::hex << q << '\t' << INT_MAX;

        while (q > 0) {
            unsigned long int r = q % 10UL;
            q /= 10UL;
            result = result * 10 + r;
            if (result > INT_MAX) {
                //cout << std::hex << result << '\t' << INT_MAX;
                result = 0;
                break;
            }
        }
        return sign * result;
    }
};
