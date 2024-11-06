
def letraas(s):

    arr = list(s)
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
        
        print(f"Iteración {i + 1}: {''.join(arr)}")
    
    sorted_string = ''.join(arr)
    return sorted_string

s = "nuevayork"
print("Ordenamiento por selección (ascendente):")
sorted_string = letraas(s)
print(f"\nCadena ordenada: {sorted_string}")


