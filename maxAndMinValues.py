def findMaxMin(list):
	#Check if max and min are equal first
	if min(list) == max(list):
		return [min(list)]
	return [min(list),max(list)]