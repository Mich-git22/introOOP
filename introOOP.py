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
        print(f"Hola {otra_persona}, soy {self.nombre}. ¡Mucho gusto!")


# Crear una instancia de la clase Persona
persona1 = Persona("Juan", 19, "Estudiante")
persona2 = Persona("Victor", 10, "Ingeniero")
# Llamada a los métodos de la instancia
persona1.presentarse()  # Hola, me llamo Ana y tengo 30 años.
persona1.describir_ocupacion()  # Ana es Ingeniera.
persona1.cambiar_ocupacion("Doctora")  # Ana ahora trabaja como Doctora.
persona1.cumplir_anios()  # Ana ha cumplido 31 años.
persona1.saludar("Carlos")  # Hola Carlos, soy Ana. ¡Mucho gusto!
def saludarA(self,nombreOtraPersona):
    return f"hola,{self.nombre},te manda a saludar {nombreOtraPersona}"
print(persona1.saludarA (persona2.nombre))