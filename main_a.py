from usuarios import Usuario
from planos import planos_jogos




def ler_dados():
    usuarios = []
    plano = []
    try:
        with open('dados.txt', 'r') as file:
            for line in file:
                line = line.strip()
                if line.startswith('usuario:'):
                    user_data = line.split('usuario: ')[1]
                    usuarios.append(Usuario.from_string(user_data))
                elif line.startswith('tarefa:'):
                    task_data = line.split('tarefa: ')[1]
                    plano.append(Usuario.from_string(task_data))
            
    except FileNotFoundError:
        pass
    return usuarios, plano


plano = []

def cadastrar(usuarios):
    print('Crie uma conta e assine ja!')
    nome = input('Nome: ')
    senha = input('Senha: ')
    usuarios.append(Usuario(nome, senha, plano))

def salvar_cadastro(usuarios):
    with open('C:/Users/182400218/Desktop/Nova pasta/dados.txt', 'a') as file:
        for user in usuarios:
            file.write(f'usuario: {user}\n')
            for task in plano:
               file.write(f'plano: {task}\n')

usuarios=[]

def login():
    nome = input("Nome de usuário: ")
    senha = input("Senha: ")
    for user in usuarios:
        if user.nome == nome and user.senha == senha:
            return True
   
    return False

def ver_plano():
     with open('C:/Users/182400218/Desktop/Nova pasta/dados.txt', 'r') as file: 
        for i in ler_dados():
            if i.plano == "1":
                print('Bronze')
            elif i.plano == "2":
               print('Prata')
            elif i.plano == "3":
                print("Ouro")
    
def main():
    usuarios , plano = ler_dados()
    while True:
        print('Bem vindo!')
        print('1.Login')
        print('2.Cadastro')
        print('3.Salvar dados')
        print('4.Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            ler_dados()
            login()
            ver_plano()
            
        elif opcao == '2':
            cadastrar(usuarios)
          
            planos_jogos()
            pagamento()

        elif opcao =='3':
            salvar_cadastro(usuarios)
            print('dados salvos...')
        
        elif opcao == '4':
            print('Saindo...')
            break
        else:
            print('Opcao invalida')

def pagamento():

    print("Efetue o pagamento com o cartão")

    cartao = input("Digite o numero do cartão:")
    cvc = input("Digite o cvc:")
    print("Compra efetuada com sucesso")

    return 


if __name__ == "__main__":
    main()


















