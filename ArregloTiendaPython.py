class Tienda:
    def __init__(self):
        self.ventas_mensuales = {
            "Ropa": [520, 630, 740, 850, 960, 1070, 1180, 1290, 1400, 1510, 1620, 1730],
            "Deportes": [460, 570, 680, 790, 900, 1010, 1120, 1230, 1340, 1450, 1560, 1670],
            "Jugueteria": [410, 520, 630, 740, 850, 960, 1070, 1180, 1290, 1400, 1510, 1620]
        }

    def agregar_venta(self, depto, mes, venta):
        if depto in self.ventas_mensuales and 1 <= mes <= 12:
            self.ventas_mensuales[depto][mes - 1] = venta
        else:
            print("Departamento o mes inválido")

    def obtener_venta(self, depto, mes):
        if depto in self.ventas_mensuales and 1 <= mes <= 12:
            return self.ventas_mensuales[depto][mes - 1]
        else:
            print("Departamento o mes inválido")
            return None

    def borrar_venta(self, depto, mes):
        if depto in self.ventas_mensuales and 1 <= mes <= 12:
            self.ventas_mensuales[depto][mes - 1] = 0
        else:
            print("Departamento o mes inválido")

    def mostrar_ventas(self):
        for depto, ventas in self.ventas_mensuales.items():
            print(f"Ventas de {depto}: {ventas}")

tienda = Tienda()

print("Ventas iniciales:")
tienda.mostrar_ventas()

print("\nAgregar venta de 1550 en Ropa en enero:")
tienda.agregar_venta("Ropa", 1, 1550)
tienda.mostrar_ventas()

print("\nObtener venta de Deportes en febrero:")
print(tienda.obtener_venta("Deportes", 2))

print("\nBorrar venta de Jugueteria en marzo:")
tienda.borrar_venta("Jugueteria", 3)
tienda.mostrar_ventas()

