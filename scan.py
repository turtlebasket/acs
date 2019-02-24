# Scan behavior for camera
from datetime import datetime as dt 			# necessary for logging
from gpiozero import Button, MotionSensor		# hardware stuff
import picamera									# camera
import socket									# streaming
from os import system
from multiprocessing import Process

system("curl", "ipinfo.io/ip", ">>", "pubIp.txt")
pubIP = open("pubIp.txt", "r").read()

log =open("scan-log.txt", "w")

pir = MotionSensor(17)
cam = picamera.PiCamera(resolution='640x480', framerate=24)

def scan():
	while True:
		pir.wait_for_motion()	
		log.write(dt.now().strftime("%Y-%m-%d %H:%M:%S"))
		with cam as camera:
			capture_name = dt.now().strftime("%Y-%m-%d_%H-%M-%S")
			camera.start_recording(str(capture_name + '.mp4'))
			pir.wait_for_no_motion()
			camera.stop_recording()

def stream():
	streamSocket = socket.socket()
	streamSocket.bind('', 8000)
	server_socket.listen(0)
	# connection = server_socket.accept()[0].makefile('rb') # <-- dunno if I need this

	while True:
		with cam as camera:
			camera.capture(streamSocket) # should be able to capture to socket... right?
		sleep(0.5) 

# runtime stuffs
if __name__ == '__main__': 	
	Process(target=scan).start()
	Process(target=stream).start()