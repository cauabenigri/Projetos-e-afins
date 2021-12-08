#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    int a;
    printf("Mude o valor de %d", a);
    scanf("%d", &a);
    printf("O valor agora é %d", a);
}
