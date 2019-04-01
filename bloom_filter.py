#Python 2 program
#Got started with help from: 
#https://www.geeksforgeeks.org/bloom-filters-introduction-and-python-implementation/
#Went route of using built in bloom features since the scope of what I would use 
#a password protected website aligns with this strengh.
import math
# Imports murmur3 hash function most standard for hasing in python.
import mmh3
#for file i/o
import sys
import os
import time
from bitarray import bitarray


class BloomFilter(object):
	#initializing the variables
	def __init__(self, dictSize, hashCount):
		super(BloomFilter, self).__init__()
		self.dictSize = dictSize
		self.bitarray = bitarray(self.dictSize)
		self.bitarray.setall(0)
		self.hashCount = hashCount
	#for adding items into the filter to tell if it's maybe good or not.
	def add(self, entry):
		takesIn = []
		for i in range(self.hashCount):
			takesIn = mmh3.hash(entry, i) % self.dictSize
#			takesIn.append(takesIn)
			self.bitarray[takesIn] = True

	def search(self, entry):
		for i in range(self.hashCount):
			takesIn = mmh3.hash(entry, i) % self.dictSize
			if self.bitarray[takesIn] == False:
				return "maybe"
			return "no"


#Got some help with file i/o
#dictSize = 623518 lines in dictionary.txt provided.
#dictSize is about 2^16, so we'll use 2^32 for the PW space.
#inputPW is password inputs from input PW's to be tested
def makeBloom(hashCount, inputPW, outPutFile):
	pwSpace = 2**32
	bFilter = BloomFilter(pwSpace, hashCount)
	#file i/o to fill table with dictonary's badPW list
	dictionary = open(sys.argv[2]).read().splitlines()
	for badPW in dictionary:
		bFilter.add(badPW)
	#write to output file(s)
	output = open(outPutFile, 'w+')
	for badPW in inputPW:
		output.write(bFilter.search(badPW) + '\n')

def main(): 
	
	inputPW = open(sys.argv[4]).read().splitlines()
	inputPW.pop(0) 
#First element is number of passwords in the list,
#so pop it not to read it as a PW
	Time3 = time.clock()
	makeBloom(3, inputPW, sys.argv[6])
	Time5 = time.clock()
	makeBloom(5, inputPW, sys.argv[7])
	print ("Ran passwords Time 3 & 5 are", Time3, Time5)

if __name__ == "__main__": main()
