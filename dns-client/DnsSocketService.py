import socket
class DnsSocketService:

    def __init__(self, pa_dns_server = "8.8.8.8") -> None:
        self.dns_server = pa_dns_server
        self.dns_port = 53
        self._listen_on = "0.0.0.0"
        self._dns_client_port = 60000
        self.socket = None
        

    def init_sockt(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.bind(self._listen_on, self._dns_client_port)
        

    def send_data(self, data:bytes):
        self.sock.sendto(data,(self.dns_server, self.dns_port))

    def get_response(self):
        return self.sock.recvfrom(1000)

    def destroy_socket(self):
        self.sock.close()