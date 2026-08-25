# -*- coding: utf-8 -*-
"""
@author: 
"""

# ============================================================
# PROYECTO: GENERADOR SEGURO DE CONTRASEÑAS
# Autor: Alejandra Guachamin
#
# Funciones:
# 1. Configurar longitud.
# 2. Seleccionar tipos de caracteres.
# 3. Generar la contraseña (usando el módulo 'secrets').
# 4. Evaluar la fortaleza de la contraseña.
# ============================================================

import secrets
import string


# ------------------------------------------------------------
# FUNCIÓN 1: CONFIGURAR LONGITUD
# ------------------------------------------------------------

def configurar_longitud():
    """
    Solicita al usuario la longitud de la contraseña.
    La longitud permitida es de 8 a 128 caracteres.
    """
    while True:
        try:
            longitud = int(
                input(
                    "\nIngrese la longitud de la contraseña "
                    "(8-16): "
                )
            )

            if 8 <= longitud <= 16:
                print(
                    f"\nLongitud configurada correctamente: "
                    f"{longitud} caracteres."
                )
                return longitud
            else:
                print(
                    "\nERROR: La longitud debe estar entre "
                    "8 y 128 caracteres."
                )

        except ValueError:
            print("\nERROR: Debe ingresar un número entero.")


# ------------------------------------------------------------
# FUNCIÓN 2: SELECCIONAR TIPOS DE CARACTERES
# ------------------------------------------------------------

def seleccionar_caracteres():
    """
    Permite al usuario seleccionar los tipos de caracteres.
    Retorna una lista con las cadenas de caracteres seleccionadas.
    """
    MAPA_CARACTERES = {
        "1": (string.ascii_uppercase, "Letras mayúsculas"),
        "2": (string.ascii_lowercase, "Letras minúsculas"),
        "3": (string.digits, "Números"),
        "4": (string.punctuation, "Símbolos")
    }

    while True:
        print("\n==========================================")
        print("      TIPOS DE CARACTERES")
        print("==========================================")
        print("1. Letras mayúsculas (A-Z)")
        print("2. Letras minúsculas (a-z)")
        print("3. Números (0-9)")
        print("4. Símbolos (!@#$%^&*...)")

        print("\nPuede seleccionar varias opciones.")
        seleccion = input(
            "Ingrese las opciones separadas por coma "
            "(ejemplo: 1,2,3,4): "
        )

        opciones = [opcion.strip() for opcion in seleccion.split(",")]

        conjuntos_seleccionados = []
        nombres_seleccionados = []

        for opcion in opciones:
            if opcion in MAPA_CARACTERES:
                chars, nombre = MAPA_CARACTERES[opcion]
                if chars not in conjuntos_seleccionados:
                    conjuntos_seleccionados.append(chars)
                    nombres_seleccionados.append(nombre)

        if len(conjuntos_seleccionados) > 0:
            print("\nTipos de caracteres seleccionados:")
            for nombre in nombres_seleccionados:
                print(f"- {nombre}")

            return conjuntos_seleccionados
        else:
            print(
                "\nERROR: Debe seleccionar al menos "
                "una opción válida (1, 2, 3 o 4)."
            )


# ------------------------------------------------------------
# FUNCIÓN 3: GENERAR CONTRASEÑA
# ------------------------------------------------------------

def generar_contrasena(longitud, conjuntos_caracteres):
    """
    Genera una contraseña segura garantizando al menos
    un carácter de cada tipo seleccionado.
    """
    contrasena = []

    # 1. Asegurar al menos un carácter de cada conjunto seleccionado
    for conjunto in conjuntos_caracteres:
        contrasena.append(secrets.choice(conjunto))

    # 2. Rellenar el resto de la longitud con una mezcla de todos los tipos
    todos_los_caracteres = "".join(conjuntos_caracteres)
    caracteres_restantes = longitud - len(contrasena)

    for _ in range(caracteres_restantes):
        contrasena.append(secrets.choice(todos_los_caracteres))

    # 3. Mezclar aleatoriamente para evitar patrones predecibles al inicio
    secrets.SystemRandom().shuffle(contrasena)

    return "".join(contrasena)


# ------------------------------------------------------------
# FUNCIÓN 4: EVALUAR FORTALEZA DE LA CONTRASEÑA
# ------------------------------------------------------------

def evaluar_fortaleza(longitud, num_tipos):
    """
    Calcula el nivel de seguridad de la contraseña
    según la longitud y la cantidad de tipos de caracteres.
    """
    if longitud >= 16 and num_tipos >= 3:
        return "MUY ALTA (Excelente seguridad) 🟢"
    elif longitud >= 12 and num_tipos >= 2:
        return "ALTA (Buena seguridad) 🟢"
    elif longitud >= 8 and num_tipos >= 2:
        return "MEDIA (Aceptable) 🟡"
    else:
        return "BAJA (Se recomienda aumentar longitud o variedad) 🔴"


# ------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------------

def main():
    while True:
        print("\n" + "=" * 60)
        print("       GENERADOR SEGURO DE CONTRASEÑAS")
        print("=" * 60)

        # 1. Configurar longitud
        longitud = configurar_longitud()

        # 2. Seleccionar tipos de caracteres
        conjuntos_caracteres = seleccionar_caracteres()

        # 3. Generar la contraseña
        contrasena_generada = generar_contrasena(
            longitud, conjuntos_caracteres
        )

        # 4. Evaluar la fortaleza
        fortaleza = evaluar_fortaleza(
            longitud, len(conjuntos_caracteres)
        )

        # --------------------------------------------------------
        # MOSTRAR RESULTADOS
        # --------------------------------------------------------
        print("\n" + "=" * 60)
        print("              RESULTADO Y DETALLES")
        print("=" * 60)
        print(f"Contraseña generada:  {contrasena_generada}")
        print(f"Longitud:             {longitud} caracteres")
        print(f"Tipos de caracteres:  {len(conjuntos_caracteres)}/4")
        print(f"Nivel de fortaleza:   {fortaleza}")
        print("=" * 60)

        # Preguntar al usuario si desea generar otra contraseña
        repetir = input(
            "\n¿Desea generar otra contraseña? (s/n): "
        ).strip().lower()

        if repetir != 's':
            print("\n¡Gracias por utilizar el Generador Seguro de Contraseñas!")
            break


# ------------------------------------------------------------
# INICIO DEL PROGRAMA
# ------------------------------------------------------------

if __name__ == "__main__":
    main()