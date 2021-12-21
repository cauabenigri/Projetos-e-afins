#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <iostream>
#include <locale.h>

using namespace std;


struct palavra{;
    char pal1[5];
    char pal2[10];
};
int* aloca(int tamanho_vetor){
    int *aux;
    aux = (int*) malloc(tamanho_vetor * sizeof(int));
    return aux;
}
int main(){
    struct palavra Palavra;
    int *vetor, tamanho;
    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanho);
    vetor = aloca(tamanho);
    for(int i = 1; i <= tamanho; i++){
        vetor[i] = i * 2;
        printf("%d", vetor[i]);
    printf("%d", sizeof(Palavra.pal1)/sizeof(int));
    for(int i = 0; i < 5; i++){
        Palavra.pal1[i] = i * 3;
        printf("%d\n", Palavra.pal1[i]);
    }
    }
    return 0;
}
