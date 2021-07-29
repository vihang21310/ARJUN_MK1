#!/usr/bin/env python3.8
import pygame
import socket
import threading
from pygame.locals import*

HOST='192.168.0.106'
PORT=48151

class Ugv:
    def __init__(self,host,port):

        self.c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.c.connect((host,port))
        
        pygame.init()
        pygame.joystick.init()

        self.deadzone = 0.6


        self.win =  pygame.display.set_mode((1,1))

        pygame.display.set_caption("ugv")


        try:
            self.j = pygame.joystick.Joystick(0)
            self.j.init()
            print ("joystick found")

        except pygame.error:
            print ("no joystick found")
            self.pygame.quit()



        self.run = True

    def Transmit(self):  
        while self.run:
            button=""
            pygame.time.delay(100)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.locals.JOYAXISMOTION:
                    x1, y1 = self.j.get_axis(0), self.j.get_axis(1)

                    y2, x2 = self.j.get_axis(4), self.j.get_axis(3)
                    
                    if y2 < -1*self.deadzone:
                        button = "ccw"
                        print("ccw")
                        print("cw\n","y2:" ,y2)
                        
                        

                    
                    elif y2 > self.deadzone:
                        button = "cw"
                        print("cw\n","y2:" ,y2)
                        

                    
                    elif  x2 < -1 * self.deadzone:
                        button = "UP1"
                        print("upper motor ccw")
                        print("x2:",x2)


                    elif x2 > self.deadzone:
                        button ="UP"
                        print("upper motor cw")
                        print("x2:",x2)

                
                    elif y1 < -1*self.deadzone:
                            
                        button = "FORWARD"
                        print("Forward")
                        print("y1:",y1)

                    elif y1 > self.deadzone:
                        button = "BACKWARD"  
                        print("Backward")
                        print("y1:",y1)


                
                    elif  x1 < -1 * self.deadzone:
                        button = "LEFT"
                        print("Left")
                        print("x1:",x1)


                    elif x1 > self.deadzone:
                        button ="RIGHT"
                        print("Right")
                        print("x1:",x1)

                    elif y1 <= self.deadzone and y1 >= -1 *self.deadzone:
                    
                        button = "STOP"
                        print("Stop")


            HEADER=chr(len(button))           
            self.c.send(bytes(HEADER,'utf-8'))    
            self.c.send(bytes(button,'utf-8'))

                
