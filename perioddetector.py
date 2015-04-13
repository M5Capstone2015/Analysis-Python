import numpy
import matplotlib.pyplot as plt
import csv
import logging

window = 100

logging.basicConfig(level=logging.INFO)
array = []
array2 = []

f = open('dump1.csv')
csv_f = csv.reader(f)
for row in csv_f:
    array.extend(row)
    logging.debug(row)
logging.info(array)

for i in range(len(array) - 1):
	logging.info(array[i])

# #Remove Outliers
# for i in range(len(array)):
# 	if int(array[i]) > 130:
# 		array[i] = array[i-1]

#Averaging
for i in range(len(array)-10):
	entry = (int(array[i])+int(array[i+1])+int(array[i+2])+int(array[i+3])+int(array[i+4])+int(array[i+5])+int(array[i+6])+int(array[i+7])+int(array[i+8])+int(array[i+9]))/10
	array2.append(entry)
	logging.info(array[i])
	



plt.figure(1)
plt.subplot(2,1,1)
plt.plot(array[1:window])
plt.subplot(2,1,2)
plt.plot(array2)
# plt.ylabel('some numbers')
plt.show()