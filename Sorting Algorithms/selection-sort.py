# Average time complexity = O(N^2)
def selection_sort(arr, n):
    for i in range(n-2):
        i_min = i
        for j in range(i+1, n-1):
            if arr[j] < arr[i_min]:
                i_min = j

        # swap
        arr[i], arr[i_min] = arr[i_min], arr[i]


x = [3, 4, 1, 7, 5, 6, 9, 10]
selection_sort(x, len(x))
print(x)
