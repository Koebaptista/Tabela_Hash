# Criando uma tabela hash usando um dicionário em Python
tabela_hash = {}

# Função para adicionar uma pessoa na tabela hash
def adicionar_pessoa(nome, idade):
    tabela_hash[nome] = idade
    print(f"{nome} foi adicionado com a idade {idade}.")

# Função para buscar a idade de uma pessoa na tabela hash
def buscar_idade(nome):
    if nome in tabela_hash:
        return f"A idade de {nome} é {tabela_hash[nome]}."
    else:
        return f"{nome} não está na tabela hash."

# Função para remover uma pessoa da tabela hash
def remover_pessoa(nome):
    if nome in tabela_hash:
        del tabela_hash[nome]
        print(f"{nome} foi removido da tabela hash.")
    else:
        print(f"{nome} não está na tabela hash para ser removido.")

# Função principal que executa o código
def main():
    # Adicionando algumas pessoas
    adicionar_pessoa("Alice", 30)
    adicionar_pessoa("Bob", 25)
    adicionar_pessoa("Charlie", 35)

    # Buscando idades
    print(buscar_idade("Alice"))
    print(buscar_idade("Bob"))
    print(buscar_idade("David"))  # Não está na tabela

    # Removendo uma pessoa
    remover_pessoa("Charlie")

    # Tentando buscar uma pessoa removida
    print(buscar_idade("Charlie"))

# Bloco que garante que o código só será executado se o arquivo for rodado diretamente
if __name__ == "__main__":
    main()
