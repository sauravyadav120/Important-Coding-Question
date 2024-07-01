'''1->Sort the array of 0s, 1s, and 2s using o(n)'''	
def sort012(arr,n):
  lo = 0
  hi = n-1
  mid = 0
  while(mid<=hi):
    if arr[mid] == 0:
      arr[lo],arr[mid] = arr[mid],arr[lo]
      lo = lo + 1
      mid = mid + 1
    elif arr[mid] == 1:
      mid = mid + 1
    else:
      arr[mid],arr[hi] = arr[hi],arr[mid]
      hi = hi - 1
  return arr
def printArray(arr):
  for i in arr:
    print(i,end=" ")
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
n = len(arr)
printArray(sort012(arr, n))
'''2->find Largest sum contiguous Subarray [V.IMP] using Kadane's algorithm'''
def maxSubarraySum(arr , n):
    maxsum = -2
    currsum = 0
    for i in range(0 , n):
        currsum = currsum + arr[i]
        if(currsum > maxsum):
            maxsum = currsum
        if(currsum < 0):
            currsum = 0
    return maxsum
arr = [-2, -3, 4, -1, -2, 1, 5, -3]
n = len(arr)
print('Maximum contiguous sum is',maxSubarraySum(arr , n))
'''3.	Find maximum element in array '''
def max(arr,n):
    arr.sort()
    return arr[n-1]
arr = [10,334,44,6,7]
n = len(arr)
print(max(arr,n))
'''7.find kth smallest element in array.'''
def small(arr, k):
    arr.sort()
    return arr[k-1]
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(small(arr, k))

'''4 Write a program to rotate elements of an array to the left by a given number of positions.'''
def rotate_array(arr, k):
    return arr[k:] + arr[:k]

array = [1, 2, 3, 4, 5]
k = 2
print("Original array:", array)
print("Array after rotation:", rotate_array(array, k))

'''5.They gave me an array code to print the last element'''
arr = [1, 2, 3, 4, 5]
print(arr[-1])

'''6.Find array duplicate values.'''
def dupli(arr):
    s = set()
    duplicates = set()
    for i in arr:
        if i in s:
            duplicates.add(i)
        else:
            s.add(i)
    return list(duplicates)

arr = [1, 2, 2, 6, 7, 9, 10, 1]
print(dupli(arr))

'''Single Inheritance'''
class BaseClass:
    def method1(self):
        return "Method 1 from BaseClass"

class DerivedClass(BaseClass):
    def method2(self):
        return "Method 2 from DerivedClass"

obj = DerivedClass()
print(obj.method1())
print(obj.method2())  


'''Multiple Inheritance'''
class BaseClass1:
    def method1(self):
        return "Method 1 from BaseClass1"

class BaseClass2:
    def method2(self):
        return "Method 2 from BaseClass2"

class DerivedClass(BaseClass1, BaseClass2):
    def method3(self):
        return "Method 3 from DerivedClass"
obj = DerivedClass()

print(obj.method1())  
print(obj.method2())  
print(obj.method3()) 

'''Multilevel Inheritance'''
class BaseClass:
    def method1(self):
        return "Method 1 from BaseClass"

class IntermediateClass(BaseClass):
    def method2(self):
        return "Method 2 from IntermediateClass"

class DerivedClass(IntermediateClass):
    def method3(self):
        return "Method 3 from DerivedClass"
obj = DerivedClass()
print(obj.method1())
print(obj.method2())  
print(obj.method3())  
'''Hybrid Inheritance'''
class BaseClass:
    def base_method(self):
        return "Method from BaseClass"

class DerivedClass1(BaseClass):
    def method1(self):
        return "Method 1 from DerivedClass1"

class DerivedClass2(BaseClass):
    def method2(self):
        return "Method 2 from DerivedClass2"

class HybridClass(DerivedClass1, DerivedClass2):
    def hybrid_method(self):
        return "Method from HybridClass"

obj = HybridClass()
print(obj.base_method())  
print(obj.method1())     
print(obj.method2())      
print(obj.hybrid_method())  
