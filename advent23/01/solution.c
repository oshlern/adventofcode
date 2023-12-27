#include <stdio.h>


int main(int argc, char *argv[]) {
    char string[] = "cas";
    printf(string);
    printf(strlen(string));

    // printf("Thanks for waddling through this program. Have a nice day.");
    return 0;
}


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