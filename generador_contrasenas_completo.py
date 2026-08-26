# -*- coding: utf-8 -*-
"""
PROYECTO: GENERADOR SEGURO DE CONTRASEÑAS - NIVEL 2

Estructuras: variables, strings, condicionales, while, for, tuplas, listas,
diccionarios, funciones y excepciones.
Seguridad: se utiliza secrets en lugar de random.
"""

import secrets
import string
import tkinter as tk


# FUNCIÓN: mostrar_titulo
# Rol: presentación del sistema.
# Muestra el encabezado principal.
def mostrar_titulo():
    """Muestra el título del programa."""
    # Muestra en pantalla el encabezado principal del generador de contraseñas.
    print("\n" + "=" * 60)
    print("          GENERADOR SEGURO DE CONTRASEÑAS")
    print("              PROYECTO - COMPLETO")
    print("=" * 60)


# FUNCIÓN: leer_entero
# Rol: validación de datos.
# Solicita un entero y lo mantiene dentro del rango establecido.
def leer_entero(mensaje, minimo, maximo):
    """Lee y valida un número entero."""
    # Solicita un número entero y repite la petición hasta que esté dentro del rango permitido.
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"ERROR: ingrese un valor entre {minimo} y {maximo}.")
        except ValueError:
            print("ERROR: debe ingresar un número entero.")


# FUNCIÓN: crear_configuracion
# Rol: entrada y organización de datos.
# Retorna una tupla con longitud y categorías seleccionadas.
def crear_configuracion():
    """Crea la configuración de generación."""
    # Solicita y organiza la longitud y los tipos de caracteres que se utilizarán.
    print("\n" + "=" * 50)
    print("          CONFIGURACIÓN DE PARÁMETROS")
    print("=" * 50)

    longitud = leer_entero(
        "Longitud de la contraseña (8-32): ", 8, 32
    )

    mayusculas = input("¿Incluir MAYÚSCULAS? (s/n): ").strip().lower() == "s"
    minusculas = input("¿Incluir MINÚSCULAS? (s/n): ").strip().lower() == "s"
    numeros = input("¿Incluir NÚMEROS? (s/n): ").strip().lower() == "s"
    simbolos = input("¿Incluir SÍMBOLOS? (s/n): ").strip().lower() == "s"

    if not any((mayusculas, minusculas, numeros, simbolos)):
        print("Debe seleccionar al menos una categoría. Se activarán minúsculas.")
        minusculas = True

    return (longitud, mayusculas, minusculas, numeros, simbolos)


# FUNCIÓN: construir_grupos
# Rol: manejo de strings y estructuras de datos.
# Construye los grupos disponibles y devuelve un string y una tupla.
def construir_grupos(configuracion):
    """Construye los grupos de caracteres según la configuración."""
    # Construye los grupos de caracteres disponibles según la configuración seleccionada.
    _, mayusculas, minusculas, numeros, simbolos = configuracion
    grupos = []

    if mayusculas:
        grupos.append(string.ascii_uppercase)
    if minusculas:
        grupos.append(string.ascii_lowercase)
    if numeros:
        grupos.append(string.digits)
    if simbolos:
        grupos.append("!@#$%^&*()-_=+[]{};:,.?/")

    return "".join(grupos), tuple(grupos)


# FUNCIÓN: generar_contrasena
# Rol: lógica principal de generación.
# Usa secrets y garantiza al menos un carácter por categoría.
def generar_contrasena(configuracion):
    """Genera una contraseña criptográficamente segura."""
    # Genera una contraseña segura, garantizando un carácter de cada categoría elegida y mezclando el resultado.
    longitud, _, _, _, _ = configuracion
    todos, grupos = construir_grupos(configuracion)

    obligatorios = []
    for grupo in grupos:
        obligatorios.append(secrets.choice(grupo))

    restantes = longitud - len(obligatorios)
    caracteres = obligatorios + [
        secrets.choice(todos) for _ in range(restantes)
    ]

    secrets.SystemRandom().shuffle(caracteres)
    return "".join(caracteres)


