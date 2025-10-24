class Solution {
    public:
        int nextBeautifulNumber(int n) {
            int* digits = new int[7]();
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
                increment(digits + 1, counts);
                counts[*digits]++;
            }
        }
    };
