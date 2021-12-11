#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
#include <string>

void fatorial(int f);

int main(){
    int num = 0;
    std::cout <<  "Digite um número para fazer o fatorial: ";
    std::cin >> num;
    fatorial(num);
    return 0;

}

void fatorial(int f){
    int i, fatorial =  1;
    for(i = f; i > 0; i--){
        fatorial *= i;
        if(i > 1){
            std::cout << i << " x ";
        }else{
            std::cout << i << " = ";
        }
    }
    std::cout << fatorial;
}
