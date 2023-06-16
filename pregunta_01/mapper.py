#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada estándar

def purpose_amount(x):
    return x[2]  # Devuelve el tercer elemento de la lista 'x'

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    result = line.split(',')  # Divide la línea en una lista utilizando ',' como separador
    print(purpose_amount(result))  # Imprime el tercer elemento de la lista 'result'

