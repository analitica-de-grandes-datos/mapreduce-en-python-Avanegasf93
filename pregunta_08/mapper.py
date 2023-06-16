#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar

if __name__ == '__main__':

    for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
        lista = line.strip().replace('-', ' ').split(' ')  # Elimina los espacios en blanco al principio y al final, reemplaza los guiones por espacios y divide la línea en una lista utilizando los espacios como separador
        sys.stdout.write("{}\t{}\n".format(lista[0], lista[8]))  # Escribe en la salida estándar el primer y noveno elemento de la lista separados por un tabulador y seguido de un salto de línea
