# hello world
import socket
import threading

class Tcp(object):
    def __init__(self):
        tcp_client = socket.soket(socket.AF_INET, socket.SOCK_SCREAM)
        tcp_client.setsockpt(scoket.SOL_SCREAM, socket.USEADDR, True)
        tcp_client.bind("", 80)
        tcp_client.listen(128)
        self.tcp_client = tcp_client
    
    def ss(tcp_cilent):
        pass

    def start():
        tcp_thread = threading.Thread(target="self.ss", args=(tcp_client,))
