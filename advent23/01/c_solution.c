#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, char *argv[]) {
    char* filename = "input.txt";
    // char* filename = "test_input.txt";

    FILE* fp = fopen(filename, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    
    int total = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        int first_d = 0;
        int last_d = 0;
        for (int i = 0; i < read; i++) {
            char c = line[i];
            if (isdigit(c)) {
                if (first_d == 0) {
                    first_d = c - '0';
                }
                last_d = c - '0';
            }
        }
        // printf("Retrieved line of length %zu: %zu\n", read, len);
        printf("%s", line);
        printf("\t\ttotal: %d, update: %d\n", total, first_d * 10 + last_d);
        total += first_d * 10 + last_d;
    }
    printf("\n%d\n", total);

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}
