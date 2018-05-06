# Pulsates an LED connected to GPIO pin 1 with a suitable resistor 4 times using softPwm
# softPwm uses a fixed frequency
import wiringpi

OUTPUT = 1

PIN_TO_PWM = 15 # wPi

wiringpi.wiringPiSetup()
wiringpi.pinMode(PIN_TO_PWM,OUTPUT)
wiringpi.softPwmCreate(PIN_TO_PWM,0,100) # Setup PWM using Pin, Initial Value and Range parameters
# int softPwmCreate (int pin, int initialValue, int pwmRange)


for time in range(0,4): # 亮三次
	for brightness in range(0,100): # Going from 0 to 100 will give us full off to full on
		wiringpi.softPwmWrite(PIN_TO_PWM,brightness) # Change PWM duty cycle
		wiringpi.delay(50) # Delay for 0.2 seconds
	for brightness in reversed(range(0,100)): # 相反，從100到0
		wiringpi.softPwmWrite(PIN_TO_PWM,brightness)
		wiringpi.delay(50)