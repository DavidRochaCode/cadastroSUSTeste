import psycopg2
from bd import *


#configuracao

#-----------------------------------------------------------------------------------------------------
hostname = 'localhost'
database = 'ubs'
username = 'postgres'
pwd = 'alaska'
port_id = 5432
conn = None
cur = None
try:
    conn = psycopg2.connect(
        host = hostname,
        dbname = database,
        user = username,
        password = pwd,
        port = port_id
    ) 
    cur = conn.cursor()

    #fim da configuracao

    #INSERIR O CODIGO SQL AQUI


    #--------criar tabela------------#

    def criar_tabela():
        cur.execute(nomes)
      

    criar_tabela()

    #--------inserir valores na tabela --#
    
    def inserir_na_tabela():
        try:
            print("\n")
            nome_tabela = input("qual tabela adicionar?: ")
            print("\n")
            id_pessoa = input("ID da pessoa: ")
            print("\n")
            nome_pessoa = input("Nome da pessoa: ")
            print("\n")
            idade_pessoa = input("Idade da pessoa: ")
            print("\n")
            cur.execute ("INSERT INTO " +nome_tabela+"(id, nome, age) VALUES(%s,%s,%s);",(id_pessoa, nome_pessoa, idade_pessoa))   
            conn.commit()
            again = input("Gostaria de adicionar mais nomes? 1 - SIM | 2 - NAO:  ")
            print("\n")
            while again == "1":
                inserir_na_tabela()
                print("\n")
                again = input("Gostaria de adicionar mais nomes? 1 - SIM | 2 - NAO:  ")
        except: 
            print("O usuario ja existe no sistema.")
 # ------ Imprimir bd ------------#
    def imprimir_tabela():
        print("\n")
        tb_nome = input("De qual tabela imprimir?: ")
        cur.execute("SELECT * FROM {0} ORDER BY id".format(tb_nome))
        for record in cur.fetchall():
            print("---------------------------------------")
            print(" | Id: {0} |  Nome: {1} |  Idade: {2} |".format(record[0],record[1],record[2]))
            print("---------------------------------------")          

#--------consultar tabela------------#
     
    def consultar_tabela():
        try:
            print("\n")
            pessoa_nome = input("Qual tabela consultar?: ")
            print("\n")
            pessoa_id = input("Qual o id da pessoa?: ")
            cur.execute("SELECT * FROM {0} WHERE id = {1}".format(pessoa_nome,pessoa_id))
            for record2 in cur.fetchall():
                print("\n")
                print("---------------------------------------")
                print(" | Id: {0} |  Nome: {1} |  Idade: {2} |".format(record2[0],record2[1],record2[2]))
                print("---------------------------------------")
        except:
            print("\n")
            print("Pessoa nao encontrada")

# ---------deletar tabela-------- (testar)---#

    def apagar_tabela():
        print("\n")
        qual_apagar = input("De qual tabela apagar?: ")
        id_apagar = input("Qual o id da pessoa?: ")
        cur.execute("DELETE FROM {0} WHERE id = {1};".format(qual_apagar,id_apagar))
        conn.commit()
        print("Elemento apagado")

    def update_table():
        tabela_update = input("De qual tabela vai alterar?: ")
        mudar_update = input("Qual elemento mudar?: ")
        id_update = input("Qual o id do elemento: ")
        wt_update = input("Pelo o que voce quer mudar?: ")
        cur.execute("UPDATE {0} SET {1} = '{2}' WHERE id = {3};".format(tabela_update,mudar_update,wt_update,id_update))
        conn.commit()
        


    # ------ Pagina Inicial----------#
    def inicial_page():
        print("\n")
        print("---------- BANCO DE DADOS DA UBS ---------- \n")
        print("Nessa tabela voce pode:\n")
        print("1-Consultar BD | 2-Add no BD | 3-Remover do BD | 4-consultar BD extendido | 5 - Atualizar BD")
        print("\n")
        escolha = int(input("O que voce gostaria de fazer?: "))

        if escolha == 1:
            consultar_tabela()
        elif escolha == 2:
            inserir_na_tabela()
        elif escolha == 3:
            apagar_tabela()
        elif escolha == 4:
            imprimir_tabela()
        elif escolha == 5:
            update_table()
        
        else:
            print("Desculpa, nao entendi.")
    inicial_page()
    
# --------------------------------------------------------------
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()