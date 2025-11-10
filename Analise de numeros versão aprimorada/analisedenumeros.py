print("Programa Impar ou Par")
par = 0
impar = 0
numeros_lista = []

for i in range (15):
    numeros = int(input(f"Digite o número {i+1}º número: "))
    numeros_lista.append(numeros)

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
input()