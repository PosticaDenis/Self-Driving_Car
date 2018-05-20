import logging
import socket
import car_controller as car

log = logging.getLogger('udp_server')
TF = 0.05
UDP_IP = "127.0.0.1"
UDP_PORT = 5005


def udp_server(UDP_IP, UDP_PORT):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    log.info("Listening on udp %s:%s" % (UDP_IP, UDP_PORT))
    s.bind((UDP_IP, UDP_PORT))
    while True:
        (data, addr) = s.recvfrom(128*1024)
        yield data


FORMAT_CONS = '%(asctime)s %(name)-12s %(levelname)8s\t%(message)s'
logging.basicConfig(level=logging.DEBUG, format=FORMAT_CONS)


for data in udp_server():
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