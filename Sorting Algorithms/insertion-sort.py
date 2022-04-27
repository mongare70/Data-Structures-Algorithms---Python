# Average time complexity = O(N^2)
def insertion_sort(arr, n):
    for i in range(1, n-1):
        value = arr[i]
        hole = i

        while hole > 0 and arr[hole - 1] > value:
            arr[hole] = arr[hole-1]
            hole = hole - 1

        arr[hole] = value


x = [3, 4, 1, 7, 5, 6, 9, 10]
insertion_sort(x, len(x))
print(x)