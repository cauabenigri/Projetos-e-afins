#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>

int* alocaVetor(int tamanho){
    int *aux;
    aux = (int*) malloc(tamanho * sizeof(int));
    return aux;
}

int main(){
    int tamanho_vetor, *vetor;
    std::cout << "Digite um tamanho para o vetor";
    std::cin >> tamanho_vetor;
    vetor = alocaVetor(tamanho_vetor);
    vetor[0] = 12;
    std::cout << vetor[0];
    free(vetor);
    return 0;

}