# FUNCIÓN: evaluar_fortaleza
# Rol: análisis y toma de decisiones.
# Retorna una tupla: nivel, puntuación y recomendaciones.
def evaluar_fortaleza(contrasena):
    """Evalúa la fortaleza de una contraseña."""
    # Analiza la longitud y los tipos de caracteres para calcular la fortaleza y generar recomendaciones.
    puntuacion = 0
    recomendaciones = []

    if len(contrasena) >= 16:
        puntuacion += 2
    elif len(contrasena) >= 12:
        puntuacion += 1
    else:
        recomendaciones.append("Se recomiendan al menos 12 caracteres.")

    if any(c.isupper() for c in contrasena):
        puntuacion += 1
    else:
        recomendaciones.append("Incluya letras mayúsculas.")

    if any(c.islower() for c in contrasena):
        puntuacion += 1
    else:
        recomendaciones.append("Incluya letras minúsculas.")

    if any(c.isdigit() for c in contrasena):
        puntuacion += 1
    else:
        recomendaciones.append("Incluya números.")

    if any(c in string.punctuation for c in contrasena):
        puntuacion += 1
    else:
        recomendaciones.append("Incluya símbolos.")

    if puntuacion >= 6:
        nivel = "MUY FUERTE"
    elif puntuacion >= 5:
        nivel = "FUERTE"
    elif puntuacion >= 3:
        nivel = "MEDIA"
    else:
        nivel = "DÉBIL"

    return nivel, puntuacion, tuple(recomendaciones)


# FUNCIÓN: registrar_historial
# Rol: manejo de listas y tuplas.
# Guarda únicamente metadatos; nunca almacena la contraseña.
def registrar_historial(historial, numero, contrasena, nivel):
    """Registra número, longitud y fortaleza."""
    # Guarda en el historial únicamente el número, la longitud y el nivel de fortaleza.
    historial.append((numero, len(contrasena), contrasena, nivel))


# FUNCIÓN: mostrar_historial
# Rol: presentación de información.
# Muestra generaciones sin revelar contraseñas.
def mostrar_historial(historial):
    """Muestra el historial de generaciones."""
    # Muestra las generaciones anteriores sin revelar las contraseñas almacenadas.
    print("\n--- HISTORIAL ---")
    if not historial:
        print("Todavía no existen generaciones.")
        return

    for numero, longitud, nivel in historial:
        print(f"#{numero:02d} | Longitud: {longitud:02d} | contrasena | Fortaleza: {nivel}")


# FUNCIÓN: mostrar_estadisticas
# Rol: análisis de datos.
# Usa un diccionario para contar niveles de fortaleza.
def mostrar_estadisticas(historial):
    """Muestra estadísticas de las generaciones."""
    # Cuenta y muestra cuántas contraseñas corresponden a cada nivel de fortaleza.
    conteo = {
        "MUY FUERTE": 0,
        "FUERTE": 0,
        "MEDIA": 0,
        "DÉBIL": 0
    }

    for _, _, nivel in historial:
        conteo[nivel] += 1

    print("\n--- ESTADÍSTICAS ---")
    print(f"Total generadas: {len(historial)}")
    for nivel, cantidad in conteo.items():
        print(f"{nivel}: {cantidad}")


# FUNCIÓN: mostrar_contrasena
# Rol: interfaz y protección visual.
# Permite mostrar u ocultar la última contraseña.
def mostrar_contrasena(contrasena):
    """Muestra u oculta visualmente la contraseña."""
    # Muestra la última contraseña y permite ocultarla o volver a mostrarla.
    if not contrasena:
        print("Todavía no se ha generado una contraseña.")
        return

    print(f"\nContraseña: {contrasena}")
    if input("¿Desea ocultarla? (s/n): ").strip().lower() == "s":
        print("*" * len(contrasena))
        if input("¿Desea volver a mostrarla? (s/n): ").strip().lower() == "s":
            print(f"Contraseña: {contrasena}")


# FUNCIÓN: copiar_contrasena
# Rol: integración con el sistema operativo.
# Copia la contraseña al portapapeles mediante Tkinter.
def copiar_contrasena(contrasena):
    """Copia la contraseña al portapapeles."""
    # Copia la última contraseña al portapapeles utilizando Tkinter.
    if not contrasena:
        print("No existe una contraseña para copiar.")
        return

    try:
        ventana = tk.Tk()
        ventana.withdraw()
        ventana.clipboard_clear()
        ventana.clipboard_append(contrasena)
        ventana.update()
        print("Contraseña copiada al portapapeles.")
        ventana.destroy()
    except Exception as error:
        print(f"No fue posible copiar la contraseña: {error}")


