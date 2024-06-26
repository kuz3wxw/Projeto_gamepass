class Usuario:
    def __init__(self, nome, senha, plano):
        self.nome = nome
        self.senha = senha
        self.plano = plano
    def __repr__(self):
        return f'{self.nome}, {self.senha}, {self.plano}'
    
    def from_string(user_str):
        nome, senha, plano = user_str.split(',')
        return Usuario(nome, senha, plano)