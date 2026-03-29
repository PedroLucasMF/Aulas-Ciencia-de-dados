lista = [1,2,2,3,4,5,6,6,7]
listaUnica = list(dict.fromkeys(lista))
print(listaUnica)
##Filtragem de Dados: Dado que vocˆe possui uma lista L contendo elementos duplicados,
##qual a maneira logicamente mais eficiente de transform ́a-la em uma estrutura que contenha
##apenas valores  ́unicos?
matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matriz)
## matriz[2][2] = 0 ao se utilizar () para declarar os valores eles ficam imutaveis esta linha quando descomentada não rodaria.
print(matriz)
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Tentando buscar uma chave existente
value_a = my_dict.get('a')
print(f"Valor de 'a': {value_a}")

# Tentando buscar uma chave que não existe (retorna None por padrão)
value_d = my_dict.get('d')
print(f"Valor de 'd' (sem existir): {value_d}")

# Tentando buscar uma chave que não existe com um valor padrão
value_e = my_dict.get('e', 'Chave não encontrada')
print(f"Valor de 'e' (com valor padrão): {value_e}")

# Demonstrando o que aconteceria com acesso direto (comentado para evitar erro)
# try:
#     value_f = my_dict['f']
#     print(f"Valor de 'f': {value_f}")
# except KeyError as e:
#     print(f"Erro ao acessar 'f' diretamente: {e}")

frase = input("Digite uma frase: ")
qnt = 0
contador = 0
for _ in frase:
  qnt += 1
  if _ != " ":
        contador += 1

print("Sua frase tem ", qnt, " caracteres contado os espaços")
print("Sua frase tem ", contador, " caracteres sem os espaços")

#Contando a quantia de caracteres com e sem espaço, uma forma de contar direto é o len(frase).
#tabuada
numero = input("Diga um numero: ")
n = 0
while n <= 10:
  resultado = int(numero) * n
  print(numero, "x", n, "=", resultado)
  n += 1
  S = [10, 20, 30, 40, 50, 60]
print(S[1:5])
#atividade de sling
soma = 0
for i in range(5):
  numero = int(input("Digite um numero: "))
  soma += numero
print(soma)
#Acumulo de numeros
soma = 0
notas = int(input("Quantas notas voce quer digitar? "))
for i in range(notas):
  n = int(input("Digite uma nota: "))
  soma += n

print("A media é: ", soma / notas)
#MEdia com For
print("voce ira digitar 10 numeros")
m100 = 0
for i in range(10):
  n = int(input("Digite um numero: "))
  if n > 100:
    print(n, "è maior que 100")
    m100 += 1
print("Voce digitou ", m100, " numeros maiores que 100")
lista = []

for i in range(5):
  nome = input("Digite um nome: ")
  lista.append(nome) #envia o nome para a lista

print(lista)

#Preenchendo uma lista com input dentro do for
n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))
impar = 0

for n1 in range(n2):
  resto = n1 % 3
  if resto == 0:
    impar += 1
print("Entre ", n1, "e ", n2, "existem ", impar, " numeros impares")

#Verificação de numeros impares em um range dito pelo usuario
numero = int(input("Digite um numero: "))
resultado = 1

for i in range(numero, 0, -1):
    resultado *= i
    print(resultado)

print("O fatorial de", numero, "é", resultado)
#Fatorial
nomes = ["Ana", "Bruno", "Carlos", "Daniela", "Eduardo"]

busca = input("Digite um nome: ")

encontrado = False

for nome in nomes:
    if nome == busca:
        encontrado = True
        break

if encontrado:
    print("Nome encontrado na lista!")
else:
    print("Nome não encontrado.")

#Busca de nomes sem a utilização de in
