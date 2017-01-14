import RPi.GPIO as GPIO
import time

# Variables

delay = 0.0055
steps = 500

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Enable GPIO pins for  ENA and ENB for stepper

enable_a = 4
enable_b = 18

# Enable pins for IN1-4 to control step sequence

coil_A_1_pin = 27
coil_A_2_pin = 22
coil_B_1_pin = 23
coil_B_2_pin = 24

# Set pin states

#GPIO.setup(enable_a, GPIO.OUT)
GPIO.setup(enable_b, GPIO.OUT)
#GPIO.setup(coil_A_1_pin, GPIO.OUT)
#GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

# Set ENA and ENB to high to enable stepper

#GPIO.output(enable_a, True)
GPIO.output(enable_b, True)

# Function for step sequence

#def setStep(w1, w2):
#  GPIO.output(coil_A_1_pin, w1)
#  GPIO.output(coil_A_2_pin, w2)

#Reverse
#setStep(1,0)
#time.sleep(3)
#Forward
#setStep(0,1)
#time.sleep(3)


def setStep(w1, w2):
  GPIO.output(coil_B_1_pin, w1)
  GPIO.output(coil_B_2_pin, w2)

#Right
setStep(1,0)
time.sleep(3)
#Left
setStep(0,1)
time.sleep(3)

  
#def setStep(w1, w2, w3, w4):
#  GPIO.output(coil_A_1_pin, w1)
#  GPIO.output(coil_A_2_pin, w2)
#  GPIO.output(coil_B_1_pin, w3)
#  GPIO.output(coil_B_2_pin, w4)

# loop through step sequence based on number of steps

#for i in range(0, steps):
#    setStep(1,0)
#    time.sleep(delay)
#    setStep(0,1)
#    time.sleep(delay)

#for i in range(0, steps):
#    setStep(1,0,1,0)
#    time.sleep(delay)
#    setStep(0,1,1,0)
#    time.sleep(delay)
#    setStep(0,1,0,1)
#    time.sleep(delay)
#    setStep(1,0,0,1)
#    time.sleep(delay)

# Reverse previous step sequence to reverse motor direction

#for i in range(0, steps):
#    setStep(1,0,0,1)
#    time.sleep(delay)
#    setStep(0,1,0,1)
#    time.sleep(delay)
#    setStep(0,1,1,0)
#    time.sleep(delay)
#    setStep(1,0,1,0)
#    time.sleep(delay)

#GPIO.output(enable_a, False)
GPIO.output(enable_b, False)
GPIO.cleanup()
