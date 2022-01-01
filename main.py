from gpiozero import LED
from time import sleep
from gpiozero import Buzzer
from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero import Button

b = TonalBuzzer(17)
led = LED(2)
led.off()
button = Button(3)
print("Setting up")
print("Motor  Output on Pin: " + led)
print("Buzzer Output on Pin: " + b)
print("Button  Input on Pin: " + button)



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
  print(ml + "ml dispensing")
    startTones()
    led.on()
    sleep(1)
    led.off()
    sleep(1)
    led.on()
    sleep(1)
    led.off()
    endTones()
  print(ml + "ml dispense complete")

button.wait_for_press()
dispense(1000)
