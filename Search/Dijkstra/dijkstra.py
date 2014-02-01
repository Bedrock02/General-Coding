#in order to run this algorithm simply
#cat cities.in | dijkstra.py

import hheap
import sys
from collections import defaultdict


def DijkstraCity(input = sys.stdin):
	
	TravelHeap = hheap.hheap()
	Neghbrs = defaultdict(dict)

	#----------Start of importing cities
	line = sys.stdin.readline()
	#set up the Neghbrs dictionary
	splitInput = line.split()
	TravelHeap[splitInput[0]] = 0
	Neghbrs[splitInput[0]]

	for x in splitInput[1:]:
		Neghbrs[x]
		TravelHeap[x] = float("+inf")

	#read in next line
	line = sys.stdin.readline()
	#Take in Neighbors
	while line != "":
		splitInput = line.split()
		Neghbrs[splitInput[0]][splitInput[1]] = splitInput[2]
		Neghbrs[splitInput[1]][splitInput[0]] = splitInput[2]
		line = sys.stdin.readline()
	#------------End of importing cities


	while len(TravelHeap) !=0 :
		
		poppedCity = TravelHeap.pop()
		TravelHeap.Display(poppedCity)
		for others in Neghbrs[poppedCity[2]]:
			TravelHeap.update_if_better(others,poppedCity[1]+int(Neghbrs[poppedCity[2]][others]),poppedCity[2])
			del Neghbrs[others][poppedCity[2]]

if __name__ == '__main__':
	DijkstraCity()