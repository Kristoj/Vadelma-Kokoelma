
import bme280_sample
import matplotlib.pyplot as plt

for ii in range(100):
	bme280_sample.readData()
	with open('temperatures.txt', 'r') as f:
		t = f.readlines()
		
	fig,(ax1,ax2,ax3) = plt.subplots(ncols=1,nrows=3)
	ax1.plot(t)
	ax1.set_title('Temperature')
	
	