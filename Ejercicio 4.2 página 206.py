#Ejercicio 4,2 - Página 206

from enum import Enum

class LocalType(Enum):
    INTERNO = 1
    CALLE = 2

class Property:
    def __init__(self, property_id, area, address):
        self.property_id = property_id
        self.area = area
        self.address = address
        self.sale_price = 0.0

    def calculate_sale_price(self, area_value):
        self.sale_price = self.area * area_value
        return self.sale_price

    def print_info(self):
        print(f"Identificador inmobiliario = {self.property_id}")
        print(f"Area = {self.area}")
        print(f"Dirección = {self.address}")
        print(f"Precio de venta = ${self.sale_price:.1E}")

class ResidentialProperty(Property):
    def __init__(self, property_id, area, address, bedrooms, bathrooms):
        super().__init__(property_id, area, address)
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms

    def print_info(self):
        super().print_info()
        print(f"Número de habitaciones = {self.bedrooms}")
        print(f"Número de baños = {self.bathrooms}")

class House(ResidentialProperty):
    def __init__(self, property_id, area, address, bedrooms, bathrooms, floors):
        super().__init__(property_id, area, address, bedrooms, bathrooms)
        self.floors = floors

    def print_info(self):
        super().print_info()
        print(f"Número de pisos = {self.floors}")

class Apartment(ResidentialProperty):
    def __init__(self, property_id, area, address, bedrooms, bathrooms):
        super().__init__(property_id, area, address, bedrooms, bathrooms)

class Local(Property):
    def __init__(self, property_id, area, address, local_type):
        super().__init__(property_id, area, address)
        self.local_type = local_type

    def print_info(self):
        super().print_info()
        print(f"Tipo de local = {self.local_type.name}")

# CLASES ESPECÍFICAS
class FamilyApartment(Apartment):
    area_value = 2000000
    
    def __init__(self, property_id, area, address, bedrooms, bathrooms, administration_fee):
        super().__init__(property_id, area, address, bedrooms, bathrooms)
        self.administration_fee = administration_fee

    def print_info(self):
        super().print_info()
        print(f"Valor de la administración = ${self.administration_fee}")

class StudioApartment(Apartment):
    area_value = 1500000
    
    def __init__(self, property_id, area, address):
        super().__init__(property_id, area, address, 1, 1)

    def print_info(self):
        super().print_info()
        print()

class RuralHouse(House):
    area_value = 1500000
    
    def __init__(self, property_id, area, address, bedrooms, bathrooms, floors, distance, altitude):
        super().__init__(property_id, area, address, bedrooms, bathrooms, floors)
        self.distance = distance
        self.altitude = altitude

    def print_info(self):
        super().print_info()
        print(f"Distancia la cabecera municipal = {self.distance}km")
        print(f"Altitud sobre el nivel del mar = {self.altitude}metros")
        print()

class UrbanHouse(House):
    def __init__(self, property_id, area, address, bedrooms, bathrooms, floors):
        super().__init__(property_id, area, address, bedrooms, bathrooms, floors)

class CommercialLocal(Local):
    area_value = 3000000
    
    def __init__(self, property_id, area, address, local_type, shopping_center):
        super().__init__(property_id, area, address, local_type)
        self.shopping_center = shopping_center

    def print_info(self):
        super().print_info()
        print(f"Centro Comercial = {self.shopping_center}")
        print()

class Office(Local):
    area_value = 3500000
    
    def __init__(self, property_id, area, address, local_type, is_government):
        super().__init__(property_id, area, address, local_type)
        self.is_government = is_government

    def print_info(self):
        super().print_info()
        print(f"Es oficina gubernamental = {self.is_government}")
        print()

class GatedCommunityHouse(UrbanHouse):
    area_value = 2500000
    
    def __init__(self, property_id, area, address, bedrooms, bathrooms, floors, administration_fee, has_pool, has_sports_fields):
        super().__init__(property_id, area, address, bedrooms, bathrooms, floors)
        self.administration_fee = administration_fee
        self.has_pool = has_pool
        self.has_sports_fields = has_sports_fields

    def print_info(self):
        super().print_info()
        print(f"Valor de la administración = ${self.administration_fee}")
        print(f"Tiene piscina? = {self.has_pool}")
        print(f"Tiene campos deportivos? = {self.has_sports_fields}")
        print()

class IndependentHouse(UrbanHouse):
    area_value = 3000000.0
    
    def __init__(self, property_id, area, address, bedrooms, bathrooms, floors):
        super().__init__(property_id, area, address, bedrooms, bathrooms, floors)

if __name__ == "__main__":
    print("Datos apartamento")
    apt1 = FamilyApartment(103067, 120, "Avenida Santander 45-45", 3, 2, 200000)
    apt1.calculate_sale_price(FamilyApartment.area_value)
    apt1.print_info()
    
    print("\nDatos apartamento")
    apt2 = StudioApartment(12354, 50, "Avenida Caracas 30-15")
    apt2.calculate_sale_price(StudioApartment.area_value)
    apt2.print_info()
