from time import sleep
import os
import RPi.GPIO as GPIO
GPIO.setmode (GPIO.BOARD)
#BCM uses the GPIO numbers while BOARD uses the actual pin number
GPIO.setwarnings (False)


#First we initialize the inputs and outputs:

#Outputs (LED)
GPIO.setup(21, GPIO.OUT) #green
GPIO.setup(19, GPIO.OUT) #red
GPIO.setup(23, GPIO.OUT) #blue

#Inputs (Buttons)
GPIO.setup(11, GPIO.IN) #Button1
GPIO.setup(12, GPIO.IN) #Button2
GPIO.setup(13, GPIO.IN) #Button3

#Inputs (Sensors)

GPIO.setup(7, GPIO.IN) #Sensor1, e.g. PID
GPIO.setup(26, GPIO.IN) #Sensor2
GPIO.setup(32, GPIO.IN) #Sensor3
GPIO.setup(33, GPIO.IN) #Sensor4
GPIO.setup(8, GPIO.IN) #Sensor5
GPIO.setup(10, GPIO.IN) #Sensor6
GPIO.setup(35, GPIO.IN) #Sensor7
GPIO.setup(38, GPIO.IN) #Sensor8
GPIO.setup(40, GPIO.IN) #Sensor9

#MOSFET to act as a switch
GPIO.setup(15, GPIO.OUT) #this is an output?



#Now we start the test procedure:

#test LED, each color for 2 seconds:
#green led
GPIO.output(21, GPIO.HIGH)
print ("LED green on")
sleep (2)
GPIO.output(21, GPIO.LOW)
print ("LED green off")
#red led
GPIO.output(19, GPIO.HIGH)
print ("LED red on")
sleep (2)
GPIO.output(19, GPIO.LOW)
print ("LED red off")
#red blue
GPIO.output(23, GPIO.HIGH)
print ("LED blue on")
sleep (2)
GPIO.output(23, GPIO.LOW)
print ("LED blue off")
sleep (2)
print ("LED tests done")

#Test the MOSFET switch for 5 seconds:

GPIO.output(15, GPIO.HIGH)
print ("MOSFET activated")
sleep (5)
GPIO.output(23, GPIO.LOW)
print ("Mosfet deactivated")
sleep (2)
print ("MOSFET tests done, start testing inputs")



#Now we test the inputs, if the desired GPIO pins get a voltage, this script will print a text
#if one of the 3 buttons are cloing, it will print a message


while(True):

    if (GPIO.input(11)):
        print ("Button 1 pushed")
    if (GPIO.input(12)):
        print ("Button 2 pushed")
    if (GPIO.input(13)):
        print ("Button 3 pushed")

        
        
    if (GPIO.input(7)==True):
        print ("Yes, Sensing on pin7")
    if (GPIO.input(26)==True):
        print ("Yes, Sensing on pin26")
    if (GPIO.input(32)==True):
        print ("Yes, Sensing on pin32")
    if (GPIO.input(33)==True):
        print ("Yes, Sensing on pin33")
    if (GPIO.input(8)==True):
        print ("Yes, Sensing on pin8")
    if (GPIO.input(10)==True):
        print ("Yes, Sensing on pin10")       
    if (GPIO.input(35)==True):
        print ("Yes, Sensing on pin35")
    if (GPIO.input(38)==True):
        print ("Yes, Sensing on pin38")
    if (GPIO.input(40)==True):
        print ("Yes, Sensing on pin40")



GPIO.cleanup()
