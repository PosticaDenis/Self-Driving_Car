import socket
import Tkinter as tk

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
MESSAGE = "Hello, World!"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

def key_input(event):
    print "Key: ", event.char
    key_press = event.char
    key_set = ['w', 's', 'a', 'd', 'q', 'e']

    if key_press.lower() in key_set:
        MESSAGE = key_press.lower()
        print('Key: ' + MESSAGE)
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    else:
        print("Hell no to the no no ...")

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()