def zigzag(arr):
    operator = False  # Indicates "<"
    for i in range(len(arr)-1):
        if operator == False:
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if operator == True:
            if arr[i] < arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
        if operator == True:
            operator = False
        else:
            operator = True

    return arr

arr = [4, 3, 7, 8, 6, 2, 1]
zarr = zigzag(arr)
print zarr