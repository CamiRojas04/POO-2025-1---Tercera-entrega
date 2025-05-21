#Ejercicio propuesto - Página 227
class ComputerDevice:
    def __init__(self):
        self.brand = "Acer"
        print(f"Marca = {self.brand}")

class Tablet(ComputerDevice):
    def __init__(self, brand):
        super().__init__()  # Invoca al constructor de la clase padre
        print(f"Marca = {brand}")

if __name__ == "__main__":
    my_tablet = Tablet("Dell")
