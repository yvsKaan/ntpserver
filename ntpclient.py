import ntplib
from time import ctime
from datetime import datetime, timezone

def get_ntp_server():
    try:
        client = ntplib.NTPClient()
        host_address = input('Host address input:')
        port_address = input('Port address input:')
        response = client.request(host=host_address, port=port_address)

        if response:
            print('You are connected to NTP server')
            print(f"Your host: {host_address}")
            print(f"Your port: {port_address}")
            print(f"Today: {ctime(response.orig_time)}")
            print(f"Client time of request: {datetime.fromtimestamp(response.orig_time, timezone.utc)}")
            print(f"Server responded with: {datetime.fromtimestamp(response.tx_time, timezone.utc)}")

        else: 
            print("You are not connected to NTP server")
    except Exception as e:
        print(e)


get_ntp_server()

   