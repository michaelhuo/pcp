def swap(A, i, j):

	temp = A[i]
	A[i] = A[j]
	A[j] = temp


# Partition using Hoare's Partitioning scheme
def Partition(a, low, high):

	pivot = a[low]
	(i, j) = (low - 1, high + 1)

	while True:

		while True:
			i = i + 1
			if a[i] >= pivot:
				break

		while True:
			j = j - 1
			if a[j] <= pivot:
				break

		if i >= j:
			return j

		swap(a, i, j)


# Quicksort routine
def quickSort(a, low, high):

	# base condition
	if low >= high:
		return

	# rearrange the elements across pivot
	pivot = Partition(a, low, high)

	# recur on sublist containing elements less than the pivot
	quickSort(a, low, pivot)

	# recur on sublist containing elements more than the pivot
	quickSort(a, pivot + 1, high)


# Quick Sort using Hoare's Partitioning scheme
if __name__ == '__main__':

	a = [9, -3, 5, 2, 6, 8, -6, 1, 3]
	a = [9, -3]

	quickSort(a, 0, len(a) - 1)

	# print the sorted list
	print(a)
