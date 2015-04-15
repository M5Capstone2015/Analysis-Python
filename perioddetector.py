#!/Library/Frameworks/Python.framework/Versions/3.4/bin/python3 -u
import numpy
import matplotlib.pyplot as plt
import csv
import logging

window = 100

logging.basicConfig(level=logging.WARNING)
array =  []
array2 = []
Portiaderivates = [-22,
10,
-10,
0,
-20,
-30,
0,
-20,
20,
30,
11,
19,
0,
-30,
-30,
-20,
-19,
0,
-1,
14,
46,
-10,
20,
-10,
-10,
-20,
-20,
1,
19,
30,
40,
22,
-12,
-10,
0,
0,
-20,
-20,
10,
30,
48,
5,
-10,
-43,
0,
-20,
-10,
0,
30,
43,
5,
0,
-26,
-12,
0,
0,
-40,
78,
-233,
9,
-20,
244,
0,
-10,
0,
0,
0,
10,
-10,
-9,
0,
-11,
0,
0,
30,
12,
0,
-12,
-19,
0,
0,
-21,
10,
20,
22,
26,
-28,
-20,
0,
-20,
-10,
-20,
41,
19,
33,
-21,
-12,
-10,
-20,
-20,
-20,
30,
30,
22,
31,
-10,
0,
-33,
-10,
10,
33,
0,
-13,
-8,
-12,
0,
-10,
0,
22,
26,
-244,
249,
-33,
-19,
0,
9,
43,
-21,
0,
8,
18,
-5,
-33,
-19,
-21,
-20,
-20,
30,
20,
20,
0,
-20,
-10,
0,
-20,
-10,
-10,
10,
10,
30,
20,
0,
-20,
-20,
0,
-30,
0,
10,
30,
21,
9,
0,
-30,
30,
-9,
0,
9,
43,
-239,
0,
244,
-38,
0,
0,
33,
-239,
20,
-11,
249,
-5,
-5,
-43,
22,
26,
5,
0,
0,
-10,
0,
-33,
0,
38,
5,
0,
-5,
-38,
-10,
-40,
50,
0,
33,
10,
-249,
249,
-10,
-33,
-10,
-9,
9,
22,
0,
21,
-33,
0,
-10,
0,
10,
38,
-244,
0,
244,
-38,
0,
-19,
-21,
10,
30,
33,
5,
-28,
-10,
0,
-10,
-40,
88,
0,
0,
-26,
21,
0,
0,
-21,
21,
0,
-13,
-20,
-30,
-20,
-30,
-19,
-11,
0,
24,
26,
30,
11,
0,
-31,
-20,
-10,
-20,
-10,
0,
30,
30,
10,
-20,
-26,
-13,
-21,
10,
24,
26,
10,
10,
-10,
-30,
-6,
0,
6,
61,
52,
5,
-38,
-19,
0,
0,
9,
48,
0,
-244,
196,
-40,
-10]
Portiaspeaks = [4,
5,
7,
10,
11,
16,
21,
22,
24,
25,
31,
36,
40,
42,
46,
49,
52,
56,
60,
61,
62,
63,
64,
65,
68,
72,
73,
76,
79,
82,
86,
87,
91,
94,
97,
100,
106,
110,
112,
114,
117,
121,
123,
125,
126,
131,
133,
135,
137,
143,
147,
150,
153,
158,
161,
163,
168,
169,
170,
172,
174,
176,
177,
180,
181,
182,
185,
186,
189,
194,
196,
198,
201,
205,
207,
209,
210,
211,
215,
218,
219,
221,
223,
225,
227,
228,
230,
232,
236,
239,
241,
244,
245,
248,
249,
251,
259,
264,
270,
273,
277,
282,
286,
290,
294,
297,
298,
299]
Portiaspeaks2 = []
array3 = []
array4 = []
array5 = []
array6 = []
array7 = [5,
15,
24,
36,
46,
55,
64,
81,
91,
100,
110,
125,
137,
146,
174,
181,
186,
192,
199,
208,
212,
232,
273,
290,
296
]
array8 = []
indexarray = []

f = open('dump.csv')
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

# for i in range(len(array)):
#             if int(array[i]) < 750:
#                 array[i] = array[i-1]

for i in range(len(array)-1):
            entry = (int(array[i+1]) - int(array[i]))
            array2.append(entry)
	

for i in range(len(array2)-1):
	if int(array2[i]) >= 0 and int(array2[i+1]) < 0:
		entry = 1
		array3.append(array[i+1])
		array4.append(array[i+1])
	elif int(array2[i]) <= 0 and int(array2[i+1]) > 0:
		entry = 1
		array3.append(array[i+1])
		array4.append(array[i+1])
	else:
		entry = 0
		array3.append(min(array))
array3.insert(0,min(array3))

print(array4)


#local maxima
for i in range(len(array4)-2):
	if int(array4[i+1]) > int(array4[i]) and int(array4[i+1]) > int(array4[i+2]):
		array5.append(array4[i+1])

##print(array5)
minimum = min(array3)
index = 0
for i in range(len(array3)):

	if array3[i] is array5[index]:
		array6.append(array5[index])
		indexarray.append(i)
		if index < len(array5)-1:
			print(array5[index])
			index = index +1
	else:
		array6.append(minimum)

##print(array6)
print(indexarray)

index2 = 0
for i in range(len(array3)):

	if i is array7[index2]:
		array8.append(array[i])
		if index2 < len(array7)-1:
			index2 = index2 +1
	else:
		array8.append(minimum)
print(array8)

index2 = 0
for i in range(len(array)):

	if i is Portiaspeaks[index2]:
		Portiaspeaks2.append(array[i])
		if index2 < len(Portiaspeaks)-1:
			index2 = index2 +1
	else:
		Portiaspeaks2.append(minimum)
print(array8)

print("Length of Portiaspeaks",len(Portiaspeaks))


plt.figure(1)
plt.subplot(3,1,1)
plt.plot(array)
plt.plot(Portiaspeaks2)
##plt.plot(array6)

plt.subplot(3,1,2)
# plt.plot(array)
# plt.plot(array8)
plt.plot(array2)
plt.subplot(3,1,3)
# plt.plot(array8)
# plt.plot(array6)
plt.plot(Portiaderivates)
plt.plot()
# plt.ylabel('some numbers')
plt.show()
