import socket
import car_controller as car

TF = 0.05
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print('Received: ' + data)
    if data.lower() == 'w':
        car.forward(TF)
    elif data.lower() == 's':
        car.reverse(TF)
    elif data.lower() == 'a':
        car.fullleft(TF)
    elif data.lower() == 'd':
        car.fullright(TF)
    elif data.lower() == 'q':
        car.left(TF)
    elif data.lower() == 'e':
        car.right(TF)
    else:
        print("Hell no to the no no ...")