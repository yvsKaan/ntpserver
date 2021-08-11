package main

import (
	"fmt"
	"net"
	"os"
	"time"
)

const (
	host = "127.0.0.1"
	port = ":1234"
)

func main() {
	udpAddr, err := net.ResolveUDPAddr("udp4", port)
	checkError(err)
	conn, err := net.ListenUDP("udp", udpAddr)
	checkError(err)
	fmt.Println("Listening Server...")
	for {
		handleClient(conn)
	}
}

func handleClient(conn *net.UDPConn) {
	buffer := make([]byte, 1024)
	n, addr, err := conn.ReadFromUDP(buffer)
	checkError(err)

	fmt.Println("Client: ", addr)
	message := string(buffer[:n])
	fmt.Println("Received from Client:", message)

	if message == "time" {
		daytime := time.Now().String()
		conn.WriteToUDP([]byte(daytime), addr)
		fmt.Println("Server answer is " + daytime)
	}
}

func checkError(err error) {
	if err != nil {
		fmt.Fprint(os.Stderr, "Fatal error ", err.Error())
		os.Exit(1)
	}
}
