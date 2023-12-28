#include <string.h>
#include <stdio.h>
#include <stdlib.h>

const char* FILENAME = "input";
const int NUM_CARDS = 202;
const int NUM_WIN = 10;
const int NUM_HAVE = 25;
// const char* FILENAME = "test";
// const int NUM_CARDS = 6;
// const int NUM_WIN = 5;
// const int NUM_HAVE = 8;

void read_ns(char* str, int* ns) {
    char* token = strtok(str, " ");
    int i = 0;
    while (token != NULL) {
        ns[i++] = atoi(token);
        token = strtok(NULL, " ");
    }
}

void score_line(char* line, int* copies) {
    // printf("%s", line);
    // for (int i = 1; i<NUM_CARDS; i++) {
        // total += copies[i];
        // printf("Card %d: %d copies\n", i, copies[i]);
    // }
    char* card_str = strtok(line, ":");
    char*  win_str = strtok(NULL, "|");
    char* have_str = strtok(NULL, "\n");

    int win_ns[NUM_WIN];
    int have_ns[NUM_HAVE];
    strtok(card_str, " ");
    int card_i = atoi(strtok(NULL, ":")) - 1;
    // printf("-%d copies: %d\n", card_i, copies[card_i]);

    read_ns(win_str, win_ns);
    read_ns(have_str, have_ns);

    int matches = 0;
    for (int i=0; i<NUM_WIN; i++) {
        for (int j=0; j<NUM_HAVE; j++) {
            if (win_ns[i] == have_ns[j]) {
                matches++;
            }
        }
    }
    for (int i = 0; i < matches && card_i + i + 1 < NUM_CARDS; i++) {
        copies[card_i+1+i] += copies[card_i];
    }
    // printf("%d %d copies: %d\n", card_i, matches, copies[card_i]);
}


int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    int copies[NUM_CARDS];
    for (int i = 0; i<NUM_CARDS; i++)
        copies[i] = 1;
    while ((read = getline(&line, &len, fp)) != -1)
        score_line(line, copies);
    
    int total = 0;
    for (int i = 0; i<NUM_CARDS; i++) {
        total += copies[i];
        // printf("Card %d: %d copies\n", i, copies[i]);
    }
    printf("%d\n", total);

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}