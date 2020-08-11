import socket
from threading import Thread
from time import localtime, gmtime, strftime, sleep
from picamera import PiCamera
from gpiozero import MotionSensor

cam = PiCamera()
pir = MotionSensor(17)

cam.framerate = 24
cam.resolution = (640, 480)
cam.vflip = True
sock = socket.socket()
sock.bind(('0.0.0.0', 8000))
sock.listen(0)

def net_stream():
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

def motion_capture():
    while True:
        pir.wait_for_motion()
        logtime = strftime("[%H:%M:%S on %m/%d/%Y]\n", localtime())
        cam.capture("{}.jpg".format(logtime))
        print("Motion/Image at {} captured.".format(logtime))
        pir.wait_for_no_motion()

def motion_log():
    while True:
        pir.wait_for_motion()
    with open("motion.log", "a+") as motionlog:
        motionlog.write(strftime("[%H:%M:%S on %m/%d/%Y]\n", localtime()))
    pir.wait_for_no_motion()

cam.start_preview()
sleep(2) # warmup time

Thread(target=motionLog).start()
print("motionLog thread started.")
Thread(target=net_stream).start()
print("netStream thread started.")

cam.stop_preview()
