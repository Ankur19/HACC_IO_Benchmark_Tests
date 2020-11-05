import os
import pandas as pd

columns = ["Bandwidth", "Size", "MaxTime", "ReadWrite", "NumParticles", "NumProcesses"]
numParticles = [10, 25, 50, 100, 250, 500, 1000]
numProcesses = [1, 2, 3, 4]
folders = ["1","2","3","4","5"]

def processTxt(file):
	df = pd.DataFrame(columns = columns)
	bandwidth = []
	size = []
	maxTime = []
	readWrite = []
	particle = []
	process = []
	pIdx = 0
	partIdx = 0
	for line in file:
		if "READ" in line:
			text = line.split(" ")
			bandwidth.append(text[4])
			size.append(text[6])
			maxTime.append(text[8])
			readWrite.append("Read")
			particle.append(str(numParticles[partIdx]*100000))
			process.append(str(numProcesses[pIdx]))
			pIdx+=1
			if pIdx==4:
				pIdx = 0
				partIdx+=1
		elif "WRITE" in line:
			text = line.split(" ")
			bandwidth.append(text[4])
			size.append(text[6])
			maxTime.append(text[8])
			readWrite.append("Write")
			particle.append(str(numParticles[partIdx]*100000))
			process.append(str(numProcesses[pIdx]))
		
	df[columns[0]] = [float(i) for i in bandwidth]
	df[columns[1]] = [int(i) for i in size]
	df[columns[2]] = [float(i) for i in maxTime]
	#df[columns[3]] = readWrite
	df[columns[4]] = [int(i) for i in particle]
	df[columns[5]] = [int(i) for i in process]

	return df


def processResults():
	dirs = ["localResults", "volumeResults", "bindMountResults"]

	for dir in dirs:
		allDfs = []
		for fold in folders:
			with open(dir+"/" + fold + "/result.txt", 'r') as file:
				df = processTxt(file)
				allDfs.append(df)
		df = pd.concat(allDfs).groupby(level=0).mean()
		df.to_csv(dir+".csv")

if __name__=="__main__":
	processResults()