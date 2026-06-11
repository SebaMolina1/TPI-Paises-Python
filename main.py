from funciones import *

ARCHIVO = "paises.csv"

def mostrar_menu(total_paises):
    """Muestra el menú principal con la cantidad de países cargados."""
    print("\n" + "="*50)
    print("   SISTEMA DE GESTIÓN DE PAÍSES")
    print("="*50)
    print(f"   Países en memoria: {total_paises}")
    print("-"*50)
    print("  1. Ver todos los países")
    print("  2. Agregar nuevo país")
    print("  3. Actualizar población y superficie")
    print("  4. Buscar país por nombre")
    print("  5. Filtrar países")
    print("  6. Ordenar países")
    print("  7. Mostrar estadísticas")
    print("  8. Guardar datos a CSV")
    print("  9. Salir")
    print("="*50)

def menu_filtros(paises):
    """Submenú para elegir el tipo de filtro a aplicar."""
    print("\n  --- Filtrar países ---")
    print("  a. Por continente")
    print("  b. Por rango de población")
    print("  c. Por rango de superficie")
    opcion = input("\n  Seleccione filtro (a/b/c): ").strip().lower()
    if opcion == 'a':
        filtrar_por_continente(paises)
    elif opcion == 'b':
        filtrar_por_poblacion(paises)
    elif opcion == 'c':
        filtrar_por_superficie(paises)
    else:
        print("  Opción inválida")

def main():
    # Carga automática al iniciar el programa
    print("\n" + "="*50)
    print("   SISTEMA DE GESTIÓN DE PAÍSES")
    print("   Programación 1 - UTN TUP")
    print("="*50)
    print("\n  Cargando datos...")
    paises = cargar_datos(ARCHIVO)

    # Bucle principal del menú
    while True:
        mostrar_menu(len(paises))
        opcion = input("\n  Seleccione una opción (1-9): ").strip()

        if opcion == '1':
            listar_paises(paises)

        elif opcion == '2':
            paises = agregar_pais(paises)

        elif opcion == '3':
            if len(paises) > 0:
                actualizar_pais(paises)
            else:
                print("  No hay países cargados. Verifique el archivo CSV.")

        elif opcion == '4':
            if len(paises) > 0:
                buscar_por_nombre(paises)
            else:
                print("  No hay países cargados.")

        elif opcion == '5':
            if len(paises) > 0:
                menu_filtros(paises)
            else:
                print("  No hay países cargados.")

        elif opcion == '6':
            if len(paises) > 0:
                ordenar_paises(paises)
            else:
                print("  No hay países cargados.")

        elif opcion == '7':
            if len(paises) > 0:
                estadisticas(paises)
            else:
                print("  No hay países cargados.")

        elif opcion == '8':
            if len(paises) > 0:
                guardar_datos(ARCHIVO, paises)
            else:
                print("  No hay datos para guardar.")

        elif opcion == '9':
            if len(paises) > 0:
                resp = input("\n  ¿Guardar cambios antes de salir? (s/n): ").strip().lower()
                if resp == 's':
                    guardar_datos(ARCHIVO, paises)
            print("\n  Programa finalizado. ¡Hasta luego!")
            break

        else:
            print("  Opción inválida, intente de nuevo (1-9)")

if __name__ == "__main__":
    main()
