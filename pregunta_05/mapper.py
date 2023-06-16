#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar

if __name__ == '__main__':  # Comprueba si el script se ejecuta directamente (no como módulo)

    for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
        lista = line.strip().replace('-', ' ').split(' ')  # Elimina los espacios en blanco al inicio y final de la línea, reemplaza los guiones por espacios y divide la línea en una lista utilizando los espacios como separadores

        # Escribe en la salida estándar el formato "elemento     1" utilizando el quinto elemento de la lista
        sys.stdout.write("{}\t1\n".format(lista[4]))
