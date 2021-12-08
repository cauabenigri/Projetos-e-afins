#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    float a, b;
    printf("Digite um número: ");
    scanf("%f", &a);
    printf("Digite outro número: ");
    scanf("%f", &b);
    float result = a - b;
    printf("A diferença entre %f e %f é %f", a, b, fabs(result));
}
