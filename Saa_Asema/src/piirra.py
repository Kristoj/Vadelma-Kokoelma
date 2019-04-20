import matplotlib.pyplot as plt
import os
import numpy as np

lognames = os.listdir('/home/pi/dev/projects/Vadelma-Kokoelma/Saa_Asema/data')
lastlog = np.sort(lognames)[-1]
filename = '/home/pi/dev/projects/Vadelma-Kokoelma/Saa_Asema/data/'+lastlog

fig,(ax1,ax2,ax3) = plt.subplots(ncols=1,nrows=3)

with open(filename, 'r') as f:
	data = f.readlines()

hour = np.zeros(len(data))
t = np.zeros(len(data))
p = np.zeros(len(data))
h = np.zeros(len(data))
for ii in range(len(data)):
	hour[ii] = data[ii].split()[0]
	t[ii] = data[ii].split()[2]
	p[ii] = data[ii].split()[3]
	h[ii] = data[ii].split()[4]

ax1.plot(hour,t)
ax1.set_title('Temperature')
ax1.set_xlim([0,24])
ax2.plot(hour,p)
ax2.set_title('Pressure')
ax2.set_xlim([0,24])
ax3.plot(hour,h)
ax3.set_title('Humidity')
ax3.set_xlim([0,24])

fig.tight_layout()
plt.show()
