#include <string.h>
#include <stdio.h>
#include <stdlib.h>

void read_ns(char* str, int* ns) {
    char* token = strtok(str, " ");
    int i = 0;
    while (token != NULL) {
        ns[i++] = atoi(token);
        token = strtok(NULL, " ");
    }
}

int score_line(char* line) {
    char* card_str = strtok(line, ":");
    char*  win_str = strtok(NULL, "|");
    char* have_str = strtok(NULL, "\n");

    int win_ns[10];
    int have_ns[25];

    read_ns(win_str, win_ns);
    read_ns(have_str, have_ns);

    
    int score = 0;
    for (int i=0; i<10; i++) {
        for (int j=0; j<25; j++) {
            if (win_ns[i] == have_ns[j]) {
                // printf("%s. %d %d | %d %d == %d, \n", card_str, i, j, win_ns[i], have_ns[j], win_ns[i] == have_ns[j]);
                if (score == 0) {
                    score = 1;
                } else {
                    score *= 2;
                }
            }
        }
    }
    return score;
}


int main(int argc, char *argv[]) {
    char* filename = "input";
    // char* filename = "test";

    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(filename, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    int total = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        // printf("%s", line);
        int score = score_line(line);
        // printf("%d\n", score);

        total += score;
    }

    printf("%d\n", total);

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}