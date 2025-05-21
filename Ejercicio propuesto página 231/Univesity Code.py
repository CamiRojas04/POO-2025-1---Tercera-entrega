#Ejercicio propuesto - Página 31

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def get_name(self):
        return self.name
    
    def get_address(self):
        return self.address
    
    def set_name(self, name):
        self.name = name
    
    def set_address(self, address):
        self.address = address
    
    def show_info(self):
        print(f"Nombre: {self.name}")
        print(f"Dirección: {self.address}")

class Student(Person):
    def __init__(self, name, address, career, semester):
        super().__init__(name, address)
        self.career = career
        self.semester = semester
    
    def get_career(self):
        return self.career
    
    def get_semester(self):
        return self.semester
    
    def set_career(self, career):
        self.career = career
    
    def set_semester(self, semester):
        self.semester = semester
    
    def show_info(self):
        super().show_info()
        print(f"Carrera: {self.career}")
        print(f"Semestre: {self.semester}")

class Professor(Person):
    def __init__(self, name, address, department, category):
        super().__init__(name, address)
        self.department = department
        self.category = category
    
    def get_department(self):
        return self.department
    
    def get_category(self):
        return self.category
    
    def set_department(self, department):
        self.department = department
    
    def set_category(self, category):
        self.category = category
    
    def show_info(self):
        super().show_info()
        print(f"Departamento: {self.department}")
        print(f"Categoría: {self.category}")

if __name__ == "__main__":
    
    # Crear un estudiante
    print("\n Datos del Estudiante\n")
    student = Student("María González", "Calle 123 #45-67", "Ingeniería de Sistemas", 5)
    student.show_info()
    
    # Modificar datos del estudiante
    student.set_semester(6)
    print("\nEl estudiante ha avanzado de semestre:\n")
    print(f"Nuevo semestre: {student.get_semester()}")
    
    # Crear un profesor
    print("\n Datos del Profesor \n")
    professor = Professor("Carlos Mendoza", "Avenida Principal 22-33", "Ciencias Básicas", "Asociado")
    professor.show_info()
    
    # Modificar datos del profesor
    professor.set_category("Titular")
    print("\nEl profesor ha sido promovido:\n")
    print(f"Nueva categoría: {professor.get_category()}")
    
