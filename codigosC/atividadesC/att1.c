int main()
{
int numero;
printf("insira um numero: ");
scanf("%d", &numero);
printf("\nvalor lido: %d", numero);
float numerof;
 printf("insira um numero: ");
 scanf("%f", &numerof);
 printf("\nvalor lido: %f", numerof);
int dia, mes, ano, hora, minuto;
 printf("insira o dia: ");
 scanf("%d", &dia);
 printf("\ninsira o mes: ");
 scanf("%d", &mes);
 printf("\ninsira o ano: ");
 scanf("%d", &ano);
 printf("\ninsira a hora: ");
 scanf("%d", &hora);
 printf("\ninsira os minutos: ");
 scanf("%d", &minuto);
 printf("%d/%d/%d hora: %d:%d", dia, mes, ano, hora, minuto);
char c1, c2, c3;
printf("insira uma letra e tecle enter 3 vezes: ");
scanf("%c %c %c", &c1, &c2, &c3);
printf("%c%c%c", c1, c2, c3);
float nf1, nf2;
printf("insira um numero quebrado e tecle enter 2 vezes: ");
scanf("%f%f", &nf1, &nf2);
printf("%f, %f", nf2, nf1);
int numero3;
 printf("digite um numero de 3 digitos: ");
 scanf("%d", &numero3);
 int centena = numero3 / 100;
 int dezena = (numero3 / 10) % 10;
 int unidade = numero3 % 10;
 printf("Numero invertido: %d%d%d\n", unidade, dezena, centena);
return 0;
}