
import time
from getpass import getpass
import stdiomask
import mysql.connector

def main_menu():
    print('''Bem-Vindos!
        Escolha uma Opção:
        (1) Fazer login 
        (2) Cadastro
        (3) Sair
        ''')
    otion = int(input('Opçao: '))
    return (otion)

def login():
    UserName =  input ('Digite o usuario: ')
    password =  stdiomask.getpass ('Digite a senha: ', mask='*')
    return (UserName, password)



while True:

    option = main_menu()

    if option == 1:
        #login
        UserName, password = login()

        con = mysql.connector.connect(host='localhost',
        database='user', user= 'root', password='')
        cur = con.cursor()
        cur.execute(f"""SELECT TOKEN from usuarios WHERE TOKEN='{UserName}' AND SENHA= '{password}';
        """)

        if cur.fetchone():
            print ('login aprovado!')
            cur.close()
            con.close()
            print('conexão encerrada')
            exit()
            
        else:
            print ('Verifique as cedenciais e tente novamente')
            time.sleep(3)


    if option == 2:
        #cadastro
        UserName, password = login()

        con = mysql.connector.connect(host='localhost',
        database='user', user= 'root', password='')

        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS usuarios(
                     TOKEN VARCHAR(30),
                     SENHA VARCHAR (30)
                           
               );            """)

        if UserName == password:
            print ('A senha e o usário devem ser diferentes')
            time.sleep(3)
        
        else:
            cur = con.cursor()
            cur.execute("""INSERT INTO usuarios
                (TOKEN, SENHA)
                VALUES
                (%s, %s)""", (UserName, password))
                
            print ('Cadastro com sucesso!')
            cur.close()
            con.close()
            print('conexão encerrada')
            exit()
        
    if option == 3:
        print('Adeus!')
        exit()
    
    else:
        print('Opção incorrta, tente novamente!')
        time.sleep(3)


    













