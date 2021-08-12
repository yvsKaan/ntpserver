import os
import socket
import click

@click.command()
@click.option('--host', help='Your Host Address', default=None)
@click.option('--port', help="Your Port Address", default=None)

def client(host,port):
    if host == None : host = input('Host address input:')
    if port == None : port = input('Port address input:')
    
    serverAddress = (host, int(port))
    bufferSize = 1024

    try:
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        while True:
            clientMessage = input("Enter your command:")
            if clientMessage == "exit":
                break

            bytesToSend = str.encode(clientMessage)

            UDPServerSocket.sendto(bytesToSend, serverAddress)

            serverMessage = UDPServerSocket.recvfrom(bufferSize)

            msg = serverMessage[0].decode()
            
            print("Server response: " + msg)

            if clientMessage == "time" and msg:
                is_Change = input('Do you want to change the time with Server time? Y/N:')
                if is_Change.lower() == 'y':
                    os.system('sudo timedatectl set-time '+ msg.split()[0]+ msg.split()[1])
                    print("System Date/Time Changed.")

    except Exception as e:
        print(e)

if __name__ == '__main__':
    client()

