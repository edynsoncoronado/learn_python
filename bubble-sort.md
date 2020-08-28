# Bubble Sort

![Algorithm](src/image/Bubble-sort.gif)

## Python
```python
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [190, 1200, 1, 2, 4, 55, 1000, 6, 800]
bubbleSort(array)

for i in range(len(array)):
    print("%d"%array[i])
```