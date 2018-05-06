import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD) # GPIO.setmode(GPIO.BOARD)是指定電路板上pin number
#GPIO.setmode(GPIO.BCM) # BCM number
GPIO.setup(8, GPIO.OUT)  # physical number = 8

p = GPIO.PWM(8, 50)  # channel=8(上面設的輸出num) frequency=50Hz
#可以將frquency改成5、30、100
#頻率愈低愈能看到燈泡閃爍(pulse間格明顯)
#頻率愈高會看到燈泡很順的變亮變暗(看不到間隔)
p.start(0)
# dc = duty cycle,每次迴圈增加5，到最亮時再減5，LED會從最暗到最亮再到最暗
try:
    while 1:
        for dc in range(0, 101, 5): # 0到100，++5
            p.ChangeDutyCycle(dc)
            time.sleep(0.1) #間隔為0.1秒，改大(0.5)會看到明顯間格，改小(0.1)會看到燈泡閃爍
        for dc in range(100, -1, -5): # 100到0，--5
            p.ChangeDutyCycle(dc) 
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop() #斷電
GPIO.cleanup() # clean up all the ports you’ve used in the current program. 