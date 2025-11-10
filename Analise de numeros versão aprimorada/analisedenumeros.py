print("Programa Impar ou Par")
par = 0
impar = 0
i = 1
numeros_lista = []

while i < 16:
    numeros = int(input(f"Digite o número {i}º número: "))
    if numeros in numeros_lista:
        print("Voce digitou um número repetido, tente novamente!")
        input("Aperte (Enter) para continuar")
        continue
    else:
        numeros_lista.append(numeros)
        i += 1
        continue

maior = max(numeros_lista)
menor = min(numeros_lista)
numeros_lista.sort()  #sort serve pra deixar em ordem crescente
print("\nLista em ordem crescente:")
print(numeros_lista) 

for numero in numeros_lista:
    if numero % 2 == 0:
        par += 1
    else:
        impar += 1

print("\nQuantidade de números pares: ", par)
print("Quantidade de números ímpares: ", impar)
print("O maior número da lista é: ", maior)
print("O menor número da lista é: ", menor)
input()