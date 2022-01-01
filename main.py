from gpiozero import LED
from time import sleep
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero import Button
print("Setting up")
b = TonalBuzzer(17)
led = LED(2)
led.off()
actionbutton = Button(3)
modebutton = Button(14)
mode = 1
print("Ready...")


def advmode(currmode):
    global mode
    if currmode >= 4:
        mode = 1
    else
        mode = currmode + 1
    print('Mode is now ' + str(mode))
    sleep(0.5)

def startTones():
    b.play(Tone(222.0))
    sleep(1)
    b.play(Tone(249.19))
    sleep(1)
    b.stop()

def endTones():
    b.play(Tone(296.00))
    sleep(0.25)
    b.stop()
    b.play(Tone(296.00))
    sleep(0.25)
    b.stop()

def dispense(ml):
    print("Dispensing:")
    print(ml)
    startTones()
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    led.on()
    sleep(1)
    led.off()
    endTones()
    print("Dispense Complete")

def clean():
    print("Clean not currently implemented returning:")

def calibrate():
    print("Calibrate not currently implemented returning:")

def update():
    print("Update not currently implemented returning:")


def performaction():
    if mode = 1:
        print("Mode is dispense")
        dispense(1000)
    elif mode = 2:
        print("Mode is clean")
        clean()
    elif mode = 3:
        print("Mode is calibrate")
        calibrate()
    elif mode = 4:
        print("Mode is update")
        update()
    else:
        print("Error! Unknown Mode")

while True:
    if actionbutton.is_pressed:
        performaction()
    elif modebutton.is_pressed:
        advmode(mode)
