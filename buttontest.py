from gpiozero import LED, Button
from time import sleep

led = LED(2)
button = Button(3)

button.wait_for_press()
led.on()
sleep(3)
led.off()
