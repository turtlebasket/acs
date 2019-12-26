import socket
from threading import Thread
from time import gmtime, strftime, sleep
from picamera import PiCamera
from gpiozero import MotionSensor

cam = PiCamera()
pir = MotionSensor(17)

cam.framerate = 24
cam.resolution = (640, 480)
cam.vflip = True
sock = socket.socket()
sock.bind(('0.0.0.0', 8000))
# sock.bind(('127.0.0.1', 8000))
sock.listen(0)

def netStream():
	while True:
		try:
			connection = sock.accept()[0].makefile('wb')
			print("create connection")
			cam.start_recording(connection, format='h264')
			print("start recording")
			while True:
				cam.wait_recording()
		except:
			pass
		finally:
			try: 
				cam.stop_recording()
				connection.close()
				sock.close()
			except BrokenPipeError: # ignore broken pipe
				pass
		print("-- END STREAM LOOP --")

def motionCapture():
	while True:
		pir.wait_for_motion()
		logtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
		cam.capture("{}.jpg".format(logtime))
		print("Motion/Image at {} captured.".format(logtime))
		pir.wait_for_no_motion()

def motionLog():
	while True:
		pir.wait_for_motion()
		with open("motion.log", "a+") as motionlog:
			motionlog.write(strftime("%Y-%m-%d %H:%M:%S\n", gmtime()))
		pir.wait_for_no_motion()
		
cam.start_preview()
sleep(2) # warmup time

Thread(target=motionLog).start()
print("motionLog thread started.")
Thread(target=netStream).start()
print("netStream thread started.")

cam.stop_preview()
