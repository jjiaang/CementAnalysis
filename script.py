import os
import sys
from tkinter import filedialog
from tkinter import*

def getFile():
    fileName = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    return fileName

def specifyOutputFile():
    print("Enter the name of the output file, this will create a new file. Remember to use .txt at the end.")
    outputFile = input()
    f = open(outputFile, "x")

    return outputFile

def main():
    cement = getFile()
    stages = getFile()
    outputFile = specifyOutputFile()
    fileReadWrite(cement,stages,outputFile)

def fileReadWrite(cement,stages,outputFile):

    medians = {}

    with open(stages, 'r') as f:
        stagesArray = [line.split() for line in f]

    with open(cement, 'r') as f:
        cementArray = [line.split() for line in f]

    for i in range(len(stagesArray)):

        initialSum = 0
        counter = 0

        avgEnd = float(stagesArray[i][1])
        avgStart = float(stagesArray[i][2])

        totalAvg = float( (avgEnd + avgStart) / 2)

        for j in range(2,len(cementArray)):

            if (avgEnd >= float(cementArray[j][0]) and avgStart <= float(cementArray[j][0])):
                initialSum += float(cementArray[j][1])

                counter += 1

        avg = initialSum / counter

        medians[totalAvg] = avg

    print(medians)

    cement2 = cementArray

    del cement2[0]
    del cement2[0]

    with open(outputFile, 'w') as f:
        for item in cement2:

            if float(item[0]) in medians:

                f.write("%s\n" % (str(item[0]) + "	 " + str(medians[float(item[0])])))
main()