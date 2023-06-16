#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys  # Importa el módulo 'sys' para trabajar con la entrada y salida estándar
import operator  # Importa el módulo 'operator' para utilizar operaciones en el programa

if __name__ == '__main__':
    
    my_list = {}  # Diccionario para almacenar las letras y sus valores

    for line in sys.stdin:  # Itera sobre cada línea de la entrada estándar
        line = line.strip()  # Elimina los espacios en blanco al principio y al final de la línea
        letter, value = line.split('\t')  # Divide la línea en una letra y su valor utilizando el tabulador como separador
        
        if letter in my_list:  # Si la letra ya está en el diccionario
            my_list[letter].append(float(value))  # Agrega el valor a la lista correspondiente en el diccionario
        else:  # Si la letra no está en el diccionario
            my_list[letter] = []  # Crea una nueva lista vacía para esa letra
            my_list[letter].append(float(value))  # Agrega el valor a la lista recién creada
        
    for letter in my_list.keys():  # Itera sobre cada letra en el diccionario
        sum_letter = sum(my_list[letter])  # Calcula la suma de los valores de la letra
        aver_letter = sum(my_list[letter]) / len(my_list[letter])  # Calcula el promedio de los valores de la letra
        print('%s\t%s\t%s' % (letter, sum_letter, aver_letter))  # Imprime la letra, la suma y el promedio separados por tabuladores
