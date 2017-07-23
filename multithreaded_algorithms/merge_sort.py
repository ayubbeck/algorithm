import sys
import threading

class MergeSort:
    def __init__(self, arr):
        self.arr = arr
        self.merge_sort(self.arr, 0, len(arr) - 1)

    def merge_sort(self, arr, p, r):
    	if p < r:
            # find the split point
            q = (p + r) / 2
            # spawn the left half of array on a seperate thread
            x = threading.Thread(name='merge_sort', target=self.merge_sort, args=(arr, p, q))
            x.start()
            # spawn the right half of array on a seperate thread
            y = threading.Thread(name='merge_sort', target=self.merge_sort, args=(arr, q+1, r))
            y.start()
            # sync
            x.join()
            y.join()
            # merge
            self.merge(arr, p, q, r)

    def merge(self, arr, p, q, r):
        # get length for each side
        left_length = q - p + 1
        right_length = r - q
        # populate both right and left arrays and append infinity to both
        left_array = [arr[p + i] for i in range(left_length)] + [sys.maxint]
        right_array = [arr[q + i + 1] for i in range(right_length)] + [sys.maxint]
        # merge
        i = 0
        j = 0
        for k in range(left_length + right_length):
        	if left_array[i] <= right_array[j]:
        		arr[p + k] = left_array[i]
        		i = i + 1
        	else:
        		arr[p + k] = right_array[j]
        		j = j + 1
