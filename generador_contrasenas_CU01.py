# ============================================================
# PROYECTO: GENERADOR SEGURO DE CONTRASEÑAS
# FUNCIONES 1 Y 2
# Autor: Alejandra Guachamin
#
# Función 1:
# Configurar la longitud de la contraseña.
#
# Función 2:
# Seleccionar los tipos de caracteres que tendrá
# la contraseña.
# ============================================================


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
            # Solicitar la longitud al usuario
            longitud = int(
                input(
                    "\nIngrese la longitud de la contraseña "
                    "(8-128): "
                )
            )

            # Verificar que la longitud esté dentro del rango
            if 8 <= longitud <= 128:

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

            print(
                "\nERROR: Debe ingresar un número entero."
            )


# ------------------------------------------------------------
# FUNCIÓN 2: SELECCIONAR TIPOS DE CARACTERES
# ------------------------------------------------------------

def seleccionar_caracteres():
    """
    Permite al usuario seleccionar los tipos de caracteres
    que desea utilizar para la contraseña.

    Opciones:
    1. Mayúsculas
    2. Minúsculas
    3. Números
    4. Símbolos
    """

    while True:

        print("\n==========================================")
        print("      TIPOS DE CARACTERES")
        print("==========================================")

        print("1. Letras mayúsculas")
        print("2. Letras minúsculas")
        print("3. Números")
        print("4. Símbolos")

        print(
            "\nPuede seleccionar varias opciones."
        )

        seleccion = input(
            "Ingrese las opciones separadas por coma "
            "(ejemplo: 1,2,3,4): "
        )

        # Convertir la entrada en una lista
        opciones = seleccion.split(",")

        # Eliminar espacios
        opciones = [
            opcion.strip()
            for opcion in opciones
        ]

        # Variable donde almacenaremos las opciones
        caracteres_seleccionados = []

        # -----------------------------------------------
        # VERIFICAR OPCIÓN 1
        # -----------------------------------------------

        if "1" in opciones:

            caracteres_seleccionados.append(
                "Letras mayúsculas"
            )

        # -----------------------------------------------
        # VERIFICAR OPCIÓN 2
        # -----------------------------------------------

        if "2" in opciones:

            caracteres_seleccionados.append(
                "Letras minúsculas"
            )

        # -----------------------------------------------
        # VERIFICAR OPCIÓN 3
        # -----------------------------------------------

        if "3" in opciones:

            caracteres_seleccionados.append(
                "Números"
            )

        # -----------------------------------------------
        # VERIFICAR OPCIÓN 4
        # -----------------------------------------------

        if "4" in opciones:

            caracteres_seleccionados.append(
                "Símbolos"
            )

        # -----------------------------------------------
        # VALIDAR SELECCIÓN
        # -----------------------------------------------

        if len(caracteres_seleccionados) > 0:

            print(
                "\nTipos de caracteres seleccionados:"
            )

            for caracter in caracteres_seleccionados:

                print(f"- {caracter}")

            return caracteres_seleccionados

        else:

            print(
                "\nERROR: Debe seleccionar al menos "
                "un tipo de carácter."
            )


# ------------------------------------------------------------
# FUNCIÓN PRINCIPAL
# ------------------------------------------------------------

def main():

    print("\n" + "=" * 60)
    print("       GENERADOR SEGURO DE CONTRASEÑAS")
    print("=" * 60)

    print("\nFUNCIONES IMPLEMENTADAS:")
    print("1. Configurar longitud")
    print("2. Seleccionar tipos de caracteres")

    # Ejecutar FUNCIÓN 1
    longitud = configurar_longitud()

    # Ejecutar FUNCIÓN 2
    caracteres = seleccionar_caracteres()

    # --------------------------------------------------------
    # MOSTRAR RESUMEN
    # --------------------------------------------------------

    print("\n" + "=" * 60)
    print("              CONFIGURACIÓN")
    print("=" * 60)

    print(
        f"Longitud seleccionada: {longitud} caracteres"
    )

    print("Tipos de caracteres:")

    for caracter in caracteres:

        print(f"- {caracter}")

    print("=" * 60)

    print(
        "\nLas funciones 1 y 2 se ejecutaron "
        "correctamente."
    )


# ------------------------------------------------------------
# INICIO DEL PROGRAMA
# ------------------------------------------------------------

if __name__ == "__main__":
    main()