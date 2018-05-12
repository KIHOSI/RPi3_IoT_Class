# 拍照
from picamera import PiCamera
from time import sleep

camera = PiCamera()

#拍一張
#camera.start_preview()
#sleep(5)
#camera.capture('/home/pi/image.jpg')
#camera.stop_preview()

#連拍五張
camera.start_preview()
for i in range(5):
    sleep(5)
    camera.capture('/home/pi/image%s.jpg' % i)
camera.stop_preview()