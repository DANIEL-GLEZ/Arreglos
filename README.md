# Arreglos
Arreglos bidimensionales en Java y Python
Explicación sobre el código (¿Qué hace?, ¿Para qué sirve? ¿Métodos usados?)

=== En Python ===
Creamos la clase Tienda con ventas predefinadas para cada mes y departamento (Ropa, Deportes, Juguetería). 
Creamos un diccionario ventas_mensuales donde cada clave es un departamento y el valor es una lista de 12 elementos (uno por cada mes)
Creamos agregar_ventas donde insertamos o actualizamos en un departamentos y mes especifico, en nuestro código tambien verifica si ambos son válidos, Si lo son, actualiza la venta en la posición correspondientes de la lista.
Creamos obtener_venta que sirve para buscar y devolver la venta (el valor) de un departamento y del mes especifico. Si excede los limites establecidos imprime un mensaje de error.
Creamos Borrar_venta donde elimina (pone en 0) la venta de un departamento y mes establecido que nosotros especificamos dentro del código, ponemos un mes y departamento si no supera los limites establecidos pone en 0 la venta que indicamos (como si se borrara).
Creamos mostrar_ventas donde nos muestra todos los departamentos y sus respectivas ventas las imprime indicandonos las ventas de cada departamento

=== En Java ===
Creamos un clase pública definida como Almacén: que define la estructura de la tienda con un arreglo bidimensional para las ventas.
Creamos el método agregarVenta: Donde insertamos o actualizamos una venta de un departamento y mes especificos.
Creamos obtenerVenta: Busca y devuelve el dato (la venta) del departamento y mes que especificamos.
Creamos borrarVenta: donde eliminamos (ponemos en valor 0) alguna venta y departamento.
Creamos el método mostrarVentas: donde nos muestra la venta de todos los departamentos.
Método toString Este es un método específico de Java que se usa para obtener una representación en forma de cadena del objeto. Es útil para imprimir el estado del objeto de manera legible. En este caso, toString recorre el arreglo bidimensional y construye una cadena con las ventas de cada departamento.

=== Java y Python Comparación/Diferencias ===
Trabajando en ambos lenguajes:
Java: Requiere una estructura más formal con declaraciones explícitas de clases y métodos. Usa llaves {} para definir bloques de código.
Python: Es más conciso y usa indentación para definir bloques de código.

Arreglos Bidimensionales:
Java: Usa arreglos bidimensionales (int[][]) y requiere inicialización explícita.
Python: Usa listas anidadas y es más flexible en la inicialización.

Método Principal:
Java: Usa el método main para ejecutar el programa.
Python: Ejecuta el código directamente bajo la condición if __name__ == "__main__":.

