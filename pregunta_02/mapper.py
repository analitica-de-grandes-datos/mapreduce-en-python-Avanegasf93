#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada estándar

def purpose_amount(x):
    return x[3] + "*" + x[4]  # Concatena el cuarto elemento de la lista 'x', un asterisco y el quinto elemento

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    result = line.split(',')  # Divide la línea en una lista utilizando ',' como separador
    print(purpose_amount(result))  # Imprime el resultado de la función 'purpose_amount' aplicada a la lista 'result'
