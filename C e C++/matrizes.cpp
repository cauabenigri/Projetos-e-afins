#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <string>
#include <iostream>

int main(){
    setlocale(LC_ALL, "");
    std::string matriz[3][3];
    int i, j;
    for(i = 0; i < 3; i++){
        for(j = 0; j < 3; j++){
            std::cout << "Digite um número para a posição";
            std::cout << "[" << i << "." << j << "]" << " " ;
            setbuf(stdin, NULL);
            std::cin >> matriz[i][j];
        }
    }
    for(i = 2
        ; i >= 0; i--){
        for(j = 0; j <= 2; j++){
            std::cout << matriz[i][j] << " ";
        }
        std::cout << "\n";
    }
    system("pause");
    return 0;
}
