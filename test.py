import urllib.request
import pyturn
import socket

# Set up relayed connection
addr = "freestun.net:3478"
user = "free"
cred = "free"
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
external_sock.bind(("0.0.0.0", extenal_port))
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
