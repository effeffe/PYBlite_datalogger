'''
Author: Filippo Falezza
Co-owner: Eric Liu
'''
from pyb import ADC,Pin,Timer,main
from array import array
from time import sleep
import os,gc

#initialise pins
adc0 = ADC(Pin.board.Y12)
adc1 = ADC(Pin.board.Y11)
tim = Timer(4, freq=5000) #create 5KHz timer

sleep(1)#wait for the board to flush some data and don't get mad when copying/paste the code
rx0_0 = array('H', (0 for i in range(5000)))
rx0_1 = array('H', (0 for i in range(5000)))
rx1_0 = array('H', (0 for i in range(5000)))
rx1_1 = array('H', (0 for i in range(5000)))
rx2_0 = array('H', (0 for i in range(5000)))
rx2_1 = array('H', (0 for i in range(5000)))
rx3_0 = array('H', (0 for i in range(5000)))
sleep(1)
rx3_1 = array('H', (0 for i in range(5000)))

#timeout of 5s before the acquisition, 
sleep(5)

#4s acquisition:
ADC.read_timed_multi((adc0,adc1), (rx0_0,rx0_1), tim)
ADC.read_timed_multi((adc0,adc1), (rx1_0,rx1_1), tim)
ADC.read_timed_multi((adc0,adc1), (rx2_0,rx2_1), tim)
ADC.read_timed_multi((adc0,adc1), (rx3_0,rx3_1), tim)
gc.collect()
#main("/sd/write.py") # script to execute next to save the data
#Note: Y11 Vertical, Y12 Horizontal for the conf used
