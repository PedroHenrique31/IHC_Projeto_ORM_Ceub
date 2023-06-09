from sqlalchemy.ext.automap import automap_base


class visualiza:
    # gera uma classe com um BD, opnde perfomamos as coisas
    def __init__(self, DB,ses):
        self.BancoDados = DB
        self.sessao=ses

    def menu(self):
        continuar = True
        while continuar:
            print('\n' * 12)
            print('CRUD de Serviços - MENU')
            print('1 - Incluir')
            print('2 - Consultar')
            print('3 - Alterar')
            print('4 - Excluir')
            print('5 - Sair')
            opc = input('Qual a sua opção? ')
            print("\n" * 30)
            if opc == '1':
                self.incluir()
            elif opc == '2':
                self.consultar()
            elif opc == '3':
                self.alterar()
            elif opc == '4':
                self.excluir()
            elif opc == '5':
                continuar = False
            else:
                print('Opção inválida')
                input()
        # Finalizando o programa


    ## Vamos colocar aqui as funcoes de CRUD
    def incluir(self):

        opcao = input("Selecione o que deseja incluir\n1-Aluno\n2-Disciplina\n3-Matricular aluno em disciplina\n")
        if opcao == '1':
            self.inserirAluno()
        else:
            print("Não entendi o que disse")

    def inserirAluno(self):

        aluno = self.BancoDados.classes.aluno # isso gera uma classe que representa a tablea aluno no banco
        novoAluno=aluno() # cria novo objeto do tipo aluno
        print(type(aluno))
        print("\n" * 30)
        print("Digite as informações a seguir")
        nome = input("Nome do aluno: ")
        nascimento = input("Data de nascimento do aluno: ")
        novoAluno.NOME=nome
        novoAluno.DATA_NASCIMENTO=nascimento
        self.sessao.add(novoAluno)# comando que escreve o insert
        self.sessao.commit()# envia a alateração para o banco

    def consultar(self):
        ALUNO=self.BancoDados.classes.aluno # cria objeto tabela de alunos
        alunos=self.sessao.query(ALUNO).all() # consulta tudo
        for alu in alunos:
            print('-------------------------------------------------------------------')
            print("Aluno ID: "+str(alu.COD)+" Nome: "+alu.NOME+" Data nascimento: "+str(alu.DATA_NASCIMENTO))
        input("Pressione [Enter] para voltar ao menu.")



    def alterar(self):
        #Mostra uma lista de alunos disponíveis
        alunos=self.sessao.query(self.BancoDados.classes.aluno).all()
        print("Alunos listados")
        for a in alunos:
            print("Aluno ID: "+str(a.COD)+" nome: "+a.NOME)
            print("---------------------------------------------------")
        id_aluno_alterar=int(input("Digite o número de ID do aluno selecionado: "))
        # Agora com o id do aluno vamos pegá-lo
        aluno_alterar=self.sessao.query(self.BancoDados.classes.aluno).filter_by(COD=id_aluno_alterar).first()
        aluno_alterar.NOME=input("Alterar nome [{}]: ".format(aluno_alterar.NOME))
        aluno_alterar.DATA_NASCIMENTO=input("Alterar data de nascimento [{}]: ".format(aluno_alterar.DATA_NASCIMENTO))
        self.sessao.commit() # pelo visto já faz o update
        input("Pressione [Enter] para voltar ao menu.")
    def excluir(self):
        #Mostra uma lista de alunos disponíveis
        alunos=self.sessao.query(self.BancoDados.classes.aluno).all()
        print("Alunos listados")
        for a in alunos:
            print("Aluno ID: "+str(a.COD)+" nome: "+a.NOME)
            print("---------------------------------------------------")
        id_aluno_alterar=int(input("Digite o número de ID do aluno que deseja excluir: "))
        # Agora vamos a exclusão
        tb_alunos=self.BancoDados.classes.aluno
        aluno_excluir=self.sessao.query(tb_alunos).filter(tb_alunos.COD==id_aluno_alterar)
        aluno_excluir.delete()
        self.sessao.commit()
        input("Pressione [Enter] para voltar ao menu.")

def incluirMatricula():
    pass


def inserirDisciplina():
    pass



