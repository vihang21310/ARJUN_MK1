import cv2, socket, numpy, pickle
import datetime
s=socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
ip="100.104.200.89"
port=6666
s.bind((ip,port))
while True:
	x=s.recvfrom(1000000)
	clientip = x[1][0]
	data=x[0]
	data=pickle.loads(data)
	frame = cv2.imdecode(data, cv2.IMREAD_COLOR)
	img = cv2.rectangle(frame,(260,180),(380,300),(0,0,255),2)
	img = cv2.circle(img, (320, 240), 50, (0, 0, 255), 2)
	img = cv2.line(img, (310, 240), (330, 240), (0, 0, 255), 2)
	img = cv2.line(img, (320, 230), (320, 250), (0, 0, 255), 2)
	img = cv2.line(img, (5,9), (5, 50), (0, 0, 255), 2)
	img = cv2.line(img, (5,9), (50, 9), (0, 0, 255), 2)
	img = cv2.line(img, (635, 9), (595, 9), (0, 0, 255), 2)
	img = cv2.line(img, (635, 9), (635, 50), (0, 0, 255), 2)
	img = cv2.line(img, (5, 430), (5, 471), (0, 0, 255), 2)
	img = cv2.line(img, (5, 471), (50, 471), (0, 0, 255), 2)
	img = cv2.line(img, (635, 471), (595, 471), (0, 0, 255), 2)
	img = cv2.line(img, (635, 430), (635, 471), (0, 0, 255), 2)

	font = cv2.FONT_HERSHEY_SIMPLEX
	datet = str(datetime.datetime.now())
	img = cv2.putText(img, datet, (15,50), font, 0.5, (0,0,255), 1, cv2.LINE_AA)
	cv2.namedWindow("server", cv2.WINDOW_NORMAL) 
	frame = cv2.resize(frame, (500,400)) 

	cv2.imshow('server', frame) #to open image
	if cv2.waitKey(10) == 13:
	  break
cv2.destroyAllWindows()