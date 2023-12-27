// #define _GNU_SOURCE
// #include <string.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    FILE* fp;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    fp = fopen("input", "r");
    if (fp == NULL)
        exit(EXIT_FAILURE);
    while ((read = getline(&line, &len, fp)) != -1) {
        printf("Retrieved line of length %zu: %zu\n", read, len);
        printf("%s", line);
    }
    fclose(fp);
    if (line)
        free(line);
    exit(EXIT_SUCCESS);
}

// int main(int argc, char *argv[]) {
    // char string[] = "cas";
    // printf("%s\n", string);
    // printf("%lu\n", strlen(string));
// }


// int main() {
//     const char* a = "12345";
//     auto b = a[1];
//     std::cout << "Hello World" << std::endl;
//     std::cout << b << std::endl;
//     // std::cout << (b == "1") << std::endl;
// }