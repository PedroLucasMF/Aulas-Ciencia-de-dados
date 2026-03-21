int main()
{
    int n1;
    int ma = 0;
    printf("digite um numero ");
    scanf("%d", &n1);
    int mo = n1;
    
    while(n1 >= 0){
        printf("digite um numero ");
        scanf("%d", &n1);
        if(n1 > ma){
            ma = n1;
        }
        if(n1 < mo && n1 >= 0){
            mo = n1;
        }
        else{}
    }
    printf("o maior e menor numero são: %d e %d", ma, mo);

    return 0;
}