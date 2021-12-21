#include <stdio.h>
#include <stdlib.h>
#include <locale.h>


void main(){
    char vetor[5];
    setbuf(stdin, NULL);
    fgets(vetor, 5, stdin);
    printf("%s", vetor);
}
