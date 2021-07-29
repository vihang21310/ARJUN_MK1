#!/usr/bin/env python3.8

import socket
import serial
# arduino = serial.Serial(port="/dev/ttyACM0", baudrate=9600, timeout=0.01)

# def data_write(x):
#     if x == 'FORWARD':

#         arduino.write(b'f')

#     elif x == 'BACKWARD':
#         arduino.write(b'd')

#     elif x == 'LEFT':
#         arduino.write(b'l')
    
#     elif x == 'RIGHT':
#         arduino.write(b'r')

#     elif x == 'STOP':
#         arduino.write(b's')

#     elif x == 'ccw':
#         arduino.write(b'c')

#     elif x == 'cw':
#         arduino.write(b'w')

#     elif x == 'UP1':
#         arduino.write(b'u')

#     elif x == 'UP':
#         arduino.write(b'v')
    
    
        
s = socket.socket()

HOST1='192.168.0.106'
PORT=48151

s.bind((HOST1,PORT))    
s.listen(5)            
print(".....!!!WAITING FOR CONNECTIONS!!!.....")

while True:
    clientsocket, address = s.accept()          

    while True:
        
        LETTER=clientsocket.recv(1)                                 
        SIZE=ord(LETTER.decode('utf-8'))                            
        msg=clientsocket.recv(SIZE)                                 
        msg = msg.decode('utf-8')
        print(msg)
        # data_write(msg)
    clientsocket.close()          
