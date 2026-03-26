#ProcessData.py
#Name:Riley Mayfield
#Date:3/25
#Assignment:Lab 8
#Purpose: Develop understanding of using .csv files

import random


def getID(info):
  initial = str.lower(info[0][0])
  last = str.lower(info[1])
  while len(last) < 5:
    last = last+"x"
  number = info[3][-3:]

  return initial + last + number

def getMajorYear(info):
  major = str.upper(info[6][0:3])

  year = info[5][1]
  if year == "r":
    year = "FR"
  elif year == "o":
    year = "SO"
  elif year == "u":
    year = "JR"
  else:
    year = "SR"
  
  return major + "-" + year

def getFirst(info):
  first = info[0]
  return first

def getLast(info):
  last = info[1]
  return last

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  for line in inFile:
    info = line.split(" ")
    userID = getID(info)
    majorYear = getMajorYear(info)
    last = getLast(info)
    first = getFirst(info)
    outFile.write(last + "," + first + "," + userID + "," + majorYear + "\n")



  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
