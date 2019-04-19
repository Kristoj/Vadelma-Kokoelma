
import bme280_sample
import matplotlib.pyplot as plt
import time

plt.ion()
fig,(ax1,ax2,ax3) = plt.subplots(ncols=1,nrows=3)
for ii in range(10):
	bme280_sample.readData()
	with open('/home/pi/dev/projects/Vadelma-Kokoelma/Saa_Asema/data/temperatures.txt', 'r') as f:
		t = f.readlines()
	with open('/home/pi/dev/projects/Vadelma-Kokoelma/Saa_Asema/data/pressures.txt', 'r') as f:
		p = f.readlines()
	with open('/home/pi/dev/projects/Vadelma-Kokoelma/Saa_Asema/data/humidities.txt', 'r') as f:
		h = f.readlines()
	
	ax1.plot(t)
	ax1.set_title('Temperature')
	ax2.plot(p)
	ax2.set_title('Pressure')
	ax3.plot(h)
	ax3.set_title('Humidity')
	
	plt.draw()
	
	plt.pause(1)
	
