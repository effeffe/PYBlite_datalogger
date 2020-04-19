'''
Author: Filippo Falezza ¢2020
'''
import os,pyb,array
adc = pyb.ADC(pyb.Pin.board.Y12)
tim = pyb.Timer(4, freq=10000) #create 10KHz timer
#Now it samples 4s at 10KHz
rx0 = array.array('H', (0 for i in range(10000)))
rx1 = array.array('H', (0 for i in range(10000)))
rx2 = array.array('H', (0 for i in range(10000)))
rx3 = array.array('H', (0 for i in range(10000)))
pyb.ADC.read_timed(adc, rx0, tim)
pyb.ADC.read_timed(adc, rx1, tim)
pyb.ADC.read_timed(adc, rx2, tim)
pyb.ADC.read_timed(adc, rx3, tim)
f_ = open("/sd/magnetometer.csv", "w")
for item in rx0:
    f_.write('%d\n' % (item))
for item in rx1:
    f_.write('%d\n' % (item))
for item in rx2:
    f_.write('%d\n' % (item))
for item in rx3:
    f_.write('%d\n' % (item)))
f_.close()
