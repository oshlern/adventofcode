#include <iostream>
using namespace std;

class Solution {
public:
    int divide(int dividend, int divisor) {
        int divisors[32];
        int quotient = 0;
        int HALF_INT_MAX = 1073741824;
        divisors[0] = divisor;
        int idx = 0;
        while ((divisors[idx] <= HALF_INT_MAX) && (divisors[idx] <= dividend))  {
            divisors[idx+1] = divisors[idx] + divisors[idx];
            idx++;
        }

        for (; idx >= 0; idx--) {
            quotient = quotient + quotient;
            if (dividend >= divisors[idx]) {
                dividend -= divisors[idx];
                quotient += 1;
                cout << idx << ": divisor " << divisors[idx] << ", quotient " << quotient << ", remainder " << dividend << endl;

            }
        }
        return quotient;
    }
};

int main() {
    Solution solution;
    int dividend = 20;
    int divisor = 2;
    cout << solution.divide(dividend, divisor) << endl;
}




    // int divide(int dividend, int divisor) {
    //     if (dividend == 0) return 0;
    //     if ((dividend == INT_MIN) && (divisor == -1)) return INT_MAX;
        
    //     bool dividend_pos = (dividend > 0);
    //     bool neg = ((dividend > 0) != (divisor > 0));
    //     int sign = neg ? -1 : 1;
    //     int quotient = -sign; // offset loop by 1

    //     while (dividend_pos ? (dividend >= 0) : (dividend <= 0)) {
    //         quotient += sign;
    //         if (neg) {
    //             dividend += divisor;
    //         } else {
    //             dividend -= divisor;
    //         }
    //     }

    //     return quotient;
    // }

