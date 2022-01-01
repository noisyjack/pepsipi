from gpiozero import LED
from time import sleep
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero import Button
import subprocess
import sys
print("Setting up")
b = TonalBuzzer(17)                     # Pin with Buzzer attached
led = LED(21)                           # Pin with Dispensor Motor Attached
led.off()
actionbutton = Button(3)                # Pin with Action Button Attached (dispense / update ect)
modebutton = Button(14)                 # Pin with Mode Button Attached (mode change ect)
mode = 1
pumpdispense = 150                      # Pump dispense volume in 60s
print("Ready...")
mode_friendlynames = ["NA", "Dispense", "Clean", "Calibrate", "Update"]
def beep(num):
    while num >= 1:
        sleep(0.15)
        b.play(Tone(400))
        sleep(0.15)
        b.stop()
        num -=1

def advmode(currmode):
    global mode
    global mode_friendlynames
    if currmode >= 4:
        mode = 1
    else:
        mode = currmode + 1
    print('Mode is now ' + mode_friendlynames[mode])
    beep(mode)
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
    global pumpdispense
    print("Dispensing:")
    print(ml)
    dispensetime = 60*(ml/pumpdispense)
    startTones()
    led.on()
    sleep(dispensetime)
    led.off()
    endTones()
    print("Dispense Complete")

def clean():
    print("Cleaning Process Started, Press to End:")
    sleep(0.25)
    startTones()
    led.on()
    actionbutton.wait_for_press()
    led.off()
    endTones()
    print("Cleaning Complete")
    sleep(0.25)
    print("Returning to Dispense Mode")
    global mode
    mode = 1

def calibrate():
    print("Calibrate not currently implemented returning:")
    sleep(0.5)

def update():


    subprocess.run(["sh", "updater.sh"])
    sys.exit(0)

    sleep(0.5)


def performaction():
    if mode == 1:
        print("Mode is " + mode_friendlynames[mode])
        dispense(40)
    elif mode == 2:
        print("Mode is clean")
        clean()
    elif mode == 3:
        print("Mode is calibrate")
        calibrate()
    elif mode == 4:
        print("Mode is update")
        update()
    else:
        print("Error! Unknown Mode")

beep(2)

while True:
    if actionbutton.is_pressed:
        performaction()
    elif modebutton.is_pressed:
        advmode(mode)
