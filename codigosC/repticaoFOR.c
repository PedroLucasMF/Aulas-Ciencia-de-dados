int main()
{
    float nota1 = 0; 
    float nota2 = 0;
    float n1 = 0;
    float n2 = 0;
    for (int i = 0; i < 5; i++){
        printf("digite a primeira e a segunda do aluno: ");
        scanf("%f %f", &n1, &n2);
        nota1 = n1 + nota1;
        nota2 = n2 + nota2;
    }
    float media1 = nota1/5; 
    float media2 = nota2/5;
    
    printf("\nA media na prova 1 e 2 são respectivamente: %f e %f", media1, media2);
return 0;
}