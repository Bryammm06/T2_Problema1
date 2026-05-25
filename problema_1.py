import random

def encontrar_max_min_multiplos_3(arreglo, indice=0, max_val=None, min_val=None):

    if indice == len(arreglo):
        return max_val, min_val
    
    val_actual = arreglo[indice]
    
    ###if val_actual /3 ==0;
    ###if max_val is None:
    ###max_val = val_actual
    ###min_val = val_actual
    ##else:
    ###if val_actual > max_val:
    ###max_val = val_actual
    ###if val_actual < min_val:
    ###min_val = val_actual
    ##NO FUNCIONÓ.

    if val_actual % 3 == 0:
        if max_val is None:
            max_val = val_actual
            min_val = val_actual
        else:
            if val_actual > max_val:
                max_val = val_actual
            if val_actual < min_val:
                min_val = val_actual
                
    ####RECURSIDAD ALPLICADA
    return encontrar_max_min_multiplos_3(arreglo, indice + 1, max_val, min_val)

def calcular_promedio_recursivo(arreglo):
    
    max_val, min_val = encontrar_max_min_multiplos_3(arreglo)
    if max_val is None or min_val is None:
        return None
    
    promedio = (max_val + min_val) / 2
    return promedio

    ###MAIN
if __name__ == "__main__":
    print("---/---PROBLEMA 1---/---")

    try:
        tamanio = int(input("Ingrese el tamaño del arreglo: "))
        if tamanio <= 0:
            print("Por favor, ingrese un número mayor a 0.")
            exit()
    except ValueError:
        print("Entrada inválida. Debe ingresar un número entero.")
        exit()
        
    ###ARREGLO NROS ALEATORIOS
    arreglo_usuario = [random.randint(10, 9999) for _ in range(tamanio)]
    print(f"\nArreglo generado:\n{arreglo_usuario}\n")
    
    ###PROMEDIO
    resultado = calcular_promedio_recursivo(arreglo_usuario)
    
    ###RESULTADO
    if resultado is not None:
        print(f"Resultado del promedio (Máx + Mín) / 2 de múltiplos de 3: {resultado}")
    else:
        print("No se encontraron números múltiplos de 3 en el arreglo generado.")