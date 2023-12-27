#include <string.h>
#include <stdio.h>
#include <stdlib.h>

struct Balls {
    int blue;
    int red;
    int green;
    int game_id;
};

struct Balls seen_balls(char* line) {
    struct Balls seen = {0, 0, 0};
    char *draw, *color;
    char *ptr1, *ptr2, *ptr3;
    strtok_r(line, " ", &ptr1);
    seen.game_id = atoi(strtok_r(NULL, ":", &ptr1));
    while ((draw = strtok_r(NULL, ";", &ptr1))) {
        char* one_ball = strtok_r(draw, ",\n", &ptr2);
        while (one_ball != NULL) {
            int n = atoi(strtok_r(one_ball, " ", &ptr3));
            char* color = strtok_r(NULL, " ", &ptr3);
            if ((strcmp(color, "red") == 0) && (seen.red < n)) {
                seen.red = n;
            } else if ((strcmp(color, "blue") == 0) && (seen.blue < n)) {
                seen.blue = n;
            } else if ((strcmp(color, "green") == 0) && (seen.green < n)) {
                seen.green = n;
            }
            one_ball = strtok_r(NULL, ",\n", &ptr2);
        }
    }
    return seen;
}



int main(int argc, char *argv[]) {
    char* filename = "input.txt";
    // char* filename = "test_input.txt";

    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen(filename, "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);

    int max_blue = 14, max_red = 12, max_green = 13;
    int total = 0;
    int power = 0;
    while ((read = getline(&line, &len, fp)) != -1) {
        struct Balls seen = seen_balls(line);
        if ((max_blue >= seen.blue) && (max_green >= seen.green) && (max_red >= seen.red))
            total += seen.game_id;
        power += seen.blue * seen.green * seen.red;
    }

    printf("total: %d\npower: %d\n", total, power);

    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}