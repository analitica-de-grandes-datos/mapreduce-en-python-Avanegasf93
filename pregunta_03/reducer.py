#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada estándar

for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
    line = line.replace("\n", "")  # Elimina los saltos de línea de la línea actual
    if '*' in line:  # Verifica si la línea contiene un asterisco
        # Imprime la línea dividida en dos partes intercambiadas utilizando el asterisco como separador
        print(line.split("*")[1] + "," + line.split("*")[0])
