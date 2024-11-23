# PyTurn
A python client that implements the TURN protocol. This library is made from [Pion's TURN implementation](https://github.com/pion/turn/tree/master) in go, and converted to python using [gopy](https://github.com/go-python/gopy). The reason for this is due to there not being any other python implementation.

## Info
* Currently TURN over UDP is the only implemented method
* IPv6 is not currently implemented as it is not yet in Pion's implementation

## Installation
* `pip3 install ` + relavent `.whl` file for your system (see [dist](dist))
* If one does not exist, or you wish to compile yourself, see [COMPILATION.md](COMPILATION.md)

## Example
``` python
# Note: this example won't work over a symmetric NAT if the
# TURN server uses a port restricted NAT (which seems to be
# the case on some TURN servers).
import urllib.request
import pyturn
import socket

# Set up relayed connection
addr = "example.com:3478"
user = "user123"
cred = "pass123"
client = pyturn.TURNServer(addr, user, cred)
client.listen()
relayed_sock = client.allocate(retry=1)
relayed_sock.settimeout(4)
relayed_addr = relayed_sock.getsockname()
print("Relayed Address:", relayed_addr)

# Set up local connection
extenal_port = 50001
# Get external IP (we are connecting to ourselves)
external_ip = urllib.request.urlopen("http://v4.ident.me") \
  .read().decode("utf8")
external_addr = (external_ip, extenal_port)
external_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
external_sock.bind(("0.0.0.0", external_port))
print("External Address:", external_addr)

# Create connection
# Punch UDP hole to ourselves
relayed_sock.sendto(b"hello", external_addr)
external_sock.sendto(b"hello", relayed_addr) 
packet, addr = relayed_sock.recvfrom(1024)
print(packet, addr)

external_sock.close()
relayed_sock.close()
client.close()
```