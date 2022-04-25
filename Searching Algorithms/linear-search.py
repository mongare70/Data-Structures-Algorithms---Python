def search(arr, target):
    for i in range(len(arr)):
        if target == arr[i]:
            return i
    
    return -1


array1 = [4, 10, 7, 8, 3, 7, 1, 20]
print(search(array1, 3))

