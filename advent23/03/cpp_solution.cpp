#include <iostream>

int main() {
    const char* in_str = "467..114..\n...*......\n..35..633.\n......#...\n617*......\n.....+.58.\n..592.....\n......755.\n...$.*....\n.664.598..";
    char* a = in_str;
    // auto b = a[1];
    const char* a = in_str;
    while (a[0] != NULL) {
        a += sizeof(char);
        std::cout << a[0] << std::endl;
    }
    std::cout << "Hello World" << std::endl;
    // std::cout << b << std::endl;
    // std::cout << a.size << std::endl;
    // std::cout << a.length << std::endl;
    std::cout << sizeof(*a) << std::endl;
    // std::cout << size(a)/size_t(a[0]) << std::endl;
    // std::cout << size_t(a) << std::endl;
    // std::cout << size_t(a[0]) << std::endl;
    // std::cout <<  << std::endl;
    
    
    // std::cout << (b == "1") << std::endl;
}