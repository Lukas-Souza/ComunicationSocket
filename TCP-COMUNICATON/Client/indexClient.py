#
# |@.1.0
# |autor: Limae
#
import threading
import socket
import os 
from datetime import datetime
import inteface 
def main():
    ChaveIp = input("Coloque o endereço IPv4 local do bate papo onde voce quer se conectar: \n")
    time = datetime.now()
    timeNow = time.strftime('%H:%M')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    global Data
    Data = time.strftime('%d/%m/%y')
    try:
        client.connect((ChaveIp, 7777))
    except:

        return print('\nNão foi possívvel se conectar ao servidor!\n')
    
    Val_username()
    inteface.inicialização(username, Data)

    print('Você se Conectadou ao chat')

    Texto = "oin"

    thread1 = threading.Thread(target=receiveMessages, args=[client])
    thread2 = threading.Thread(target=sendMessages, args=[client, username, timeNow, Data,Texto])

    thread1.start()
    thread2.start()

# 

def receiveMessages(client):
    while True:
        try:
            msg = client.recv(2048).decode('utf-8')
            print(msg +'\n')
            
            
        except:
            print('\nNão foi possível permanecer conectado no servidor!\n')
            print('Pressione <Enter> Para continuar...')
            client.close()
            break
            

def sendMessages(client, username, timeNow, Data, Texto):
    client.send(f'{timeNow}\033[37m|\033[32m{username}Entrou no chat...\033[m '.encode('utf-8'))
    while True:
        try:
            msg = input()
            if msg == "::exit":
                client.send(f'\033[1;33m{timeNow}\033[37m|\033[0;35m{username} saiu da Conversa com este nicknaname..\033[m\n'.encode('utf-8'))
                client.close()
                print("\033[1;35mVocê se desconectou da conversa por favor aperte tecla [ENTER] para continuar... \033[m\n")
                client.sendall(username.encode("utf-8"))
            elif msg == "::clear":
                os.system("cls")
                inteface.inicialização(username, Data)

            else:
                time = datetime.now()
                timeNow = time.strftime('%H:%M')
                client.send(f'\033[1;33m{timeNow}\033[37m|\033[0;35m{username}//\033[1;35m:\033[37m {msg}\033[m'.encode('utf-8'))

        except:
            return
        

def Val_username():
    global username
    username = input('\033[mDigite o nome que você quer ultilizar durante a conversa: \n')
    while username == "" or username == " ":

        print("\033[0;31mVocê digitou um nome invalido...\n")
        username = input('Por favor digite um nickename valido..\033[m\n')
        return username 

main()