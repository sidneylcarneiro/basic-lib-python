
```markdown
# Projeto Python - Exemplos de Funcionalidades

Este repositório contém diversos exemplos de código Python que demonstram funcionalidades específicas,
incluindo manipulação de arquivos, geração de números aleatórios,
manipulação de data e hora, e muito mais.
O objetivo deste repositório é fornecer exemplos práticos de como usar algumas das bibliotecas padrão do Python.

## Estrutura do Projeto

Os arquivos Python no repositório são organizados conforme descrito abaixo:

### 1. `py_datetime.py`
Este script demonstra como trabalhar com datas e horas no Python utilizando o módulo `datetime`. Ele inclui exemplos de como:
- Obter a data e hora atual.
- Realizar operações com datas (como adicionar dias).
- Calcular atrasos com base em datas.
- Trabalhar com diferentes formatos de data.

#### Funcionalidades:
- Obtenção da data e hora atual.
- Conversão de data para diferentes formatos.
- Cálculo de atrasos entre datas.

### 2. `py_file_handling.py`
Este script demonstra operações básicas de manipulação de arquivos no Python utilizando o módulo `os`. Ele mostra como:
- Criar, ler, atualizar e excluir arquivos.
- Substituir conteúdo em arquivos.
- Listar diretórios e criar novas pastas.

#### Funcionalidades:
- Criação e leitura de arquivos.
- Atualização e substituição de conteúdo em arquivos.
- Exclusão de arquivos.
- Criação de diretórios.

### 3. `py_math.py`
Este script mostra como realizar operações matemáticas utilizando o módulo `math` do Python. Inclui exemplos de como:
- Calcular raízes quadradas, valores absolutos e fatoriais.
- Realizar operações como logaritmos e exponenciação.
- Arredondar números para cima ou para baixo.

#### Funcionalidades:
- Cálculo de raízes quadradas e logaritmos.
- Cálculo de fatorial e valor absoluto.
- Arredondamento de números.

### 4. `py_os.py`
Este script demonstra como trabalhar com o sistema operacional no Python, utilizando o módulo `os`. Ele mostra como:
- Obter informações sobre o sistema, como o nome de usuário e diretório atual.
- Mudar de diretório.
- Criar e remover pastas.

#### Funcionalidades:
- Obtenção de informações do sistema.
- Navegação entre diretórios.
- Criação e remoção de pastas.

### 5. `py_random.py`
Este script demonstra como gerar números aleatórios no Python, utilizando o módulo `random`. Ele inclui exemplos de como:
- Realizar sorteios aleatórios de números únicos e repetidos.
- Gerar números aleatórios entre 0 e 1.
- Embaralhar listas.

#### Funcionalidades:
- Sorteio de números aleatórios.
- Geração de números entre 0 e 1.
- Embaralhamento de listas.

### 6. `py_zoneinfo.py`
Este script demonstra como trabalhar com fusos horários utilizando o módulo `zoneinfo` no Python. Ele inclui exemplos de como:
- Converter a hora local para um fuso horário específico.
- Trabalhar com fusos horários de diferentes regiões.

#### Funcionalidades:
- Conversão de hora para diferentes fusos horários.
- Listagem de fusos horários disponíveis.

## Requisitos
- Python 3.9 ou superior.
- Para fusos horários, o módulo `zoneinfo` pode precisar da instalação do pacote `tzdata` (especialmente em sistemas Windows).

### Instalação do `tzdata` (se necessário)
Se estiver usando uma versão do Python anterior a 3.9, ou se o módulo `zoneinfo` não estiver funcionando corretamente, você pode precisar instalar a dependência `tzdata`:
```bash
pip install tzdata
```

## Como Usar
1. Clone o repositório:
    ```bash
    git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd SEU_REPOSITORIO
    ```

3. Execute os arquivos Python desejados. Exemplo:
    ```bash
    python py_datetime.py
    ```

## Contribuições
Sinta-se à vontade para fazer melhorias neste repositório! Se encontrar algum bug ou desejar adicionar novos exemplos, fique à vontade para abrir uma *issue* ou submeter um *pull request*.

---

### Considerações
- **Exemplos Simples**: Cada arquivo Python neste repositório oferece exemplos simples e diretos, com explicações claras sobre a funcionalidade demonstrada.
- **Modularidade**: Cada arquivo foca em uma funcionalidade específica, facilitando a manutenção e compreensão.

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
```
