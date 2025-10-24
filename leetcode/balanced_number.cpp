class Solution {
public:
    int nextBeautifulNumber(int n) {
        // int L = std::ceil(std::log10(n)) + 1;
        int* digits = new int[14]();
        int* counts = new int[10]();
        int i = 0;
        int d;
        int N = n;
        while (n > 0) {
            d = n % 10;
            digits[i] = d;
            counts[d]++;
            n = n / 10;
            i++;
        }
        increment(digits, counts);
        N++;
        while (!isValid(counts)) {
            increment(digits, counts);
            N++;
            // std::cout << N << " N" << std::endl;
            // print(digits, counts);
        }
        return N;
    }

    bool isValid(int* counts) {
        for (int i = 0; i < 10; i++) {
            if ((counts[i] != i) && (counts[i] != 0)) {
                return false;
            }
        }
        return true;
    }

    void increment(int* digits, int* counts) {
        if (counts[*digits] != 0) {
            counts[*digits]--;
        }

        if (*digits != 9) {
            (*digits)++;
            counts[*digits]++;
        } else {
            *digits = 0;
            // std::cout << "before " << *digits << " counts " << counts[*digits] << std::endl;

            // std::cout << "after " << *digits << " counts " << counts[*digits] << std::endl;
            increment(digits + 1, counts);
            counts[*digits]++;
        }
    }

    void print(int* digits, int* counts) {
        for (int i = 0; i < 7; ++i) {
            std::cout << digits[i];
        }
        // std::cout << " Digits" << std::endl;
        for (int i = 0; i < 10; ++i) {
            std::cout << counts[i];
        }
        // std::cout << " Counts" << std::endl;
    }

    // std::cout << "log10(" << n << ") = " << result << std::endl;
    // return result;
        // digits = array(len=log10(n)+1))
        // counts = array(len=10)
        // // fill digits
        // // fill counts

        // while !isValid(counts):
        //     increment digits
        //     edit counts
};
