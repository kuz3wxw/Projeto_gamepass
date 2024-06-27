from usuarios import Usuario

# Função para ler dados dos usuários a partir de um arquivo
def ler_dados():
    usuarios = []
    try:
        with open('dados.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('usuario:'):
                    user_data = line.split('usuario: ')[1]
                    usuarios.append(Usuario.from_string(user_data))
    except FileNotFoundError:
        pass
    return usuarios

# Função para verificar se um usuário já existe
def usuario_existe(usuarios, nome, senha):
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
    return False

# Função para cadastrar um novo usuário
def cadastrar(usuarios):
    print('\nCrie uma conta e assine já!')
    while True:
        nome = input('Nome: ')
        senha = input('Senha: ')

        if usuario_existe(usuarios, nome, senha):
            print('Usuário já cadastrado com esse nome e senha. Por favor, escolha outro nome e senha.')
        else:
            plano_escolhido = planos_jogos()
            usuario = Usuario(nome, senha, plano_escolhido)
            usuarios.append(usuario)
            print('\nCadastro realizado com sucesso!')
            return usuario

# Função para salvar o cadastro dos usuários em um arquivo
def salvar_cadastro(usuarios):
    with open('dados.txt', 'w') as file:
        for user in usuarios:
            file.write(f'usuario: {user}\n')

# Função para fazer login
def login(usuarios):
    nome = input("\nNome de usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            print('\nLogin bem-sucedido!')
            print(f'Olá, {user.nome}!')
            print(f'Plano escolhido: {user.plano}\n')
            return True
    print('\nNome de usuário ou senha incorretos.\n')
    return False

# Função para efetuar o pagamento
def pagamento():
    while True:
        print("\nEfetue o pagamento com o cartão")
        cartao = input("Digite o número do cartão:")  # Remova int()
        cvc = input("Digite o cvc:")  # Remova int()

        if cartao.isdigit() and cvc.isdigit():
            print("Cartão e CVC válidos.\n")
            break
        else:
            print("Entrada inválida. Por favor, digite apenas números.\n")

# Função para escolher o plano de jogos
def planos_jogos():
    print("\nBem-vindo ao catálogo de jogos!")
    print("Agora vamos escolher um plano ideal para você!")
    print("Esses são os planos disponíveis:")
    
    print("""
    Bronze:
    Assassin's Creed Rogue Remastered
    Bee Simulator
    Ben 10: Power Trip
    Celeste
    Just Cause 4
    Killing Floor 2
    NBA 2K24 Kobe Bryant Edition for PS4™
    SAMURAI WARRIORS 5
    Teardown
    UNCHARTED 4: A Thief’s End
    Valiant Hearts: The Great War™
    
    R$ 50,00
    """)
    
    print("""
    Prata:
    A Hat in Time
    Bee Simulator
    Ben 10: Power Trip
    Cat Quest II
    Celeste
    Chess Ultra
    Dark Rose Valkyrie
    DAVE THE DIVER
    Eagle Flight
    Earth Defense Force 4.1: The Shadow of New Despair
    D BROTHERS
    Fade to Silence
    FAR CRY 3: BLOOD DRAGON CLASSIC EDITION
    Get Even
    Ghost of Tsushima DIRECTOR’S CUT (PlayStation Plus)
    Hardspace: Shipbreaker
    Harvest Moon: Mad Dash
    Immortals Fenyx Rising™ PS4 & PS5
    Journey To The Savage Planet: Employee Of The Month
    JUMANJI: The Video Game
    Kena: Bridge of Spirits PS4 & PS5
    Killing Floor 2
    Lawn Mowing Simulator: Landmark Edition
    NBA 2K24 Kobe Bryant Edition for PS4™
    Observer: System Redux
    Paradise Killer
    PAW Patrol Mighty Pups Save Adventure Bay
    Rabbids® Invasion
    Sackboy: A Big Adventure PS4 & PS5
    Salt and Sacrifice
    Tails Noir
    Tales of Arise PS4 & PS5
    UNCHARTED: The Lost Legacy
    Undertale
    
    R$ 80,00
    """)
    
    print("""
    Ouro:
    Observer: System Redux
    Paradise Killer
    PAW Patrol Mighty Pups Save Adventure Bay
    Rabbids® Invasion
    Sackboy: A Big Adventure PS4 & PS5
    Salt and Sacrifice
    Tails Noir
    Tales of Arise PS4 & PS5
    UNCHARTED: The Lost Legacy
    Undertale
    A Hat in Time
    Bee Simulator
    Ben 10: Power Trip
    Cat Quest II
    Celeste
    Chess Ultra
    Dark Rose Valkyrie
    DAVE THE DIVER
    Eagle Flight
    Earth Defense Force 4.1: The Shadow of New Despair
    Observer: System Redux
    ODDBALLERS
    Oddworld: New 'n' Tasty
    Oddworld: Soulstorm Enhanced Edition
    Odin Sphere Leifthrasir
    The Elder Scrolls V: Skyrim Special Edition - PS5 & PS4
    The Evil Within
    The Evil Within 2
    The Fisherman - Fishing Planet
    The Forgotten City
    The Gardens Between
    The Last Guardian
    TRON RUN/r
    Tropico 5
    Two Point Hospital: JUMBO Edition
    Two Point Hospital™
    
    R$ 150,00
    """)
    
    while True:
        plano = input('Digite o número do plano desejado: 1-Bronze / 2-Prata / 3-Ouro: ')
    
        if plano == '1':
            return 'Bronze'
        elif plano == '2':
            return 'Prata'
        elif plano == '3':
            return 'Ouro'
        else:
            print('Erro, tente novamente')

# Função principal
def main():
    usuarios = ler_dados()
    while True:
        print('\nBem-vindo!')
        print('1. Login')
        print('2. Cadastro')
        print('3. Salvar dados')
        print('4. Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            login(usuarios)
        elif opcao == '2':
            cadastrar(usuarios)
            salvar_cadastro(usuarios)  # Salva o cadastro após cadastrar um novo usuário
            pagamento()  # Exemplo de pagamento após o cadastro, pode ser ajustado conforme necessário
        elif opcao == '3':
            salvar_cadastro(usuarios)
            print('\nDados salvos...')
        elif opcao == '4':
            print('\nSaindo...')
            break
        else:
            print('\nOpção inválida')

if __name__ == "__main__":
    main()
