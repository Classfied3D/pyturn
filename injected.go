package main

import (
	"net"
	"time"
)

// start injected.go

import "errors"

func NetListenPacket(network, address string) (net.PacketConn, error) {
	return net.ListenPacket(network, address)
}

type RecievedPacket struct {
	N int
	Addr net.Addr
}

func NetConnReadFrom(conn net.PacketConn, p []byte)  (RecievedPacket, error) {
	n, addr, err := conn.ReadFrom(p)
	if err != nil {
		return RecievedPacket{}, err
	}
	pack := RecievedPacket{
		N: n,
		Addr: addr,
	}
	return pack, nil
}

func NetConnWriteTo(conn net.PacketConn, p []byte, addr net.Addr) (int, error) {
	return conn.WriteTo(p, addr)
}

func NetConnClose(conn net.PacketConn) error {
	return conn.Close()
}

func NetConnGetLocalAddr(conn net.PacketConn) net.Addr {
	return conn.LocalAddr()
}

func NetAddrString(addr net.Addr) string {
	return addr.String()
}

func NetConnSetTimeout(conn net.PacketConn, sec int) error {
	deadline := time.Now().Add(time.Duration(sec) * time.Millisecond)
	return conn.SetDeadline(deadline)
}

func NetResolveUDPAddr(network, address string) (net.UDPAddr, error) {
	udpAddr, err := net.ResolveUDPAddr(network, address)
	if err != nil {
		return net.UDPAddr{}, err
	}
	return *udpAddr, nil
}

func NetUDPAddrChangePort(addr net.Addr, port int) error {
	udpAddr, ok := addr.(*net.UDPAddr)
	if !ok {
		return errors.New("addr was not a UDPAddr")
	}
	udpAddr.Port = port
	return nil
}

// end injected.go