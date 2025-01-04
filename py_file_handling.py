import os


def create_file(path, content):
    with open(path, "w") as file:
        file.write(content)
    print(f"Arquivo criado com o conteúdo: {content}")
    return path  


def read_file(path):
    try:
        with open(path, "r") as file:
            content = file.read()
        print("Conteúdo do arquivo:")
        print(content)
    except FileNotFoundError:
        print("Arquivo não encontrado!")


def update_file(path, content):
    with open(path, "a") as file:
        file.write(content + "\n")
    print(f"Conteúdo '{content}' adicionado ao arquivo.")


def find_and_replace(path, target, replacement):
    try:
        with open(path, "r") as file:
            content = file.read()
        
        new_content = content.replace(target, replacement)
        
        with open(path, "w") as file:
            file.write(new_content)
        
        print(f"'{target}' foi substituído por '{replacement}'.")
    except FileNotFoundError:
        print("Arquivo não encontrado para substituição!")


def delete_file(path):
    try:
        os.remove(path)
        print(f"Arquivo '{path}' excluído com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado para exclusão!")
    except PermissionError:
        print("Sem permissão para excluir o arquivo.")


file_path = r"D:\Github\Python\basic-lib-python\texto2.txt"

create_file(file_path, "Primeira linha.\nSegunda linha.\nTerceira linha.")

read_file(file_path)

update_file(file_path, "Quarta linha adicionada.")
update_file(file_path, "Quinta linha adicionada.")

find_and_replace(file_path, "Segunda", "Outra")
read_file(file_path)

delete_file(file_path)
read_file(file_path)

input()
