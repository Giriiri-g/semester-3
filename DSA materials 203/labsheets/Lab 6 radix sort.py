def countingSort(arr, exp1):
     n = len(arr)
     output = [0] * (n)
     count = [0] * (10)
     for i in range(0, n):
          index = arr[i] // exp1
          count[index % 10] += 1

     for i in range(1, 10):
          count[i] += count[i - 1]

     i = n - 1
     while i >= 0:
          index = arr[i] // exp1
          output[count[index % 10] - 1] = arr[i]
          count[index % 10] -= 1
          i -= 1
     i = 0
     for i in range(0, len(arr)):
          arr[i] = output[i]


def radixSort(arr):
     max1 = max(arr)
     exp = 1
     i=0
     while max1 / exp >= 1:
          i += 1
          countingSort(arr, exp)
          print(f"Array after {i}th Pass to Counting Sort: {arr}")
          exp *= 10


arr = [432,8,530,90,88,231,11,45,677,199]
print("Array Before Sorting: ")
for i in range(len(arr)):
     print(arr[i], end=", ")
print("\n\n")

radixSort(arr)

print("\n\nArray after Sorting: ")
for i in range(len(arr)):
     print(arr[i], end=", ")
