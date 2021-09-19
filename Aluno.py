class Aluno():
    def __init__(self, nome, nota1, nota2, nota3):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3
        
    
    def CalculoNota(self):
        notaFinal = float(self.nota1) + float(self.nota2) + float(self.nota3) 
        print('\nNota Final ' + str(notaFinal) + '')
        if float(notaFinal) < 60 :
            print('REPROVADO')
            resto =  60 - notaFinal
            print('Faltaram ' + str(resto) + ' Pontos\n');
        else:
            print('APROVADO\n')
        
        

