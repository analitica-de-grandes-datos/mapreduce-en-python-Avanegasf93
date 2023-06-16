#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada estándar
biggest_purposes = {}  # Crea un diccionario vacío llamado 'biggest_purposes' para almacenar los propósitos más grandes

def set_bigger_purpose(dictionary_purposes, actual_element):
    # Incrementa el contador para el elemento actual en el diccionario de propósitos más grandes
    dictionary_purposes[actual_element] = int(dictionary_purposes.get(actual_element) or 0) + 1
    return dictionary_purposes  # Devuelve el diccionario actualizado de propósitos más grandes

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    set_bigger_purpose(biggest_purposes, line.replace("\n", ""))  # Llama a la función para establecer el propósito más grande

for purpose, amount in biggest_purposes.items():  # Itera sobre cada par de clave-valor en el diccionario de propósitos más grandes
    print(purpose + "    " + str(amount))  # Imprime el propósito y la cantidad correspondiente

