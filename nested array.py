
arr = []
lid=[2,3,4]
for i in range(3):
	arr.append([])
	for j in range(2):
		arr[i].append([])
		for h in range(3):
			arr[i][j].append(2)
		with open("C:/data set/danmark/13.csv") as f2:
			for line3 in f2:
				if "209223000" in line3:
					line3 = line3.split(",")
					arr[i][j][0] = line3[0]
					arr[i][j][1] = line3[1]
					arr[i][j][2] = line3[2]


x=np.array(arr)
print(x.shape)
y=[12,5,4,8]
y=np.array(y)
x=np.array(arr)
print(x.shape)
for i in range(len(x)):
	print(X[i], y[i])

print(x)

cinemas = []

for k in range(7):
    cinema = []
    for j in range(3):
        column = []

        for i in range(2):
            column.append(0)

        cinema.append(column)
    cinemas.append(cinema)

with open("C:/data set/danmark/13.csv") as f2:
	for line3 in f2:
		if "209223000" in line3:
			line3=line3.split(",")
			cinemas[0][0][0]=int(1458)
			cinemas[0][1][0]=line3[3]
			cinemas[0][0][0]=45

print(cinemas)


x=np.array(cinemas)
print(x.shape)
print(x)

#################################
