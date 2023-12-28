// #define _GNU_SOURCE
#include <string.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>

// const char* FILENAME = "input";
// const int NUM_SEEDS = 20;
const char* FILENAME = "test";
const int NUM_SEEDS = 4;
const int MAX_PAIRS = 1000;

int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");
    
    long seeds[MAX_PAIRS][2];
    int seed_i, new_i;
    getline(&line, &len, fp);
    strtok(line, " ");
    for (seed_i = 0; seed_i < NUM_SEEDS/2; seed_i++) {
        seeds[seed_i][0] = strtol(strtok(NULL, " \n"), NULL, 10);
        seeds[seed_i][1] = strtol(strtok(NULL, " \n"), NULL, 10);
    }

    long news[MAX_PAIRS][2];
    // for (new_i = 0; new_i < MAX_PAIRS; new_i++) {
    //     news[new_i][0] = -1;
    //     news[new_i][1] = -1;
    //     if (i >= NUM_SEEDS/2) {
    //         seeds[i][0] = -1;
    //         seeds[i][1] = -1;
    //     }
    // }

    getline(&line, &len, fp); // "\n"
    while ((read =  getline(&line, &len, fp)) != -1) { // "a-to-b map:"
        while ((read = getline(&line, &len, fp)) > 2) { // "x y z"
            long dst_st = strtol(strtok(line, " "), NULL, 10);
            long src_st = strtol(strtok(NULL, " "), NULL, 10);
            long range = strtol(strtok(NULL, "\n"), NULL, 10);
            long S = src_st;
            long E = src_st + range;
            for (int i = 0; i < seed_i; i++) {
                long s = seeds[i][0];
                long e = seeds[i][0];
                if ((s > S) && (s < E)) {
                    if (e < E) {
                        new
                    }
                }
                if ((src_st <= cur) && (cur < src_st + range))
                    news[i] = cur - src_st + dst_st;
            }
            // S s E e ==> NS NE, ns e
            // S s e E ==> NS NE
            // s S e E ==> NS NE
            // s S E e ==> NS NE, s S, E e
        }
        for (int i = 0; i < NUM_SEEDS; i++) {
            printf("seed: %ld, \tnew:%ld\n", seeds[i], news[i]);
            if (news[i] != -1)
                seeds[i] = news[i]; // else don't change
            news[i] = -1;
        }
    }
//28965817 + 1059891351
    long min_loc = seeds[0];
    for (int i = 0; i < NUM_SEEDS; i++)
        if (seeds[i] < min_loc)
            min_loc = seeds[i];
    printf("%ld\n", min_loc);
    // printf("Maximum value of int: %d\n", INT_MAX);

    fclose(fp);
    free(line);
    exit(EXIT_SUCCESS);
}

// void read_seeds(char* line, int seeds[]) {
//     strtok(line, " ");
//     for (int i = 0; i < NUM_SEEDS; i++)
//         seeds[i] = atoi(strtok(NULL, " \n"));
// }

void read_map(FILE* fp) {
    // strtok(line, " ");
    // for (int i = 0; i < NUM_SEEDS; i++)
    //     seeds[i] = atoi(strtok(NULL, " \n"));
}