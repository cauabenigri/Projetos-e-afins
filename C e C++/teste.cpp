#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <iostream>
#include <locale.h>

int main(){
    setlocale(LC_ALL, "");
    std::string palavra;
    std::cout << "Digite uma palavra";
    std::cin >> palavra;
    std::cout << palavra;
    system("pause");
    return 0;
}

