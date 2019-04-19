import matplotlib.pyplot as plt
import os
import numpy as np

lognames = os.listdir('/home/pi/dev/projects/Vadelma-Kokoelma/Saa_Asema/data')
lastlog = np.sort(lognames)[-1]

plt.ion()
fig,(ax1,ax2,ax3) = plt.subplots(ncols=1,nrows=3)

with open(lastlog, 'r') as f:
	data = f.readlines()

t = np.zeros(len(data))
p = np.zeros(len(data))
h = np.zeros(len(data))
for ii in range(len(data)):
	hour = data[ii].split()[0]
	t[ii] = data[ii].split()[2]
	p[ii] = data[ii].split()[3]
	h[ii] = data[ii].split()[4]

ax1.plot(hour,t)
ax1.set_title('Temperature')
ax2.plot(hour,p)
ax2.set_title('Pressure')
ax3.plot(hour,h)
ax3.set_title('Humidity')

fig.tight_layout()
plt.draw()

plt.pause(1)

