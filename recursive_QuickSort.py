import random
import time
start_time = time.time()

def QuickSort(array):
	if len(array) < 2:
		return array
	pivot = array[0]
	head = []
	tail = []
	for i in range(1, len(array)):
		if array[i] < pivot:
			head.append(array[i])
		else:
			tail.append(array[i])
	head = QuickSort(head)
	tail = QuickSort(tail)
	head.append(pivot)
	head.extend(tail)
	return  head

"""Test random numbers in range(x) with randit(y, z) size"""
randomlist = []
for i in range(0,3):
	n = random.randint(1,50000000000)
	randomlist.append(n)

print(QuickSort(randomlist))