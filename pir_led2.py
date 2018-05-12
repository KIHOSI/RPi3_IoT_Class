import RPi.GPIO as IO
import time
IO.setwarnings(False)
IO.setmode(IO.BCM)

IO.setup(14,IO.OUT) #GPIO 2 -> Red LED as output
#IO.setup(3,IO.OUT) #GPIO 3 -> Green LED as output
IO.setup(17,IO.IN) #GPIO 14 -> IR sensor as input

while 1:

    if(IO.input(17)==True): #object is far away
        print("test1")
        IO.output(14,True) #Red led ON
        time.sleep(0.1)
        #IO.output(3,False) # Green led OFF
    
    if(IO.input(17)==False): #object is near
        print("test2")
        IO.output(14,False) #Green led ON
        time.sleep(0.1)
        #IO.output(2,False) # Red led OFF

GPIO.cleanup()        