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

    char * digits[10] = {"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
    int total = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        int first_d = 0;
        int last_d = 0;
        for (int i = 0; i < read; i++) {
            int d = 0;
            for (int j = 0; j < 9; j++) {
                if (strlen(digits[j]) < read - i)
                    if (strncmp(line + i, digits[j], strlen(digits[j])) == 0)
                        d = j+1;
            }
            if (isdigit(line[i]))
                d = line[i] - '0';

            if (d) {
                if (first_d == 0) {
                    first_d = d;
                }
                last_d = d;
            }
        }
        // printf("%s", line);
        // printf("\t\ttotal: %d, update: %d\n", total, first_d * 10 + last_d);
        total += first_d * 10 + last_d;
    }
    printf("\n%d\n", total);

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}
