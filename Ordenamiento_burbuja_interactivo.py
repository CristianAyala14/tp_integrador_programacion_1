def burbuja(arr):
    n = len(arr)
    
    # Mostramos el array inicial
    print(f"Array inicial: {arr}")
    
    for i in range(n):
        # Creamos una copia del array para mostrar cambios
        arr_copia = arr.copy()
        
        # Bandera para verificar si hubo intercambios
        hay_cambios = False
        
        # Recorremos desde el primer elemento hasta el (n-i-1)ésimo
        for j in range(0, n - i - 1):
            # Si el elemento actual es mayor que el siguiente
            if arr[j] > arr[j + 1]:
                # Intercambiamos los elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                hay_cambios = True
        
        # Mostramos el estado después de cada iteración
        print(f"\nIteración {i+1}:")
        print(f"Estado final: {arr}")
        
        # Si no hubo cambios en la iteración, el array ya está ordenado
        if not hay_cambios:
            print("\nEl array ya está ordenado!")
            break
    
    return arr

# Ejemplo con números desordenados
numeros = [30,16,89,1,47,36,24,]
resultado = burbuja(numeros)
print(f"\nArray final ordenado: {resultado}")

# Puedes modificar esta lista para probar con diferentes números
mi_lista = [5, 2, 8, 1, 9]
print("\nProbando con otra lista:")
burbuja(mi_lista)