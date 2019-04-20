import matplotlib.pyplot as plt
import os
import numpy as np

lognames = os.listdir('../data')
lastlog = np.sort(lognames)[-1]
filename = '../data/'+lastlog

with open(filename, 'r') as f:
	data = f.readlines()

hour = np.zeros(len(data))
t = np.zeros(len(data))
p = np.zeros(len(data))
h = np.zeros(len(data))
meas_time = np.zeros(len(data))
for ii in range(len(data)):
	hour[ii] = data[ii].split()[0]
	t[ii] = data[ii].split()[2]
	p[ii] = data[ii].split()[3]
	h[ii] = data[ii].split()[4]
	meas_time[ii] = float(data[ii].split()[0]+'.'+data[ii].split()[1])

fig,(ax1,ax2,ax3) = plt.subplots(ncols=1,nrows=3)
ax1.plot(meas_time,t)
ax1.set_title('Temperature')
ax1.set_xlim([0,24])
ax1.set_ylabel('C')
ax2.plot(meas_time,p)
ax2.set_title('Pressure')
ax2.set_xlim([0,24])
ax2.set_ylabel('hPa')
ax3.plot(meas_time,h)
ax3.set_title('Humidity')
ax3.set_xlim([0,24])
ax3.set_ylabel('%')

fig.tight_layout()
plt.show()
