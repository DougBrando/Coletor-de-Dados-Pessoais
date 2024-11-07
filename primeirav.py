# Inicializa variáveis para armazenar a soma das idades, a média, a maior idade de um homem e o nome do homem mais velho
somaidade = 0
maioridadehomem = 0
nomevelo = ''
num_pessoas = 3  # Número de pessoas a serem registradas

# Loop para coletar informações de 'num_pessoas'
for p in range(1, num_pessoas + 1):
    print('------ {}ª pessoa -----'.format(p))  # Exibe o número da pessoa que está sendo registrada
    
    # Solicita a idade da pessoa e garante que seja um número positivo
    while True:
        try:
            idade = int(input('Idade: '))
            if idade < 0:
                print("Por favor, insira uma idade válida (número positivo).")
                continue
            break
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")

    nome = str(input('Nome: ')).strip()  # Solicita o nome da pessoa e remove espaços em branco
    s = str(input('F/M: ')).strip().upper()  # Solicita o gênero da pessoa (F ou M) e remove espaços em branco

    somaidade += idade  # Adiciona a idade da pessoa à soma total das idades

    # Se for a primeira pessoa e o gênero for masculino, armazena a idade e o nome
    if p == 1 and s == 'M':
        maioridadehomem = idade  # Define a maior idade do homem como a idade da primeira pessoa
        nomevelo = nome  # Armazena o nome do homem mais velho

    # Se o gênero for masculino e a idade for maior que a maior idade registrada, atualiza os valores
    if s == 'M' and idade > maioridadehomem:
        maioridadehomem = idade  # Atualiza a maior idade do homem
        nomevelo = nome  # Atualiza o nome do homem mais velho

# Calcula a média das idades
media = somaidade / num_pessoas

# Exibe a média das idades
print('A média é {:.1f}'.format(media))

# Exibe a maior idade de um homem e seu nome
if maioridadehomem > 0:
    print('O homem mais velho tem {} anos e se chama {}'.format(maioridadehomem, nomevelo))
else:
    print('Nenhum homem foi registrado.')
