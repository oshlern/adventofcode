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
    int time = atoi(time_str);

    getline(&line, &len, fp);
    strtok(line, ":");
    char* dist_str = strtok(NULL, "\n");
    remove_spaces(dist_str);
    int dist = atoi(dist_str);
    // int dist;
    // getline(&line, &len, fp);
    // strtok(line, ":");
    // // sscanf(strtok(NULL, "\n"), "%d", &dist);
    // dist = atoi(strtok(NULL, "\n"), NULL, 10);

    printf("a %d %d\n", time, dist);
    int score = score_trial(time, dist);



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