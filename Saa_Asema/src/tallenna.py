
import bme280_sample
import matplotlib.pyplot as plt
import time

fig,(ax1,ax2,ax3) = plt.subplots(ncols=1,nrows=3)
for ii in range(10):
	bme280_sample.readData()
	with open('temperatures.txt', 'r') as f:
		t = f.readlines()
	
	ax1.plot(t)
	ax1.set_title('Temperature')
	#plt.show(block=False)
	plt.draw()
	
	time.sleep(1)
	
