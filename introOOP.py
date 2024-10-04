# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        # Atributos de la clase
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    # Método 1: Presentarse
    def presentarse(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")

    # Método 2: Cambiar la ocupación
    def cambiar_ocupacion(self, nueva_ocupacion):
        self.ocupacion = nueva_ocupacion
        print(f"{self.nombre} ahora trabaja como {self.ocupacion}.")

    # Método 3: Cumplir años
    def cumplir_anios(self):
        self.edad += 1
        print(f"{self.nombre} ha cumplido {self.edad} años.")

    # Método 4: Describir ocupación
    def describir_ocupacion(self):
        print(f"{self.nombre} es {self.ocupacion}.")

    # Método 5: Saludar
    def saludar(self, otra_persona):
        print(f"Hola {otra_persona.nombre}, soy {self.nombre}. ¡Mucho gusto!")

    # Método adicional: Saludar a otra persona
    def saludar_a(self, nombre_otra_persona):
        return f"Hola, {self.nombre}, te manda a saludar {nombre_otra_persona}."


# Crear instancias de la clase Persona
persona1 = Persona("Juan", 19, "Estudiante")
persona2 = Persona("Victor", 10, "Ingeniero")

# Llamada a los métodos de la instancia
persona1.presentarse()  # "Hola, me llamo Juan y tengo 19 años."
persona1.describir_ocupacion()  # "Juan es Estudiante."
persona1.cambiar_ocupacion("Doctor")  # "Juan ahora trabaja como Doctor."
persona1.cumplir_anios()  # "Juan ha cumplido 20 años."
persona1.saludar(persona2)  # "Hola Victor, soy Juan. ¡Mucho gusto!"
print(persona1.saludar_a(persona2.nombre))  # "Hola, Juan, te manda a saludar Victor."
