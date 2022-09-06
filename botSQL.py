import os
import requests
import mysql.connector
from config import userSite, senhaSite, senhaSQL, siteLogin, idInicial, idFinal, siteAcesso


#Conectando ao Banco de Dados

con = mysql.connector.connect(  host='localhost',
                                database='idSIGA',
                                user='root',
                                password=senhaSQL)

if con.is_connected():
    db_info = con.get_server_info()
    print("Conectado ao servidor MySQL versão", db_info)
    cursor = con.cursor()
    cursor.execute('select database();')
    linha = cursor.fetchone()
    print('Conectado ao banco de dados', linha)



#Logando no site a ser varrido

with requests.session() as s:
    s.post(siteLogin, data={'login': userSite, 'password': senhaSite})
    s.get(siteAcesso)

    for id in range(idInicial, idFinal):

        rInfo = s.get(siteDados)
        nomeDoc = f'arquivos/Aluno - {id}.txt'

        if rInfo.status_code == requests.codes.OK:
        
            with open(nomeDoc,'wb') as novoArquivo:
                novoArquivo.write(rInfo.content)
                print(f"Documento salvo em {nomeDoc}")

            with open(nomeDoc,'r',encoding='iso8859-1') as arquivo:
                texto = arquivo.readlines()
                for linha in texto:
                    if "grr" in linha:
                        sep1 = linha.split('grr')[1]
                        sep2 = linha.split('grr')[0]
                        idCurriculo = sep2.split('\"')[8].replace(':', '').replace(',', '')
                        status = sep1.split('\"')[24]
                        grr = sep1.split('\"')[2]
                        idCurso = sep1.split('\"')[5].replace(':', '').replace(',', '')
                        nome = sep1.split('\"')[12]

                comando = f"""INSERT INTO idSIGA(idSIGA, idCurso, idCurriculo, grr, nome, status)
                            VALUES
                            ({id}, {idCurso}, {idCurriculo}, '{grr}', '{nome}', '{status}')"""

                cursor.execute(comando)
                con.commit()
                print(f'ID {id} inserido no banco de dados')
                
        os.remove(nomedoc)


        else:
            rInfo.raise_for_status()



#Encerrando a conexão do Banco de Dados MySQL

cursor.close()
con.close()
print('Conexão ao MySQL encerrada')



