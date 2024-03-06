#include <iostream>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == 0) return 0;
        if ((dividend == INT_MIN) && (divisor == -1)) return INT_MAX;
        
        bool dividend_pos = (dividend > 0);
        bool neg = ((dividend > 0) != (divisor > 0));
        int sign = neg ? -1 : 1;
        int quotient = -sign; // offset loop by 1

        while (dividend_pos ? (dividend >= 0) : (dividend <= 0)) {
            quotient += sign;
            if (neg) {
                dividend += divisor;
            } else {
                dividend -= divisor;
            }
        }

        return quotient;
    }
};

int main() {
    Solution solution;
    int dividend = -2147483648;
    int divisor = 1;
    cout << solution.divide(dividend, divisor) << endl;
}