# FUNCIÓN: generar_nueva_contrasena
# Rol: reutilización y control del flujo.
# Permite conservar o cambiar la configuración.
def generar_nueva_contrasena(configuracion):
    """Genera una nueva contraseña con la configuración elegida."""
    # Genera otra contraseña conservando la configuración actual o solicitando una nueva.
    respuesta = input(
        "\n¿Desea utilizar los mismos parámetros? (s/n): "
    ).strip().lower()

    if respuesta == "s":
        nueva_configuracion = configuracion
    else:
        nueva_configuracion = crear_configuracion()

    return generar_contrasena(nueva_configuracion), nueva_configuracion


# FUNCIÓN: mostrar_resultado_generacion
# Rol: presentación y reutilización.
# Centraliza la salida para no repetir código en el menú.
def mostrar_resultado_generacion(contrasena, historial, numero):
    """Muestra y registra el resultado de una generación."""
    # Evalúa, registra y presenta todos los datos de la contraseña recién generada.
    nivel, puntuacion, recomendaciones = evaluar_fortaleza(contrasena)
    registrar_historial(historial, numero, contrasena, nivel)

    print("\n--- CONTRASEÑA GENERADA ---")
    print(f"Contraseña: {contrasena}")
    print(f"Longitud: {len(contrasena)}")
    print(f"Fortaleza: {nivel} ({puntuacion}/6)")

    if recomendaciones:
        print("Recomendaciones:")
        for recomendacion in recomendaciones:
            print(f"- {recomendacion}")


# FUNCIÓN: mostrar_menu
# Rol: interfaz del sistema.
# Presenta todas las opciones disponibles.
def mostrar_menu():
    """Muestra el menú principal."""
    # Presenta las opciones principales que el usuario puede seleccionar.
    print("\n" + "=" * 50)
    print("1. Configurar parámetros")
    print("2. Generar contraseña")
    print("3. Evaluar última contraseña")
    print("4. Mostrar / ocultar última contraseña")
    print("5. Copiar última contraseña")
    print("6. Generar nueva contraseña")
    print("7. Ver historial")
    print("8. Ver estadísticas")
    print("9. Salir")
    print("=" * 50)


# FUNCIÓN: main
# Rol: integración del proyecto.
# Coordina todas las funciones mediante while e if/elif/else.
def main():
    """Controla el flujo completo de la aplicación."""
    # Coordina el funcionamiento completo del programa y controla el menú principal.
    configuracion = (16, True, True, True, True)
    ultima_contrasena = ""
    historial = []
    numero_generacion = 0

    mostrar_titulo()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            configuracion = crear_configuracion()
            print("Configuración guardada.")

        elif opcion == "2":
            ultima_contrasena = generar_contrasena(configuracion)
            numero_generacion += 1
            mostrar_resultado_generacion(
                ultima_contrasena, historial, numero_generacion
            )

        elif opcion == "3":
            if not ultima_contrasena:
                print("Primero debe generar una contraseña.")
            else:
                nivel, puntuacion, recomendaciones = evaluar_fortaleza(
                    ultima_contrasena
                )
                print(f"\nNivel: {nivel}")
                print(f"Puntuación: {puntuacion}/6")
                for recomendacion in recomendaciones:
                    print(f"- {recomendacion}")

        elif opcion == "4":
            mostrar_contrasena(ultima_contrasena)

        elif opcion == "5":
            copiar_contrasena(ultima_contrasena)

        elif opcion == "6":
            ultima_contrasena, configuracion = generar_nueva_contrasena(
                configuracion
            )
            numero_generacion += 1
            mostrar_resultado_generacion(
                ultima_contrasena, historial, numero_generacion
            )

        elif opcion == "7":
            mostrar_historial(historial)

        elif opcion == "8":
            mostrar_estadisticas(historial)

        elif opcion == "9":
            print("\nPrograma finalizado correctamente.")
            break

        else:
            print("Opción inválida. Seleccione del 1 al 9.")


# PUNTO DE ENTRADA
# Rol: ejecución del programa.
if __name__ == "__main__":
    main()
