#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar

def clear_spaces(x):
    x = x.replace("\n", "")  # Elimina el salto de línea
    x = x.replace("\r", "")  # Elimina el retorno de carro
    x = x.replace("\t", "")  # Elimina las tabulaciones
    return x

def purpose_amount(x):
    return clear_spaces(x[2]) + ";" + clear_spaces(x[0]) + ";" + clear_spaces(x[1])
    # return int(clear_spaces(x[2]))

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    line = line.replace("'", "")  # Elimina las comillas simples
    result = line.split('   ')  # Divide la línea en una lista utilizando tres espacios consecutivos como separador
    print(purpose_amount(result))  # Imprime el resultado de aplicar la función purpose_amount a la lista resultante
