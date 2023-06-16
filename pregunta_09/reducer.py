#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar
biggest_purposes = []  # Lista para almacenar los propósitos más grandes
count_elements_col_3 = 0  # Contador para controlar el número de elementos procesados en la columna 3

def set_bigger_purpose(array_purposes, actual_element):
    actual_element = actual_element.replace("\n", "")  # Elimina el salto de línea al final del elemento
    biggest_purposes.append(actual_element)  # Agrega el elemento a la lista de propósitos más grandes
    return array_purposes

def sortByColumn3(element):
    return int(element.split(";")[0])  # Función para ordenar los elementos por el valor de la columna 3

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    set_bigger_purpose(biggest_purposes, line)  # Llama a la función para agregar el elemento a la lista

biggest_purposes.sort(key=sortByColumn3)  # Ordena la lista de propósitos más grandes por el valor de la columna 3

for purpose in biggest_purposes:  # Itera sobre cada propósito en la lista
    count_elements_col_3 += 1  # Incrementa el contador de elementos en la columna 3
    element = purpose.split(";")  # Divide el propósito en sus componentes utilizando el punto y coma como separador
    print(element[1] + "   " + element[2] + "   " + element[0])  # Imprime los componentes en el formato especificado
    if count_elements_col_3 > 5:  # Si se han procesado más de 5 elementos en la columna 3, detiene el bucle
        break
