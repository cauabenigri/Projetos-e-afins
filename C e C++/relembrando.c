#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <locale.h>

char* aloca(int tamanho_palavra){
    char *aux;
    aux = (char*) malloc(tamanho_palavra * sizeof(char));
    return aux;
}

int main(){
    char *palavra;
    int tamanho;
    printf("Digite o tamanho da palavra: ");
    scanf("%d", &tamanho);
    palavra = aloca(tamanho);
    for(int i = 0; i < tamanho; i++){
        char letra = i + 100;
        palavra[i] = letra;
    }

    printf("%s", palavra);
    return 0;
}
