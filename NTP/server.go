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
	udp_addr, err := net.ResolveUDPAddr("udp4", port)
	checkError(err)
	conn, err := net.ListenUDP("udp", udp_addr)
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
	requestTime := time.Now()
	message := string(buffer[:n])
	if message == "time" {
		daytime := time.Now().Format("2006-01-02 15:04:05.000000")
		conn.WriteToUDP([]byte(daytime), addr)
	} else if message == "exit" {
		conn.WriteToUDP([]byte("Client Closed."), addr)
	} else {
		conn.WriteToUDP([]byte("Failed, Try again."), addr)
	}
	responseTime := time.Now()
	fmt.Println("Response Time:" + responseTime.Sub(requestTime).String())
}

func checkError(err error) {
	if err != nil {
		fmt.Fprint(os.Stderr, "Fatal error ", err.Error())
		os.Exit(1)
	}
}
