#include <iostream>

int main() {
    const char* a = "12345";
    auto b = a[1];
    std::cout << "Hello World" << std::endl;
    std::cout << b << std::endl;
    // std::cout << (b == "1") << std::endl;
}