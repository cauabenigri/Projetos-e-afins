#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    char palavra[25];
    setbuf(stdin, NULL);
    printf("Digite uma palavra: ");
    fgets(palavra, 25, stdin);
    printf("\nA palavra é %s", palavra);
}
