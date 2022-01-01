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


def advmode(currmode)
    global mode
    mode = currmode + 1
    print('Mode is now ' + str(mode))

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

while True:
    if actionbutton.is_pressed:
        dispense(1000)
    elif:
        modebutton.is_pressed:
        advmode(mode)
