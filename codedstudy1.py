estudiantes = []  

def mostrar_menu():
    print("\n===== MENÚ =====")
    print("1. Registrar un estudiante")
    print("2. Mostrar todos los estudiantes")
    print("3. Consultar promedio de un estudiante")
    print("4. Mostrar estadísticas generales")
    print("5. Salir")
    print("6. Eliminar un estudiante")

def calcular_promedio(calificaciones):
    suma = 0
    for calif in calificaciones:
        suma += calif
    return suma / 3

def pedir_calificacion(numero):
    while True:
        try:
            cal = float(input(f"Calificación {numero}: "))
            if 0 <= cal <= 100:
                return cal
            print("Debe estar entre 0 y 100.")
        except ValueError:
            print("Escribe un número válido.")

def buscar_estudiante(identificacion):
    for est in estudiantes:
        if est["id"] == identificacion:
            return est
    return None

def registrar_estudiante():
    identificacion = input("Identificación: ").strip()
    if identificacion == "":
        print("La identificación no puede estar vacía.")
        return
    if buscar_estudiante(identificacion) is not None:
        print("Ya existe un estudiante con esa identificación.")
        return

    nombre = input("Nombre: ").strip()
    if nombre == "":
        print("El nombre no puede estar vacío.")
        return

    califs = (pedir_calificacion(1), pedir_calificacion(2), pedir_calificacion(3))
    promedio = calcular_promedio(califs)
    aprobado = promedio >= 70

    if aprobado:
        situacion = "Aprobado"
    else:
        situacion = "Reprobado"

    estudiantes.append({
        "id": identificacion,
        "nombre": nombre,
        "calificaciones": califs,
        "promedio": promedio,
        "situacion": situacion,
    })
    print(f"Estudiante registrado: {nombre} | Promedio: {promedio:.2f} | {situacion}")

def mostrar_estudiantes():
    if len(estudiantes) == 0:
        print("Todavía no hay estudiantes registrados.")
        return
    for est in estudiantes:
        print(f"ID: {est['id']} | Nombre: {est['nombre']} | "
              f"Calificaciones: {est['calificaciones']} | "
              f"Promedio: {est['promedio']:.2f} | {est['situacion']}")

def consultar_estudiante():
    identificacion = input("Identificación a buscar: ").strip()
    est = buscar_estudiante(identificacion)
    if est is None:
        print("Estudiante no encontrado.")
    else:
        print(f"{est['nombre']} | Promedio: {est['promedio']:.2f} | {est['situacion']}")

def mostrar_estadisticas():
    if len(estudiantes) == 0:
        print("Todavía no hay estudiantes registrados.")
        return

    total = len(estudiantes)
    suma = 0
    aprobados = 0
    reprobados = 0
    mas_alto = estudiantes[0]["promedio"]

    for est in estudiantes:
        suma += est["promedio"]
        if est["situacion"] == "Aprobado":
            aprobados += 1
        else:
            reprobados += 1
        if est["promedio"] > mas_alto:
            mas_alto = est["promedio"]

    print(f"Estudiantes registrados: {total}")
    print(f"Promedio general: {suma / total:.2f}")
    print(f"Aprobados: {aprobados}")
    print(f"Reprobados: {reprobados}")
    print(f"Promedio más alto: {mas_alto:.2f}")

def eliminar_estudiante():
    identificacion = input("Identificación a eliminar: ").strip()
    est = buscar_estudiante(identificacion)
    if est is None:
        print("Estudiante no encontrado.")
    else:
        estudiantes.remove(est)
        print("Estudiante eliminado.")

continuar = True
while continuar:
    mostrar_menu()
    opcion = input("Elige una opción: ").strip()

    if opcion == "1":
        registrar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        consultar_estudiante()
    elif opcion == "4":
        mostrar_estadisticas()
    elif opcion == "5":
        print("Hasta luego")
        continuar = False
    elif opcion == "6":
        eliminar_estudiante()
    else:
        print("Opción inexistente, intenta de nuevo.")