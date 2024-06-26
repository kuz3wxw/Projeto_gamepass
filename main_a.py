from usuarios import Usuario
from planos import planos_jogos


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

usuarios = []

def cadastrar():
    print('Crie uma conta e assine ja!')
    nome = input('Nome: ')
    senha = input('Senha: ')
    usuarios.append(Usuario(nome, senha))

def login():
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
    return False

def main():

    while True:
        print('Bem vindo!')
        print('1.Login')
        print('2.Cadastro')
        print('3.Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            ler_dados()
            login()
        elif opcao == '2':
            cadastrar()
            planos_jogos()

       
        elif opcao == '3':
            print('Saindo...')
            break
        else:
            print('Opcao invalida')

if __name__ == "__main__":
    main()


















