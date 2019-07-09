'''
According to Wikipedia "Merge sort (also commonly spelled mergesort) is an O (n log n) comparison-based sorting algorithm. Most implementations produce a stable sort, which means that the implementation preserves the input order of equal elements in the sorted output."

Algorithm:
Conceptually, a merge sort works as follows :

Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted).
Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list.
'''

def mergesort(arr):
  arr_length = len(arr)
  if(arr_length > 1):
    middle = (arr_length)//2
    left = arr[:middle]
    right = arr[middle:]
    mergesort(left)
    mergesort(right)
    left_length = len(left)
    right_length = len(right)
    i=j=k=0
    while i < left_length and j < right_length:
      if(left[i] < right[j]):
        arr[k] = left[i]
        i += 1
      else:
        arr[k] = right[j]
        j += 1
      k += 1
    # update remaining sorted elements in left
    while i < left_length:
      arr[k] = left[i]
      i += 1
      k += 1
    # update remaining sorted elements in right
    while j < right_length:
      arr[k] = right[j]
      j += 1
      k += 1


if __name__ == '__main__':
  arr = [4,2,1,5,6,8,7,3]
  # arr = [4,2,1,5,3]
  # arr = [4,2,1,3]
  # arr = [2,1,3]
  print("Initial arr: %s" % arr)
  mergesort(arr)
  print("ater merge sort arr: %s" % arr)
