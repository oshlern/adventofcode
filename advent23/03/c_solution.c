// #define _GNU_SOURCE
// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    // FILE * fp;
    // char * line = NULL;
    // size_t len = 0;
    // ssize_t read;
    FILE* file_pointer;
    char* line = NULL;
    size_t len = 0;
    ssize_t read;
    file_pointer = fopen("input", "r");
    if (file_pointer == NULL) {
        exit(EXIT_FAILURE);
    }
    while ((read = getline(&line, &len, file_pointer)) != -1) {
        printf("Retrieved line of length %zu:\n", read);
        printf("%s", line);
    }

    // fp = fopen("input", "r");
    // if (fp == NULL)
    //     exit(EXIT_FAILURE);

    // while ((read = getline(&line, &len, fp)) != -1) {
    //     printf("Retrieved line of length %zu:\n", read);
    //     printf("%s", line);
    // }

    fclose(file_pointer);
    if (line)
        free(line);
    // if (*line_pointer)
    //     free(*line_pointer);
    exit(EXIT_SUCCESS);
}

// int main(int argc, char *argv[]) {
    // char string[] = "cas";
    // printf("%s\n", string);
    // printf("%lu\n", strlen(string));


    // printf("Thanks for waddling through this program. Have a nice day.");
    // return 0;
// }


// char* * readlines(const char* fname) {
//     FILE* file_pointer;
//     char** lines;
//     char** line_pointer;
//     size_t len = 0;
//     ssize_t read;
//     file_pointer = fopen("input", "r");
//     while ((read = getline(&line_pointer, &len, file_pointer)) > 0) {
//         printf("Retrieved line of length %zu:\n", read);
//         printf("%s", *line_pointer);
//     }
//     fclose(file_pointer);
//     if (*line_pointer)
//         free(*line_pointer);
//     exit(EXIT_SUCCESS);
//     // return 0;
// }

    // free(line_pointer);
    // char line [1000];
    // while (getline(line, &len_pointer, file_pointer) > 0) {
    // int main ( void )
// {
//   char filename[] = "file.txt";
//   FILE *file = fopen ( filename, "r" );

//   if (file != NULL) {
//     char line [1000];
//     while(fgets(line,sizeof line,file)!= NULL) /* read a line from a file */ {
//       fprintf(stdout,"%s",line); //print the file contents on stdout.
//     }

//     fclose(file);
//   }
//   else {
//     perror(filename); //print the error message on stderr.
//   }

//   return 0;
// }
        
//     }

// }

// int main(int argc, char *argv[]) {
//     char string[] = "cas";
//     printf("%s\n", string);
//     printf("%lu\n", strlen(string));

//     // printf("Thanks for waddling through this program. Have a nice day.");
//     return 0;
// }


// int main(int argc, char *argv[]) {
//     int i;
//     int count = 0;
//     int *p = &count;

//     for (i = 0; i < 10; i++) {
//         (*p)++; // Do you understand this line of code and all the other permutations of the operators? ;)
//         // printf(count);
//         // printf(*p);
//         // printf(i);
//         printf("" + i  "");
//     }

//     printf("Thanks for waddling through this program. Have a nice day.");
//     return 0;
// }

// int main() {
//     const char* a = "12345";
//     auto b = a[1];
//     std::cout << "Hello World" << std::endl;
//     std::cout << b << std::endl;
//     // std::cout << (b == "1") << std::endl;
// }