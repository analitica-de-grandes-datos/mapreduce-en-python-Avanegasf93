#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == "__main__":
    curkey = None  # Variable para almacenar la clave actual
    numeros = ""  # Variable para almacenar los números asociados a la clave actual

    for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
        key, val = line.split("\t")  # Divide la línea en clave y valor utilizando el tabulador como separador
        val = val.strip()  # Elimina los espacios en blanco alrededor del valor

        if key == curkey:  # Si la clave es igual a la clave actual
            numeros = numeros + "," + str(int(val))  # Agrega el valor a la lista de números asociados a la clave actual
        else:
            if curkey is not None:  # Si la clave actual no es None (es decir, no es la primera clave)
                sys.stdout.write("{}\t{}\n".format(curkey, numeros))  # Imprime la clave y la lista de números asociados

            curkey = key  # Actualiza la clave actual con la nueva clave
            numeros = str(int(val))  # Reinicia la lista de números con el nuevo valor

    sys.stdout.write("{}\t{}\n".format(curkey, numeros))  # Imprime la última clave y la lista de números asociados
