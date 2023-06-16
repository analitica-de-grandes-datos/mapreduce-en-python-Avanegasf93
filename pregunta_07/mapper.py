#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar

def clear_spaces(x):
    x = x.replace("\n", "")  # Elimina los caracteres de salto de línea
    x = x.replace("\r", "")  # Elimina los caracteres de retorno de carro
    x = x.replace("\t", "")  # Elimina los caracteres de tabulación
    return x

def purpose_amount(x):
    return clear_spaces(x[0]) + " " + clear_spaces(x[2]) + ";" + clear_spaces(x[1]) 
    # Devuelve una cadena concatenando los elementos de la lista 'x' con espacios y un punto y coma

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    line = line.replace("'", "")  # Elimina las comillas simples de la línea
    result = line.split('   ')  # Divide la línea en una lista utilizando '   ' como separador
    print(purpose_amount(result))  # Imprime el resultado de la función 'purpose_amount' aplicada a la lista 'result'
