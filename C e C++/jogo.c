#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <time.h>

void main(){
    setlocale(LC_ALL, "");
    srand((unsigned)time(NULL));
    int nmr = rand() % 11, esc, ten;
    printf("Tente advinhar um número de 1 a 10: ");
    scanf("%d", &esc);
    ten++;
    while(esc != nmr){
        if(nmr > esc){
            printf("Mais...");
            scanf("%d", &esc);
            ten++;
        }else{
            printf("Menos...");
            scanf("%d", &esc);
            ten++;
        }
    }
    printf("Você ganhou! Foram necessarias %d tentativas!", ten);
}
