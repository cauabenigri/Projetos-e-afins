#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    int num, cont, i;
    printf("Digite um número: ");
    scanf("%d", &num);
	for(i = 1; i <= num; i++){
        if(num % i == 0){
            cont = cont + 1;
        }
	}
	if(cont == 2){
        printf("O número é primo");
	}else{
        printf("O número não é primo");
	}
}
