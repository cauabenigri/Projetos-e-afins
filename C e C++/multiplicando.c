#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    int a, b, c;
    printf("Digite 3 valores: ");
    scanf("%d %d %d", &a, &b, &c);
    printf("Resultado: %d", a * b * c);
}
