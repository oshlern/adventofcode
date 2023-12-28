// #define _GNU_SOURCE
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

const char* FILENAME = "input";
const int N_TRIALS = 4;
// const char* FILENAME = "test";
// const int N_TRIALS = 3;

int score_trial(int N, int best) {
    int cur = 0;
    for (int i = 0; i < N/2; i++) {
        cur += (-i) + (N-1-i);
        if (cur > best) {
            int n_ways = (N/2 - i) * 2;
            if (N%2 == 0)
                n_ways -= 1;
            return n_ways;
        }
    }
    return 0;
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");

    int times[N_TRIALS];
    getline(&line, &len, fp);
    strtok(line, ":");
    for (int i = 0; i < N_TRIALS; i++)
        times[i] = atoi(strtok(NULL, " "));

    int dists[N_TRIALS];
    getline(&line, &len, fp);
    strtok(line, ":");
    for (int i = 0; i < N_TRIALS; i++)
        dists[i] = atoi(strtok(NULL, " "));

    int total = 1;
    for (int i = 0; i < N_TRIALS; i++) {
        int score = score_trial(times[i], dists[i]);
        printf("time: %d, dist: %d, score: %d\n", times[i], dists[i], score);
        total *= score;
    }
    printf("%d\n", total);


    fclose(fp);
    free(line);
    exit(EXIT_SUCCESS);
}



// n chose i
// n!/i!*(n-i)!
// 1
// i=0
// * (n-i/i+1)
// 0*7
// 1*6
// 2*5
// 3*4

// 
// -i + n-i-1
// 