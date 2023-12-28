// #define _GNU_SOURCE
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

// const char* FILENAME = "input";
// const int N_TRIALS = 4;
const char* FILENAME = "test";
const int N_TRIALS = 3;

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
int score_trial(int N, int best) {
    int cur = 0;
    // for (int i = 0; i < N/2; i++) {
    //     cur += (-i) + (N-1-i);
    //     if (cur > best) {
    //         int n_ways = (N/2 - i) * 2;
    //         if (N%2 == 0)
    //             n_ways -= 1;
    //         return n_ways;
    //     }
    // }
    return 0;
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");

    char *times_str, *dists_str;
    
        times[i] = atoi(strtok_r(NULL, " ", &times_str));
    printf("A %s\n", times_str);

    getline(&line, &len, fp);
    strtok_r(line, ":", &dists_str);
    printf("A %s\n", times_str);
    printf("B %s\n", dists_str);

    int total = 1;
    for (int i = 0; i < N_TRIALS; i++) {
        int time = atoi(strtok_r(NULL, " ", &times_str));
        int dist = atoi(strtok_r(NULL, " ", &dists_str));
        int score = score_trial(time, dist);
        // printf("time: %d, dist: %d, score: %d\n", time, dist, score);
        // total *= score;
    }
    printf("%d", total);


    fclose(fp);
    free(line);
    exit(EXIT_SUCCESS);
}