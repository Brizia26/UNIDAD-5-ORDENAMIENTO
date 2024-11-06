
def letters(arr):
    n = len(arr)
    for i in range(n - 1):
        print(f"Iteración {i + 1}:")
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(arr)  
        print()  
    return arr

letras = ['d', 'a', 'e', 'b', 'c']
print("Lista original:", letras)
print("Lista ordenada:", letters(letras))


