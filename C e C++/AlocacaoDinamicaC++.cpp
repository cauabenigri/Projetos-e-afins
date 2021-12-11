#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <new>

using namespace std;
int main(){
    int tamanho, i;
    cout << "Digite um tamanho para o vetor: ";
    cin >> tamanho;
    int *vetor = new int(tamanho);
    for(i = 0; i < tamanho; i++){
        vetor[i] = i + 2;
        cout << vetor[i] << "\n";
    }
    cout << vetor[1];
    return 0;

}
