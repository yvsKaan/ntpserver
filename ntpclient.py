import os
import socket

host_address = input('Host address input:')
port_address = input('Port address input:')
serverAddress = (host_address, int(port_address))
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
            os.system('sudo timedatectl set-time '+ msg.split()[0]+ msg.split()[1])
            print("System Date/Time Changed.")

except Exception as e:
    print(e)


