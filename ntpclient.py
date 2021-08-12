import platform
import socket
import click
import subprocess
import ntplib

class Client:    
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.op_system = platform.system()

    def run(self):
        if self.host == None : self.host = input('Host address input:')
        if self.port == None : self.port = input('Port address input:')
        
        serverAddress = (self.host, int(self.port))
        bufferSize = 1024

        try:
            UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

            while True:
                clientMessage = input("Enter your command:")
                if clientMessage == "exit":
                    break

                if clientMessage == "time":
                    bytesToSend = str.encode(clientMessage)

                    UDPServerSocket.sendto(bytesToSend, serverAddress)

                    serverMessage = UDPServerSocket.recvfrom(bufferSize)

                    msg = serverMessage[0].decode()
                
                    print("Server response: " + msg)

                    if msg:
                        is_Change = input('Do you want to change the time with Server time? Y/N:')
                        if is_Change.lower() == 'y' and self.op_system == "Linux":
                            subprocess.run(["sudo timedatectl set-time " + msg.split()[0]], shell= True) # For date
                            subprocess.run(["sudo timedatectl set-time " + msg.split()[1]], shell= True) # For time
                            print("System Date/Time Changed.")
                        if is_Change.lower() == 'y' and self.op_system != "Linux":
                            print("Sorry, only Linux Operation System can change time")

        except Exception as e:
            print(e)


@click.command()
@click.option('--host', help='Your Host Address', default=None)
@click.option('--port', help="Your Port Address", default=None)
def cli(host, port):
    try:
        ntplib.NTPClient().request(host= host)
        client = Client(host, port)
        client.run()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    cli()
