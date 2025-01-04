import os

sistema = os.environ
"""
for item, value in sistema.items():
    print(item, value)
    input()
"""
print("imprime o nome do usuário do sistema")
print(sistema['USERNAME'])
input()

#print()
print("imprime o diretório do programa atual")
print(os.getcwd())
input()

print("muda o caminho para USERPROFILE")
novoCaminho = r"c:\windows"
os.chdir(sistema['USERPROFILE']) 
input()
print("imprime o diretório do programa atual alterado")
print(os.getcwd())
input()

try:
    list_dir = os.listdir()
    if "nova_pasta" not in list_dir:
        os.mkdir("nova_pasta")
    list_dir = os.listdir()  # Refresh the list
    print(list_dir)
except OSError as e:
    print(f"Error creating directory: {e}")
input()
print(list_dir)
input()
print("Comando rmdir() só remove pastas vazias")
input()

try:
    os.chdir(os.environ['USERPROFILE'] + r"\nova_pasta")
    list_dir = os.listdir()
    print(list_dir)
    print("imprime o diretório do programa atual alterado")
except FileNotFoundError:
    print("O diretório nova_pasta não existe.")
except OSError as e:
    print(f"Erro ao mudar de diretório: {e}")
input()




