def findMaxMin(list):
	#Check if max and min are equal first
	if min(list) == max(list):
		return [min(list)]
	return [min(list),max(list)]

myList = [3,3,4,6,5,6,6]

if __name__ == "__main__":
	print (findMaxMin (myList))
