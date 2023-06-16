#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar

if __name__ == '__main__':  # Comprueba si el script se ejecuta directamente (no como módulo)

    for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
        lista = line.split(' ')  # Divide la línea en una lista utilizando el espacio como separador

        # Escribe en la salida estándar el formato "elemento     1" utilizando el primer elemento de la lista
        sys.stdout.write("{}\t1\n".format(lista[0]))
