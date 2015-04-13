#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3 -u
import numpy
import matplotlib.pyplot as plt
import csv
import logging

window = 100

logging.basicConfig(level=logging.WARNING)
array = []
array2 = []
array3 = []
array4 =  []
array5 =  []
array6 = []

f = open('smoothed2.csv')
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
# for i in range(len(array)-10):
# 	entry = (int(array[i])+int(array[i+1])+int(array[i+2])+int(array[i+3])+int(array[i+4])+int(array[i+5])+int(array[i+6])+int(array[i+7])+int(array[i+8])+int(array[i+9]))/10
# 	array2.append(entry)
# 	logging.info(array[i])
	
for i in range(len(array)-1):
	entry = (int(array[i+1]) - int(array[i]))
	array2.append(entry)

for i in range(len(array2)-1):
	if int(array2[i]) >= 0 and int(array2[i+1]) < 0:
		entry = 1
		array3.append(array[i])
		array4.append(array[i])
	else:
		entry = 0
		array3.append(min(array))

print(array4)


#local maxima
for i in range(len(array4)-2):
	if int(array4[i+1]) > int(array4[i]) and int(array4[i+1]) > int(array4[i+2]):
		array5.append(array4[i+1])

print(array5)

index = 0
for i in range(len(array3)):
	minimum = min(array3)
	if array3[i] is array5[index]:
		array6.append(array5[index])
		if index < len(array5)-1:
			print(array5[index])
			index = index + 1
	else:
		array6.append(minimum)

print(array6)



plt.figure(1)
plt.subplot(3,1,1)
plt.plot(array)
plt.plot(array3)
plt.subplot(3,1,2)
plt.plot(array2)
plt.subplot(3,1,3)
plt.plot(array6)
# plt.ylabel('some numbers')
plt.show()