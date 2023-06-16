#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada estándar
biggest_purposes = {}  # Crea un diccionario vacío llamado 'biggest_purposes' para almacenar los propósitos más grandes

def set_bigger_purpose(dictionary_purposes, actual_element):
    element_array = actual_element.split("*")  # Divide el elemento actual en una lista utilizando '*' como separador
    # Establece el valor más grande entre el valor actual del propósito en el diccionario y el valor en la posición 1 de la lista
    dictionary_purposes[element_array[0]] = max(
        int(dictionary_purposes.get(element_array[0]) or 0), int(element_array[1]))
    return dictionary_purposes  # Devuelve el diccionario actualizado de propósitos más grandes

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    set_bigger_purpose(biggest_purposes, line)  # Llama a la función para establecer el propósito más grande

for purpose, amount in biggest_purposes.items():  # Itera sobre cada par de clave-valor en el diccionario de propósitos más grandes
    print(purpose + "\t" + str(amount))  # Imprime el propósito y la cantidad correspondiente con una tabulación
