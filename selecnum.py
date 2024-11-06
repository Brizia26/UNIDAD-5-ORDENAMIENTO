

def desc(arr):
    n = len(arr)
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_index]:
                max_index = j
        
        arr[i], arr[max_index] = arr[max_index], arr[i]
        
        print(f"Iteración {i + 1}: {arr}")

arr = [64, 25, 12, 22, 11]
print("\nOrdenamiento por selección ( forma descendente):")
desc(arr)


