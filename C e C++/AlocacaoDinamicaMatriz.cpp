#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string.h>
#include <time.h>

using namespace std;

int** alocaMatriz(){
    int **matriz;
    int linhas = 3, colunas = 3;
    matriz = (int**) malloc(linhas * sizeof(int*));
    for(int i = 0; i < linhas; i++){
        matriz[i] = (int*) malloc(colunas * sizeof(int*));
    }
    return matriz;
}


int main(){
    srand((unsigned)time(NULL));
    int linhas = 3, colunas = 3;
    int** matriz;
    matriz = alocaMatriz();
    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            matriz[i][j] = ;
        }
    }
    for(int i = 0; i < linhas; i++){
        for(int j = 0; j < colunas; j++){
            cout << matriz[i][j] << " ";
        }
        cout << "\n";
    }
    return 0;

}
