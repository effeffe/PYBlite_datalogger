# -*- coding: utf-8 -*-
'''
Filippo Falezza <filippo.falezza at outlook dot it>
¢2020 GPLv3

The purpose of this script is the creation of one graph per set of input data.
The data are mean to be visualised around the first peak intensity (+-500 unit time around peak).
This is saved to a png file, while the peaks are recordered on data%s.txt
'''

import numpy as np
import matplotlib.pyplot as plt

#define arrays
letter = 'H'
Horiz = np.loadtxt('Mag%s-void_0_dist.csv' % letter)
Vert = np.loadtxt('Mag%s-void_1_dist.csv' % letter)
Volt = np.loadtxt("voltage_ref-%s-void_dist.txt" % letter)
time = np.arange(1,20001)
#DEBUG
#print(Horiz,Vert,Volt,time)

#Scale data to actual field and add errors
Horiz = (Volt*1000/2-Horiz*Volt*1000/4096)/60
Vert = (Volt*1000/2-Vert*Volt*1000/4096)/60

#find peak in the data: and show region anround this
Time_peak = np.where(Horiz == np.min(Horiz))[0][0]
Peaks = [np.min(Horiz), np.min(Vert)]

file = open('data%s.txt' % letter, 'w')
file.write(np.array2string(Peaks[0]))
file.write(' radial\n')
file.write(np.array2string(Peaks[1]))
file.write(' vertical\n')
file.close()

#create figure
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.plot(time, Horiz, 'b', label='Radial field')
ax.plot(time, Vert, 'r', label='Vertical field')
ax.set_title('Magnetic field at distance %s' % letter)
ax.set_xlabel('Time [0.2ms]')
ax.set_ylim(top=10)#This should be removed, instead should use a preprocess filter to ignore all data over 4096.
ax.set_ylabel('Magnetic field [mT]')
ax.set_xlim(Time_peak-500, Time_peak+500)
ax.legend()
plt.savefig('Mag%s.png' % letter)

