import re

class Contacto:
    def __init__(self, nombre, apellido, telefono, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.correo = correo

    def __str__(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Teléfono: {self.telefono}, Email: {self.correo}"

class Agenda:
    def __init__(self, limite_contactos=10):
        self.contactos = []
        self.limite_contactos = limite_contactos

    def agregar_contacto(self, contacto):
        if len(self.contactos) >= self.limite_contactos:
            raise Exception("La agenda está llena. No se pueden agregar más contactos, ya que es una version de prueba.")
        self.contactos.append(contacto)

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                return True
        return False

    def buscar_contacto(self, nombre):
        resultados = [contacto for contacto in self.contactos if contacto.nombre == nombre]
        return resultados

    def editar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print(f"Editando contacto: {contacto}")
                contacto.nombre = input("Nuevo nombre (dejar vacío para no cambiar): ") or contacto.nombre
                contacto.apellido = input("Nuevo apellido (dejar vacío para no cambiar): ") or contacto.apellido
                contacto.telefono = obtener_telefono("Nuevo teléfono (dejar vacío para no cambiar): ") or contacto.telefono
                contacto.correo = obtener_correo("Nuevo email (dejar vacío para no cambiar): ") or contacto.correo
                return True
        return False

    def listar_contactos(self):
        for contacto in self.contactos:
            print(contacto)

def validar_correo(correo):
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, correo)

def obtener_dato(mensaje, es_obligatorio=False, max_caracteres=20):
    while True:
        dato = input(mensaje)
        if es_obligatorio and not dato:
            print("Este campo es obligatorio.")
        elif max_caracteres and len(dato) > max_caracteres:
            print(f"El campo no puede tener más de {max_caracteres} caracteres.")
        else:
            return dato

def obtener_telefono(mensaje):
    while True:
        telefono = input(mensaje)
        if not telefono:
            return telefono
        if telefono.isdigit() and len(telefono) <= 15:
            return telefono
        print("El teléfono debe ser un número válido (máximo 15 dígitos).")

def obtener_correo(mensaje):
    while True:
        correo = input(mensaje)
        if not correo:
            return correo
        if validar_correo(correo):
            return correo
        print("Email no válido. Intente de nuevo.")

def main():
    agenda = Agenda()

    while True:
        print("\n--- Agenda de Contactos ---")
        print("1. Agregar contacto")
        print("2. Eliminar contacto")
        print("3. Buscar contacto")
        print("4. Editar contacto")
        print("5. Listar contactos")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = obtener_dato("Nombre: ", es_obligatorio=True)
                apellido = obtener_dato("Apellido: ")
                telefono = obtener_telefono("Teléfono: ")
                correo = obtener_correo("Correo: ")

                if not telefono and not correo:
                    print("Debe ingresar al menos un teléfono o un email.")
                    continue

                if any(contacto.nombre == nombre for contacto in agenda.contactos):
                    print("Ya existe un contacto con ese nombre.")
                    continue
                if telefono and any(contacto.telefono == telefono for contacto in agenda.contactos):
                    print("Ya existe un contacto con ese número de teléfono.")
                    continue

                nuevo_contacto = Contacto(nombre, apellido, telefono, correo)
                agenda.agregar_contacto(nuevo_contacto)
                print("Contacto regisrtrado")
            except Exception as e:
                print(e)

        elif opcion == "2":
            nombre = obtener_dato("Nombre del contacto que quieres borrar: ", es_obligatorio=True)
            if agenda.eliminar_contacto(nombre):
                print("Contacto borrado")
            else:
                print("Contacto no encontrado.")

        elif opcion == "3":
            nombre = obtener_dato("Nombre del contacto a buscar: ", es_obligatorio=True)
            busqueda = agenda.buscar_contacto(nombre)
            if busqueda:
                for contacto in busqueda:
                    print(contacto)
                editar = input("¿Desea editar alguno de estos contactos? (s/n): ").lower()
                if editar == 's':
                    nombre_editar = obtener_dato("Nombre del contacto a editar: ", es_obligatorio=True)
                    if agenda.editar_contacto(nombre_editar):
                        print("Contacto editado con éxito.")
                    else:
                        print("Contacto no encontrado.")
            else:
                print("No se encontraron contactos.")

        elif opcion == "4":
            nombre = obtener_dato("Nombre del contacto a editar: ", es_obligatorio=True)
            if agenda.editar_contacto(nombre):
                print("Contacto editado con éxito.")
            else:
                print("Contacto no encontrado.")

        elif opcion == "5":
            agenda.listar_contactos()

        elif opcion == "6":
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()