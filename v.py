import cv2,socket,pickle,os
import numpy as np
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_SNDBUF,100000000)
server_ip = "192.168.0.106"
server_port = 6666

cap = cv2.VideoCapture(0)
while True:
	ret,photo = cap.read()
	ret,buffer = cv2.imencode(".jpg",photo,[int(cv2.IMWRITE_JPEG_QUALITY),30])
	x_as_bytes = pickle.dumps(buffer)
	s.sendto((x_as_bytes),(server_ip,server_port))
	

cap.release()

