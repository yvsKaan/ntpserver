# NTP Project


## Installitation

### Clone repo 

    git clone https://github.com/yvsKaan/ntpserver.git

## Run 

* You need to start server side first.

    go run server.go

* When your server working, you can start your client.
    
    python ntpclient.py

    * You need to enter host and port values.
        * You can use Localhost HOST : 127.0.0.1 PORT : 1234
        * Or you can change the server host and port address from server.go file 
            You Can See Your Ntp Servers 
                pgreo ntpd
                ss -tulpn | grep ":123"

    * After That You need to enter your command and system will response.
        ###### Command Examples
        * time => Get the Server Time and Date
        * exit => Close the NTP Client