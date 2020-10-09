import os
import pandas as pd

columns = ["Bandwidth", "Size", "MaxTime"]

def processTxt(file):
    df = pd.DataFrame(columns = columns)
    bandwidth = []
    size = []
    maxTime = []
    for line in file:
        if "READ" in line:
            text = line.split(" ")
            bandwidth.append(text[4])
            size.append(text[6])
            maxTime.append(text[8])
    df[columns[0]] = bandwidth
    df[columns[1]] = size
    df[columns[2]] = maxTime

    return df


def processResults():
    dirs = ["bindMountResults", "localResults", "volumeResults"]
    for dir in dirs:
        with open(dir+"/result.txt", 'r') as file:
            df = processTxt(file)
            df.to_csv(dir+".csv")

if __name__=="__main__":
    processResults()