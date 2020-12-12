class Solution {
public:
    int getSum(int a, int b) {
        int bit = 1;
        bool carry = false;
        unsigned int mask = INT_MIN;
        int answer = 0;
        if (a == 0) {
            return b;
        }
        if (b == 0) {
            return a;
        }
        
        for (int i = 0; i <= 31; ++i) {

            int s = (a & bit) ^ (b & bit);
            bool c = (a & bit) && (b & bit);
            if (carry) {
                carry = c || ((s & bit) != 0);
                s = (s & bit) ^ bit;
            } else{
                carry = c;
            }
            answer |= s;
            //cout << bit << ',' << s << ',' << c << ',' << answer << endl;
            if (bit == INT_MIN) {
                break;
            }
            bit <<= 1;
        }
        return answer;
    }
};
