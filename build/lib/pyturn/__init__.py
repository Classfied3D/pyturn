from . import turn, go
import time

REASONABLE_VALUE = 10 ** 14 # if this creates a bug in 300 years then lmao

class TURNServer:
    def __init__(self, addr: str, user: str, cred: str, src_port: int=0, realm: str=""):
        cfg = turn.ClientConfig()
        cfg.TURNServerAddr = addr
        cfg.Realm = realm
        cfg.Username = user
        cfg.Password = cred
        cfg.Conn = turn.NetListenPacket("udp4", "0.0.0.0:" + str(src_port))
        cfg.LoggerFactory = go.logging_LoggerFactory()

        self.is_listening = False
        try:
            self.client = turn.NewClient(cfg)
        except RuntimeError as e:
            raise OSError(str(e))

    def listen(self):
        if not self.is_listening:
            self.is_listening = True
            try:
                self.client.Listen()
            except RuntimeError as e:
                raise OSError(str(e))
        
    def allocate(self, retry=0, retry_time=60):
        if not self.is_listening:
            raise OSError("TURN server is not being listened to. Call .listen() before allocating")
        try:
            return TURNSocket(self.client.Allocate())
        except RuntimeError as e:
            if str(e).endswith("Allocation Bandwidth Quota Reached") and retry > 0:
                time.sleep(retry_time)
                return self.allocate(retry - 1, retry_time)
            raise OSError(str(e))
    
    def close(self):
        if self.is_listening:
            self.is_listening = False
            try:
                self.client.Close()
            except RuntimeError as e:
                raise OSError(str(e))

    def __del__(self):
        self.close()

class TURNSocket:
    def __init__(self, conn: go.net_PacketConn):
        self.is_open = True
        self.go_conn = conn
        self.timeout = REASONABLE_VALUE

    def recvfrom(self, bufsize):
        if not self.is_open:
            raise OSError("Socket has been closed")
        go_buf = go.Slice_byte(bytes(bytearray(bufsize)))
        try:
            turn.NetConnSetTimeout(self.go_conn, int(self.timeout * 1000))
            go_packet = turn.NetConnReadFrom(self.go_conn, go_buf)
        except RuntimeError as e:
            if str(e).endswith("i/o timeout"):
                raise TimeoutError(str(e))
            raise OSError(str(e))
        return bytes(go_buf)[:go_packet.N], decode_go_addr(go_packet.Addr)

    def sendto(self, packet, addr):
        if not self.is_open:
            raise OSError("Socket has been closed")
        go_buf = go.Slice_byte(packet)
        go_addr = encode_go_addr(addr)
        try:
            turn.NetConnSetTimeout(self.go_conn, int(self.timeout * 1000))
            turn.NetConnWriteTo(self.go_conn, go_buf, go_addr)
        except RuntimeError as e:
            if str(e).endswith("i/o timeout"):
                raise TimeoutError(str(e))
            raise OSError(str(e))
        
    # Get relayed address
    def getsockname(self):
        if not self.is_open:
            raise OSError("Socket has been closed")
        try:
            go_addr = turn.NetConnGetLocalAddr(self.go_conn)
        except RuntimeError as e:
            raise OSError(str(e))
        return decode_go_addr(go_addr)

    # timeout: The read/write timeout in seconds. Set to None for no timeout
    def settimeout(self, timeout):
        self.timeout = timeout
        if timeout is None:
            self.timeout = REASONABLE_VALUE

    def close(self):
        if self.is_open:
            self.is_open = False
            turn.NetConnClose(self.go_conn)

    def __del__(self):
        self.close()

def encode_go_addr(addr):
    ip, port = addr
    return turn.NetResolveUDPAddr("udp", ip + str(":") + str(port))

def decode_go_addr(go_addr):
    ip, str_port = turn.NetAddrString(go_addr).split(":")
    port = int(str_port)
    return (ip, port)