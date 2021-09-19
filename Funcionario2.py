class Funcionario2():
    def __init__(self, nome, salarioBruto, imposto, porcentagem):
        self.nome = nome   
        self.salarioBruto = salarioBruto 
        self.imposto = imposto
        self.porcentagem = porcentagem

      
    def Dados(self):
        salario = self.salarioBruto - self.imposto
        print ('Funcionario: ' + self.nome + ', ' + 'R$' + str(salario))
    
    def DadosAtualizados(self):
        salarioFinal = self.salarioBruto + self.salarioBruto * (self.porcentagem / 100) 
        salarioFinal = salarioFinal - self.imposto     
        print('Dados Atualizados: ' + self.nome + '. ' + 'R$' + str(salarioFinal))
        



        