
def insertion_numeros(arr):
    print("Lista original:", arr)
    for i in range(1, len(arr)):
        print(f"\nIteración {i}:")
        key = arr[i]
        j = i - 1
        print(arr)  
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)  
        arr[j + 1] = key
        print(arr)  
    print("\nLista ordenada:", arr)

numeros = [8, 4, 6, 2, 7,65, 1,0]
insertion_numeros(numeros)

