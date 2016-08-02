class motor(object):
   
    def __init__(self, name, pin, WMin=0, WMax=100, simulation=True):
        self.name = name
        self.powered = False
        self.simulation = simulation
        self.__pin = pin
        
        self.setWLimits(WMin, WMax)
        

        self.__W = self.__WMin
        self.__Wh = 10

        try:
            from RPIO import PWM
            self.__IO = PWM.Servo()
        except ImportError:
            self.simulation = True

    def setPin(self, pin):
        "set the pin for each motor"
        self.__pin = pin


    def setWLimits(self, WMin, WMax):
        "set the power limit for each motor" 
        if WMin < 0:
            WMin = 0
        self.__WMin = WMin
        if WMax > 100:
            WMax = 100
        self.__WMax = WMax

    

    def start(self):
        "Run the procedure to init the PWM"
        if not self.simulation:
            try:
                from RPIO import PWM
                self.__IO = PWM.Servo()
                self.powered = True
                #TODO Decide How to manage the WMax < 100
                #to keep anyhow the throttle range 0-100
            except ImportError:
                self.simulation = True
                self.powered = False

    def stop(self):
        "Stop PWM signal"

        self.setW(0)
        if self.powered:
            self.__IO.stop_servo(self.__pin)
            self.powered = False

    def increaseW(self, step=1):
        "increases W% for the motor"

        self.__W = self.__W + step
        self.setW(self.__W)

    def decreaseW(self, step=1):
        "decreases W% for the motor"

        self.__W = self.__W - step
        self.setW(self.__W)

    def getW(self):
        "retuns current W%"
        return self.__W

    def setW(self, W):
        "Checks W% is between limits than sets it"

        PW = 0
        self.__W = W
        if self.__W < self.__WMin:
            self.__W = self.__WMin
        if self.__W > self.__WMax:
            self.__W = self.__WMax
        PW = (1000 + (self.__W) * 10)
        # Set servo to xxx us
        if self.powered:
            self.__IO.set_servo(self.__pin, PW)




mymotor = motor('m1', 17, simulation=False)
#where 17 is  GPIO17 = pin 11

print('***Disconnect ESC power')
print('***then press ENTER')
res = raw_input()
mymotor.start()
mymotor.setW(0)

#NOTE:the angular motor speed W can vary from 0 (min) to 100 (max)
#the scaling to pwm is done inside motor class
print('***Connect ESC Power')
print('***Wait beep-beep')

print('***then press ENTER')
res = raw_input()
mymotor.setW(0)
print('***Wait N beep for battery cell')
print('***Wait beeeeeep for ready')
print('***then press ENTER')
res = raw_input()
print ('increase > a | decrease > z | set W > int | quit > q')

cycling = True
try:
    while cycling:
        res = raw_input()
        if res == 'a':
            mymotor.increaseW()
        if res == 'z':
            mymotor.decreaseW()
        if res.isdigit()
          res=int(res)
          mymotor.setW(res)
        if res == 'q':
            cycling = False
finally:
    # shut down cleanly
    mymotor.stop()
    print ("well done!")









