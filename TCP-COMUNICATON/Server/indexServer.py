#
# |@.1.0
# |autor: Limae
#
import threading
import socket

# |Declaração da lista de clientes 
clients = []

# |Variaves para registro
client_IP = []
cout = 0
# ip = input("Por favor coloque a Endereço IPv4 abaixo") 
#socket.gethostname()
# Pegar o ipLocal 

#| Função main
def main(): 
    # |Declaração do Socket 
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("\033[33m=====================================================================================")
    print("\033[1;32mVocê deu incio a um servidor de bate-papo")

    try:
        # |Declaração da porta e o ip do servidor
        server.bind(("localhost", 7777))
        server.listen()
    except:
        return print('\nNão foi possível iniciar o servidor!\n')

    while True:
        # |Loop infinito para sempre ficar escultando
        client, addr = server.accept()
        clients.append(client)

        print(f'\033[m Client logado com sucesso com ip: \033[1;33m{addr}')
        # print(cout)
        thread = threading.Thread(target=messagesTreatment, args=[client])
        thread.start()
        

        
        

def messagesTreatment(client):
    while True:
        try:
            msg = client.recv(2048)
            broadcast(msg, client)
        except:
            deleteClient(client)
            break
def broadcast(msg, client):
    for clientItem in clients:
        if clientItem != client:
            try:
                clientItem.send(msg)
            except:
                deleteClient(clientItem)


def deleteClient(client):
    clients.remove(client)

#| Rodando o programa
main()