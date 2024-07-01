'''1->Selection Sort Algorithm'''
def selectionSort(arr, n):
    for i in range(n-1):
        mini = i
        for j in range(i + 1, n):
            if arr[j] < arr[mini]:
                mini = j
        arr[i],arr[mini]=arr[mini],arr[i]

arr = [64, 0, 12, 76, -1]
n = len(arr)
selectionSort(arr, n)
print('Sorted Array:',arr)
'''2->Bubble Sort'''
def bubbleSort(arr, n):
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
arr = [5, 1, 4, 2, 8]
n = len(arr)
bubbleSort(arr, n)
print("Sorted array is:")
print(arr)
'''3-Insertion Sort Algorithm'''
# def insertionSort(arr, n):
#     for i in range(1, n):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j] :
#                 arr[j + 1] = arr[j]
#                 j -= 1
#         arr[j + 1] = key
# arr = [12, 11, 13, 5, 6]
# n = len(arr)
# insertionSort(arr, n)
# print('Sorted Array:')
# print(arr)
'''4-Merge Sort Algorithm'''
def MergeSort(arr):
  if len(arr) <= 1:
    return arr
  mid = len(arr)//2
  left = MergeSort(arr[:mid])
  right = MergeSort(arr[mid:])
  return Merge(left,right)
def Merge(left, right):
  result = []
  i, j = 0, 0
  while i<len(left) and j<len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1
  result += left[i:]
  result += right[j:]
  return result
arr = [1,0,9,65,7,3,4,-1]
print(MergeSort(arr)) 
'''5->Quicksort Algorithm'''
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quicksort(array, low, pi - 1)
        quicksort(array, pi + 1, high)
arr = [10, 7, 8, 9, 1, 5]
n = len(arr) - 1
quicksort(arr, 0, n)
print('Sorted array:',arr)

'''6->Implementation of Linear Search'''
# def Linearsearch(arr,target):
#     for i in range(len(arr)):
#         if (arr[i] == target):
#             return i
#     return -1
# arr = [2, 3, 4, 10, 40]
# target = 40
# result = Linearsearch(arr,target)
# print("Element is present at index", result)
'''7->Implementation of Binary Search** TC:O(logN) SC:O(1)'''
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end ) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1      
    return -1 
arr = [2, 4, 6, 8, 10, 12, 14]
target = 12
result = binary_search(arr, target)
print("Element is present at index", result)
'''7->Recursive Binary Search Algorithm** 
Time Complexity: SC:O(1)
Best Case: O(1)
Average Case: O(log N)
Worst Case: O(log N)'''
def binarySearch(arr, start, end, target):
  mid = (start + end) // 2
  if start <= end:
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      return binarySearch(arr, mid+1, end, target)
    else:
      return binarySearch(arr, start, mid-1, target)
  return -1
arr = [2, 3, 4, 10, 40]
target = 40
result = binarySearch(arr, 0, len(arr)-1, target)
print("Element is present at index", result)
    
  
