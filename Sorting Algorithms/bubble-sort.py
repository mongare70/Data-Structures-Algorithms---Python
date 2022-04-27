# Average time complexity = O(N^2)
def bubble_sort(arr, n):
    # after n-1 we are guaranteed to be sorted
    for j in range(1, n-1):

        # n-2 to prevent n+1 falling out of bound of list
        for i in range(n-2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]


x = [3, 4, 1, 7, 5, 6, 9, 10]
bubble_sort(x, len(x))

print(x)
