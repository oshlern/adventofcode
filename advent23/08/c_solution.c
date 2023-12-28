#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <regex.h>

const char* FILENAME = "input";
// const char* FILENAME = "test";
// const char* FILENAME = "test2";

struct Node {
    char *name, *R_name, *L_name;
    struct Node *R, *L, *next;
};

struct Node* base = NULL;


int readLine(char* line) {

    const char *inputString = "AAA = (BBB, CCC)";

    const char *pattern = "([A-Z]+) = \\(([A-Z]+), ([A-Z]+)\\)";

    regex_t regex;
    int status = regcomp(&regex, pattern, REG_EXTENDED);

    if (status != 0) {
        char error_buffer[100];
        regerror(status, &regex, error_buffer, sizeof(error_buffer));
        fprintf(stderr, "Regex compilation failed: %s\n", error_buffer);
        return 1;
    }

    // Match the regular expression against the input string
    regmatch_t matches[4];
    status = regexec(&regex, inputString, 4, matches, 0);

    // Check for a successful match
    if (status = 0) {
        // Extract matched groups
        for (size_t i = 1; i < sizeof(matches) / sizeof(matches[0]); ++i) {
            if (matches[i].rm_so == -1) {
                // No match for this group
                continue;
            }

            printf("Matched group %zu: %.*s\n", i, (int)(matches[i].rm_eo - matches[i].rm_so), inputString + matches[i].rm_so);
        }
    } else if (status == REG_NOMATCH) {
        fprintf(stderr, "No match found.\n");
    } else {
        char error_buffer[100];
        regerror(status, &regex, error_buffer, sizeof(error_buffer));
        fprintf(stderr, "Regex matching failed: %s\n", error_buffer);
    }

    // Free the compiled regular expression
    regfree(&regex);
}

int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(FILENAME, "r");

    read = getline(&line, &len, fp);
    int instructions[(int) read];
    for (int i = 0; i < read; i++)
        instructions[i] = (line[i] == 'R');

    getline(&line, &len, fp); // empty row

    // while ((read = getline(&line, &len, fp)) != -1) {
    //     char* hand = strtok(line, " ");
    //     int bid = atoi(strtok(NULL, "\n"));
    //     int score = getScore(hand);
    //     // printf(hand);
    //     insertNode(hand, score, bid);
    // }
    readLine(line);

    // int total = 0;
    // struct Node* head = base;
    // for (int rank=1; head != NULL; head = head->next, rank++) {
    //     printf("%d %s %d\n", rank, head->hand, head->bid);
    //     total += rank * head->bid;
    //     free(head->hand);
    // }
    // printf("%d\n", total);

    fclose(fp);
    free(line);
    exit(EXIT_SUCCESS);
}