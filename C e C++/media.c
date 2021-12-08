#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

 void main(){
    setlocale(LC_ALL, "");
    float a, b;
    fflush(stdin);
    printf("Digite um numero: ");
    scanf("%f", &a);
    printf("Digite outro numero: ");
    scanf("%f", &b);
    printf("A media entre %f e %f e %f", a, b, (a + b) / 2);
    system("pause");
 }
