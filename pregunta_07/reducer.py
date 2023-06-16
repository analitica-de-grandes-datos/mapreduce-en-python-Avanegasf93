#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar
biggest_purposes = {}  # Diccionario para almacenar los propósitos más grandes

def set_bigger_purpose(dictionary_purposes, actual_element):
    actual_element = actual_element.replace("\n", "")  # Elimina el carácter de salto de línea
    letter = actual_element.split(" ")[0]  # Obtiene la letra del propósito
    if str(dictionary_purposes.get(letter) or "") == "":
        # Si el propósito no está en el diccionario, agrega el elemento completo a ese propósito
        dictionary_purposes[letter] = str(dictionary_purposes.get(letter) or "") + actual_element.split(" ")[1]
    else:
        # Si el propósito ya existe en el diccionario, agrega el elemento con un asterisco como separador
        dictionary_purposes[letter] = str(dictionary_purposes.get(letter) or "") + "*" + actual_element.split(" ")[1]
    return dictionary_purposes

def sortByColumn3(element):
    return int(element.split(";")[0])  # Obtiene el valor numérico de la tercera columna separada por punto y coma

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    set_bigger_purpose(biggest_purposes, line)  # Llama a la función para agregar el elemento al diccionario de propósitos más grandes

for purpose, values_and_dates in biggest_purposes.items():  # Itera sobre cada propósito y su lista de valores y fechas
    elements = values_and_dates.split("*")  # Divide la lista en elementos individuales
    elements.sort(key=sortByColumn3)  # Ordena los elementos en función del valor numérico de la tercera columna
    biggest_purposes[purpose] = elements  # Actualiza el diccionario de propósitos más grandes con la lista ordenada
    for element in elements:  # Itera sobre cada elemento en la lista ordenada
        print(purpose + "   " + element.split(";")[1] + "   " + element.split(";")[0])  # Imprime el propósito, la fecha y el valor de cada elemento
