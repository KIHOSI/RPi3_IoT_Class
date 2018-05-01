import wiringpi 
import time
wiringpi.wiringPiSetup() # For sequential pin numbering

showZero = [1,4,5,6,26,27]
showOne = [4,5]
showTwo = [1,4,6,26,28]
showThree = [1,4,5,6,28]
showFour = [4,5,27,28]
showFive = [1,5,6,27,28]
showSix = [1,5,6,26,27,28,29]
showSeven = [1,4,5]
showEight = [1,4,5,6,26,27,28,29]
showNine = [1,4,5,6,27,28,29]
error_Num = 24
closeAll = [1,4,5,6,24,26,27,28,29]

# 函式要放前面，不然後面沒辦法定義
# 依據想顯示的數字，呼叫對應七節管位置
def call7Segment(num):
    closeAllLight()
    if num == 0:
        for i in showZero:
            openLight(i)
    elif num == 1:
        for i in showOne:
            openLight(i)
    elif num == 2:
        for i in showTwo:
            openLight(i)        
    elif num == 3:
        for i in showThree:
            openLight(i)
    elif num == 4:
        for i in showFour:
            openLight(i)
    elif num == 5:
        for i in showFive:
            openLight(i)
    elif num == 6:
        for i in showSix:
            openLight(i)
    elif num == 7:
        for i in showSeven:
            openLight(i)
    elif num == 8:
        for i in showEight:
            openLight(i)
    elif num == 9:
        for i in showNine:
            openLight(i)        
    else:
        print("輸入錯誤!!!!")
        #openLight(24)
        errorLight()

# 開啟7節管控燈位置
def openLight(num):
    wiringpi.pinMode(num,1) # Set num to 1 ( OUTPUT )
    wiringpi.digitalWrite(num,1) # Write 1 ( HIGH ) to num
    wiringpi.digitalRead(num) # Read num

# 關閉指定7節管控燈位置
def closeLight(num):
    wiringpi.pinMode(num,1) # Set num to 1 ( OUTPUT )
    wiringpi.digitalWrite(num,0) # Write 0 (Low) to num
    wiringpi.digitalRead(num) # Read num

# ErrorLight
def errorLight():
    for i in range(4):
        openLight(error_Num)
        time.sleep(1)
        closeLight(error_Num)
        time.sleep(1)

# 關掉所有的數字顯示
def closeAllLight():
    for i in closeAll:
        wiringpi.pinMode(i,1) # Set num to 1 ( OUTPUT )
        wiringpi.digitalWrite(i,0) # Write 0 (Low) to num
        wiringpi.digitalRead(i) # Read num


while True:
    pinNum = input("請輸入你想顯示的數字(離開請輸入'exit'):")
    if pinNum == "exit":
        closeAllLight()
        break    
    call7Segment(int(pinNum)) # String to int
