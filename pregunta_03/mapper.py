#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada estándar

def clear_spaces(x):
    x = x.replace("\n", "")  # Elimina los saltos de línea
    x = x.replace("\r", "")  # Elimina los retornos de carro
    return x  # Devuelve la cadena 'x' sin espacios adicionales

def purpose_amount(x):
    return clear_spaces(x[1]) + "*" + clear_spaces(x[0])  # Concatena el segundo elemento de la lista 'x', un asterisco y el primer elemento

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    result = line.split(',')  # Divide la línea en una lista utilizando ',' como separador
    print(purpose_amount(result))  # Imprime el resultado de la función 'purpose_amount' aplicada a la lista 'result'
