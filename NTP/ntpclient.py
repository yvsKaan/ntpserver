import platform
import socket
import click
import subprocess
import re

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def run(self):
        self.host_port_control()
        self.udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        self.udp_socket.settimeout(2)
        try:
            while True:
                self.client_message = input("Enter your command:")
                if self.client_message == "exit":
                    break

                if self.client_message == "time":
                    self.get_time()

                else:
                    print("Command not found!")

        except Exception as e:
            print(e)
    
    def get_time(self):
        buffer_size = 1024
        op_system = platform.system()
        
        bytes_to_send = str.encode(self.client_message)
        self.udp_socket.sendto(bytes_to_send, self.server_address)

        server_message = self.udp_socket.recvfrom(buffer_size)
        msg = server_message[0].decode()

        print("Server response: " + msg)

        if msg:
            is_change = input('Do you want to change the time with Server time? Y/N:')
            if is_change.lower() == 'y':
                if op_system == "Linux":
                    subprocess.run(["timedatectl set-time " + msg.split()[0]], shell= True) # For date
                    subprocess.run(["timedatectl set-time " + msg.split()[1]], shell= True) # For time
                    print("System Date/Time Changed!")
                else:
                    print("Sorry, only Linux Operation System can change time")

    def host_port_control(self):
        if self.host is None : self.host = input('Host address input:')
        if self.port is None : self.port = input('Port address input:')
        
        split_host = re.split('[.]', self.host)
        for h in split_host:
            if not h.isdigit():
                print("Wrong Host Format. Try Again!")
                self.host = None
                self.host_port_control()

        if not self.port.isdigit():
            print("Port must be integer, Try Again!")
            self.port = None
            self.host_port_control()

        self.server_address = (self.host, int(self.port))


@click.command()
@click.option('--host', help='Your Host Address', default=None)
@click.option('--port', help="Your Port Address", default=None)
def cli(host, port):
    try:
        client = Client(host, port)
        client.run()
    except Exception as e:
        print(e)

if __name__ == '__main__':
    cli()
