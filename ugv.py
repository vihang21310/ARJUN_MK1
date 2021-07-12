#!/usr/bin/env python3.8
import pygame
import socket
from pygame.locals import*

c=socket.socket()
HOST1='192.168.0.104'
PORT=7071
c.connect((HOST1,PORT))



pygame.init()
pygame.joystick.init()

deadzone = 0.6


win =  pygame.display.set_mode((1,1))

pygame.display.set_caption("ugv")


try:
    j = pygame.joystick.Joystick(0)
    j.init()
    print ("joystick found")

except pygame.error:
    print ("no joystick found")


run = True
while run:
    button=""
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.locals.JOYAXISMOTION:
            x1, y1 = j.get_axis(0), j.get_axis(1)

            y2, x2 = j.get_axis(4), j.get_axis(3)
            
            if y2 < -1*deadzone:
                 button = "ccw"
                 print("ccw")
                 print("cw\n","y2:" ,y2)
                 
                 

            
            elif y2 > deadzone:
                 button = "cw"
                 print("cw\n","y2:" ,y2)
                 

            
           
               
               
            
            elif  x2 < -1 * deadzone:
                button = "UP1"
                print("upper motor ccw")
                print("x2:",x2)


            elif x2 > deadzone:
                button ="UP"
                print("upper motor cw")
                print("x2:",x2)

        
            elif y1 < -1*deadzone:
                    
                button = "FORWARD"
                print("Forward")
                print("y1:",y1)

            elif y1 > deadzone:
                button = "BACKWARD"  
                print("Backward")
                print("y1:",y1)


            
            

            elif  x1 < -1 * deadzone:
                button = "LEFT"
                print("Left")
                print("x1:",x1)


            elif x1 > deadzone:
                button ="RIGHT"
                print("Right")
                print("x1:",x1)

            elif y1 <= deadzone and y1 >= -1 *deadzone:
               
                button = "STOP"
                print("Stop")


    HEADER=chr(len(button))           
    c.send(bytes(HEADER,'utf-8'))    
    c.send(bytes(button,'utf-8'))

                
pygame.quit()

