from Aluno import Aluno
from Funcionario2 import Funcionario2
from Pessoa import Pessoa
from Funcionario import Funcionario
from Retangulo import Retangulo


def q1():
    nome = input('Digite seu nome\n')
    idade = input('Digite sua idade\n')
    nome2 = input('Digite seu nome\n')
    idade2 = input('digite sua idade\n')
    p1 = Pessoa(nome, idade)
    p2 = Pessoa(nome2, idade2)
    calculaIdade(p1, p2)

def calculaIdade(p1, p2):
    if p1.idade > p2.idade:
        print(p1.nome + " é o mais velho")
    elif p2.idade > p1.idade:
        print(p2.nome + " é o mais velho")
    else:
        print('idades iguais')

def q2():
    nome = input("digite seu nome\n")
    salario1 = float(input("Digite seu salario\n"))
    nome2 = input("digite seu nome\n")
    salario2 = float(input("Digite seu salario\n"))
    f1 = Funcionario(nome, salario1)
    f2 = Funcionario(nome2, salario2)
    calculaMedia(f1, f2)

def calculaMedia(f1, f2):
    media = (f1.salario + f2.salario) / 2
    print('A média é ' + str(media))

def q3():
    largura = float(input("digite a largura do Retangulo\n"))
    altura = float(input("Digite a altura do Retangulo\n"))
    r1 =  Retangulo(largura, altura)
    print('A area do Retangulo é: ' +  str(r1.area()))
    print('O perimetro do Retangulo é: ' + str(r1.perimetro()))
    print('A diagonal Do Retangulo é: ' + str(r1.diagonal()))

def q4():
    nome = input("digite seu nome: \n")
    salario = float(input("Digite seu salario: \n"))
    imposto = float(input('Digite o Imposto: \n'))
    porcentagem = float(input('Digite a porcentagem: \n'))
    f1 = Funcionario2(nome, salario, imposto, porcentagem)
    f1.Dados()
    f1.DadosAtualizados()

def q5():
    nome = input('Digite o nome do aluno\n')
    nota1 = float(input('Digite a primeira nota\n'))
    nota2 = float(input('Digite a segunda nota\n'))
    nota3 = float(input('Digite a terceira nota\n'))
    a1 = Aluno(nome, nota1, nota2, nota3)
    a1.CalculoNota()


def function1():
    print("Quem é mais velho selecionado")
    q1()

def function2():
    print("Media de Salario")
    q2()
    
def function3():
    print("Area, Perimetro e Diagonal do Retangulo selecionado")
    q3()
    
def function4():
    print("Salario com Impostos selecionado")
    q4()
    
def function5():
    print("Aprovação anual selecionado")
    q5()

def default():
    print("Numero Invalido")

if __name__ == "__main__":
    switch = {
        "1": function1,
        "2": function2,
        "3": function3,
        "4": function4,
        "5": function5
    }

    print('Menu: \n 1: Quem é mais velho \n 2: Media de Salario \n 3: Area, Perimetro e Diagonal do Retangulo \n 4: Salario com Impostos \n 5: Aprovação anual \n')

    numero = input('Escolha uma opção: ')

    case = switch.get(numero, default)
    case()
