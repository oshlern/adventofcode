// #define _GNU_SOURCE
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

const char* FILENAME = "input";
const int N_TRIALS = 4;
// const char* FILENAME = "test";
// const int N_TRIALS = 3;

long score_trial(long N, long best) {
    long cur = 0;
    for (long i = 0; i < N/2; i++) {
        cur += (-i) + (N-1-i);
        if (cur > best) {
            long n_ways = (N/2 - i) * 2;
            if (N%2 == 0)
                n_ways -= 1;
            return n_ways;
        }
    }
    return 0;
}

// from https://stackoverflow.com/a/1726321
void remove_spaces(char* s) { 
    char* d = s;
    do {
        while (*d == ' ') {
            ++d;
        }
    } while (*s++ = *d++);
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");

    getline(&line, &len, fp);
    strtok(line, ":");
    char* time_str = strtok(NULL, "\n");
    remove_spaces(time_str);
    long time = strtol(time_str, NULL, 10);

    getline(&line, &len, fp);
    strtok(line, ":");
    char* dist_str = strtok(NULL, "\n");
    remove_spaces(dist_str);
    long dist = strtol(dist_str, NULL, 10);

    printf("time %ld dist %ld\n", time, dist);
    long score = score_trial(time, dist);

    printf("score: %ld\n", score);

    fclose(fp);
    free(line);
    exit(EXIT_SUCCESS);
}