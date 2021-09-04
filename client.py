import socket

IP = "147.182.169.218"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 22))
# uncomment line below to use from server vs locally
# s.connect((IP, 22))

msg = s.recv(1234)
print(msg.decode("utf-8"))
