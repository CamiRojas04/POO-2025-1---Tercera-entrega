#Ejercicio 4.4 página 231

class Teacher:
    def print_info(self):
        print("Es un profesor.")

class FullProfessor(Teacher):
    def print_info(self):
        print("Es un profesor titular.")

if __name__ == "__main__":
    professor1 = FullProfessor()
    professor1.print_info()
