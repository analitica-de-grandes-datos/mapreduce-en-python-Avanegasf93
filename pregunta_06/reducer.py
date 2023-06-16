#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    curkey = None
    max_val = 0
    min_val = 0

    for line in sys.stdin:
        # Divide la línea en dos partes utilizando el carácter de tabulación como separador
        row = line.split("\t")
        key = row[0]
        val = float(row[1])

        if key == curkey:
            # Compara el valor actual con el máximo y mínimo actuales
            if val > max_val:
                max_val = val
            else:
                val = max_val

            if val < min_val:
                min_val = val
            else:
                val = min_val

        else:
            # Si la clave cambia, escribe la clave anterior junto con los valores máximo y mínimo en la salida estándar
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_val, min_val))

            # Actualiza la clave y los valores máximo y mínimo para la nueva clave
            curkey = key
            max_val = val
            min_val = val

    # Escribe la última clave junto con los valores máximo y mínimo en la salida estándar
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_val, min_val))
