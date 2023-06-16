#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar

if __name__ == '__main__':  # Comprueba si el script se ejecuta directamente (no como módulo)

    curkey = None  # Variable para almacenar la clave actual
    total = 0  # Variable para almacenar el total acumulado

    for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar

        key, val = line.split("\t")  # Divide la línea en clave y valor utilizando el tabulador como separador
        val = int(val)  # Convierte el valor a entero

        if key == curkey:  # Si la clave actual es igual a la clave procesada anteriormente
            total += val  # Incrementa el total acumulado con el valor actual
        else:
            if curkey is not None:  # Si la clave actual no es None (es decir, no es la primera línea)
                # Escribe en la salida estándar la clave anterior y el total acumulado
                sys.stdout.write("{}\t{}\n".format(curkey, total))

            curkey = key  # Actualiza la clave actual con la nueva clave
            total = val  # Reinicia el total acumulado con el nuevo valor

    # Escribe en la salida estándar la última clave y el total acumulado
    sys.stdout.write("{}\t{}\n".format(curkey, total))
