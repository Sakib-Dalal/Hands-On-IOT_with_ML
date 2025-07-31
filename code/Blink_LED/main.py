from machine import Pin
import time

# Use GPIO 25 for external LED (change if using another pin)
led = Pin(25, Pin.OUT)

while True:
    led.value(1)     # Turn LED ON
    time.sleep(1)    # Wait 1 second
    led.value(0)     # Turn LED OFF
    time.sleep(1)    # Wait 1 second