# Camera actions (Scan for motion, etc)

from time import gmtime, strftime, sleep
from picamera import PiCamera
from gpiozero import MotionSensor

cam = PiCamera()
pir = MotionSensor(4)

cam.start_preview()
sleep(2)
print("Camera preview started. Waiting for motion...")
while True:
    pir.wait_for_motion()
    logtime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    cam.capture("{}.jpg".format(logtime))
    print("Image at {} captured.".format(logtime))
    pir.wait_for_no_motion()

cam.stop_preview()
