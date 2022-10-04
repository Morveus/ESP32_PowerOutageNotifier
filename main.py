import time
from machine import Pin, ADC

debug = False
detector = Pin(4, Pin.IN, Pin.PULL_UP)
blueLED = Pin(17, Pin.OUT)
redLED = Pin(5, Pin.OUT)

blueLED.value(0)
redLED.value(0)


def beeper(times, duration, delay):
    i = 0
    buzzer=Pin(23,Pin.OUT)
    while i<times:
        # Turn everything on
        buzzer.value(1)
        blueLED.value(1)
        redLED.value(1)
        # Sleep for a few ms
        time.sleep_ms(duration)
        # Turn everything off
        buzzer.value(0)
        blueLED.value(0)
        redLED.value(0)
        # Sleep for a few ms
        time.sleep_ms(delay)
        i = i+1

print("Starting up...")
beeper(10, 5, 100) # 2 times, 20 ms per pulse, 100ms between pulses
print("Ready.")
beeper(1, 500, 1) # We're ready

while True:
    if(detector.value() == 1):
        if(not debug):
            beeper(1, 500, 1)
        redLED.value(1)
        blueLED.value(0)
    else:
        redLED.value(0)
        blueLED.value(1)
        
    time.sleep_ms(500)
