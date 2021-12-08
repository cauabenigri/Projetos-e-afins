#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    float a, b, c;
    printf("Digite a primeira nota: ");
    scanf("%f", &a);
    printf("Digite a segunda nota: ");
    scanf("%f", &b);
    printf("Digite a terceira nota: ");
    scanf("%f", &c);
    float resultado = (a + b + c) / 3;
    printf("A média entre %.2f, %.2f e %.2f é %.2f", a, b, c, resultado);
    if(resultado >= 7){
        printf("Você foi aprovado!");
    }else{
        printf("\nVocê está de recuperação por %.2f pontos!", 7 - resultado);
    }
}
