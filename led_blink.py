import os
import RPi.GPIO as GPIO
from time import sleep

# Set up the GPIO pin for the LED
LED_PIN = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

# Function to flash LED
def flash_led(speed):
    if speed < 10:
        # Flash quickly for slow speed
        for _ in range(3):
            GPIO.output(LED_PIN, GPIO.HIGH)
            sleep(0.1)
            GPIO.output(LED_PIN, GPIO.LOW)
            sleep(0.1)
    else:
        # Flash slowly for fast speed
        GPIO.output(LED_PIN, GPIO.HIGH)
        sleep(1)
        GPIO.output(LED_PIN, GPIO.LOW)
        sleep(1)

# Run the speed test
speed_test_result = os.popen("speedtest --simple").read()
download_speed = float(speed_test_result.split('Download: ')[1].split(' Mbit/s')[0])

# Flash the LED based on the download speed
flash_led(download_speed)

GPIO.cleanup()
