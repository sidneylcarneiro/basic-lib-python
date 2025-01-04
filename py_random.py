from random import sample, random, choice, choices, shuffle

options = list(range(0, 101))

sorteados = sample(options, 3)
print("Primeiro sorteio:", sorteados)

#segundo parâmetro é k = 3
sorteados = sample(options, 3)
print("Segundo sorteio:", sorteados)

input()

for x in range(11):
    print(f"Sorteio {x}:", sample(options, 3))

input()
lista = []
for x in range(3):
    numero_aleatorio = random()
    print("Numero aleatorio entre 0 e 1 decimal:", numero_aleatorio)
    lista.append(numero_aleatorio)
    input()

print("lista:", lista)

input()
nova_lista = list(range(0,101))
print("choice() e choices()", nova_lista)
for x in range(3):
    choice_aleatorio = choice(nova_lista)
    choices_aleatorio = choices(nova_lista, k=3)

    print("Numero aleatorio usando choice() da lista:", choice_aleatorio)    
    print("Numero aleatorio usando choices() 3 números da lista:", choices_aleatorio)
    input("Enter próximo número")

# Embaralhar a lista
shuffle(nova_lista)
print("\nLista embaralhada:", nova_lista)

input("Enter para sair")

