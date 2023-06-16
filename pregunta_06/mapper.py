#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    # Iterar sobre cada línea de entrada en la entrada estándar
    for line in sys.stdin:
        # Eliminar los espacios en blanco al inicio y al final, y reemplazar el guión por un espacio
        lista = line.strip().replace('-', ' ').split(' ')
        
        # Escribir el primer y octavo elemento de la lista separados por un tabulador en la salida estándar
        sys.stdout.write("{}\t{}\n".format(lista[0], lista[8]))
