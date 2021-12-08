#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

void main(){
    setlocale(LC_ALL, "");
    float a, b;
    int escolha;
    printf("Digite dois números: ");
    scanf("%f %f", &a, &b);
    printf("Qual operação deseja fazer? :\n[ 1 ] Adição\n[ 2 ] Subtração\n[ 3 ] Multiplicação\n[ 4 ] Divisão\n   >>>");
    scanf("%d", &escolha);
    switch(escolha){
        case 1:
            printf("O resultado é %.2f", a + b);
            break;
        case 2:
            printf("[ 1 ] %.2f - %.2f\n[ 2 ] %.2f - %.2f\n   >>>", a, b, b, a);
            scanf("%d", &escolha);
            if(escolha == 1){
                printf("O resultado é %.2f", a - b);
            }else if(escolha == 2){
                printf("O resultado é %.2f", b - a);
            }else{
                printf("Opção inválida");
            }
            break;
        case 3:
            printf("O resultado é %.2f", a * b);
            break;
        case 4:
            printf("[ 1 ] %.2f / %.2f\n[ 2 ] %.2f / %.2f\n   >>>", a, b, b, a);
            scanf("%d", &escolha);
            if(escolha == 1){
                printf("O resultado é %.2f", a / b);
            }else if(escolha == 2){
                printf("O resultado é %.2f", b / a);
            }else{
                printf("Opção inválida");
            }
            break;
        default:
            printf("Opção inválida");
    system("pause");
}
}
