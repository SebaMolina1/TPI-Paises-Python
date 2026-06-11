import csv

# Continentes válidos para validación
CONTINENTES_VALIDOS = ["América", "Europa", "Asia", "África", "Oceanía", "Antártida"]

def cargar_datos(nombre_archivo):
    """Carga los países desde un archivo CSV y los devuelve como lista de diccionarios."""
    paises = []
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
            # Detectar si el separador es coma o punto y coma
            primera_linea = archivo.readline()
            separador = ';' if ';' in primera_linea else ','
            archivo.seek(0)
            lector = csv.DictReader(archivo, delimiter=separador)
            for fila in lector:
                pais = {
                    'nombre': fila['nombre'].strip(),
                    'poblacion': int(fila['poblacion']),
                    'superficie': int(fila['superficie']),
                    'continente': fila['continente'].strip()
                }
                paises.append(pais)
        print(f"  {len(paises)} países cargados desde '{nombre_archivo}'")
    except FileNotFoundError:
        print(f"  Error: No se encontró el archivo '{nombre_archivo}'")
    except ValueError:
        print("  Error: Algunos datos numéricos son inválidos en el CSV")
    except KeyError as e:
        print(f"  Error: Falta la columna {e} en el CSV")
    return paises

def guardar_datos(nombre_archivo, paises):
    """Guarda la lista de países en el archivo CSV."""
    try:
        with open(nombre_archivo, 'w', encoding='utf-8', newline='') as archivo:
            campos = ['nombre', 'poblacion', 'superficie', 'continente']
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for p in paises:
                escritor.writerow(p)
        print("  Datos guardados correctamente.")
        return True
    except IOError as e:
        print(f"  Error al guardar los datos: {e}")
        return False

def validar_datos(nombre, poblacion, superficie, continente):
    """Valida que los datos de un país sean correctos. Devuelve (bool, mensaje)."""
    if nombre == "" or continente == "":
        return False, "Nombre y continente no pueden estar vacíos"
    try:
        pob = int(poblacion)
        if pob <= 0:
            return False, "La población debe ser mayor a cero"
    except ValueError:
        return False, "Población debe ser un número entero"
    try:
        sup = int(superficie)
        if sup <= 0:
            return False, "La superficie debe ser mayor a cero"
    except ValueError:
        return False, "Superficie debe ser un número entero"
    return True, "Datos válidos"

def mostrar_pais(p):
    """Muestra los datos de un país en formato prolijo."""
    print(f"  {p['nombre']:<25} Pob: {p['poblacion']:>12,}  Sup: {p['superficie']:>10,} km²  [{p['continente']}]")

def listar_paises(paises):
    """Muestra todos los países cargados en pantalla."""
    if len(paises) == 0:
        print("  No hay países cargados.")
        return
    print(f"\n  {'NOMBRE':<25} {'POBLACIÓN':>14}  {'SUPERFICIE':>13}  CONTINENTE")
    print("  " + "-"*70)
    for p in paises:
        mostrar_pais(p)
    print(f"\n  Total: {len(paises)} países")

def pedir_nombre(paises):
    """Pide el nombre del país en bucle hasta que sea válido (solo letras, no duplicado)."""
    while True:
        nombre = input("  Nombre: ").strip()
        if nombre == "":
            print("  Error: El nombre no puede estar vacío. Intente de nuevo.")
            continue
        if any(c.isdigit() for c in nombre):
            print("  Error: El nombre no puede contener números. Intente de nuevo.")
            continue
        duplicado = False
        for p in paises:
            if p['nombre'].lower() == nombre.lower():
                duplicado = True
                break
        if duplicado:
            print("  Error: Ese país ya existe. Intente de nuevo.")
            continue
        return nombre.title()  # Capitaliza la primera letra de cada palabra

def normalizar_texto(texto):
    """Quita tildes y pasa a minúsculas para comparar sin importar acentos."""
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u',
        'à': 'a', 'è': 'e', 'ì': 'i', 'ò': 'o', 'ù': 'u',
    }
    resultado = texto.lower()
    for con_tilde, sin_tilde in reemplazos.items():
        resultado = resultado.replace(con_tilde, sin_tilde)
    return resultado

def pedir_entero_positivo(campo):
    """Pide un número entero positivo en bucle. Acepta números con comas (45,000,000)."""
    while True:
        valor = input(f"  {campo} (solo números): ").strip()
        if valor == "":
            print("  Error: El campo no puede estar vacío. Intente de nuevo.")
            continue
        valor_limpio = valor.replace(',', '').replace('.', '')
        try:
            numero = int(valor_limpio)
            if numero <= 0:
                print("  Error: El valor debe ser mayor a cero. Intente de nuevo.")
                continue
            return numero
        except ValueError:
            print("  Error: Solo se permiten números (ej: 45000000 o 45,000,000). Intente de nuevo.")

def pedir_continente():
    """Pide el continente en bucle. Acepta con o sin tildes."""
    while True:
        print(f"  Continentes válidos: {', '.join(CONTINENTES_VALIDOS)}")
        continente = input("  Continente: ").strip()
        if continente == "":
            print("  Error: El continente no puede estar vacío. Intente de nuevo.")
            continue
        for c in CONTINENTES_VALIDOS:
            if normalizar_texto(c) == normalizar_texto(continente):
                return c
        print("  Error: Continente no reconocido. Ingrese uno de la lista.")

def agregar_pais(paises):
    """Solicita datos al usuario y agrega un nuevo país a la lista."""
    print("\n  --- Agregar nuevo país ---")
    nombre     = pedir_nombre(paises)
    poblacion  = pedir_entero_positivo("Población")
    superficie = pedir_entero_positivo("Superficie (km²)")
    continente = pedir_continente()
    nuevo = {
        'nombre': nombre,
        'poblacion': poblacion,
        'superficie': superficie,
        'continente': continente
    }
    paises.append(nuevo)
    print(f"\n  País '{nombre}' agregado correctamente.")
    return paises

def actualizar_pais(paises):
    """Busca un país por nombre y permite actualizar su población y/o superficie."""
    print("\n  --- Actualizar país ---")
    nombre = input("  Nombre del país a actualizar: ").strip()
    for p in paises:
        if p['nombre'].lower() == nombre.lower():
            print(f"\n  País encontrado: {p['nombre']}")
            print(f"  Población actual : {p['poblacion']:,}")
            print(f"  Superficie actual: {p['superficie']:,} km²")
            nueva_pob = input("\n  Nueva población (Enter para no cambiar): ").strip()
            nueva_sup = input("  Nueva superficie (Enter para no cambiar): ").strip()
            if nueva_pob != "":
                try:
                    valor = int(nueva_pob)
                    if valor > 0:
                        p['poblacion'] = valor
                        print("  Población actualizada.")
                    else:
                        print("  Valor inválido, población no cambiada.")
                except ValueError:
                    print("  Valor inválido, población no cambiada.")
            if nueva_sup != "":
                try:
                    valor = int(nueva_sup)
                    if valor > 0:
                        p['superficie'] = valor
                        print("  Superficie actualizada.")
                    else:
                        print("  Valor inválido, superficie no cambiada.")
                except ValueError:
                    print("  Valor inválido, superficie no cambiada.")
            return paises
    print(f"  País '{nombre}' no encontrado.")
    return paises

def buscar_por_nombre(paises):
    """Busca países cuyo nombre contenga el texto ingresado (coincidencia parcial)."""
    print("\n  --- Buscar país por nombre ---")
    busqueda = input("  Ingrese nombre o parte del nombre: ").strip().lower()
    if busqueda == "":
        print("  Error: Ingrese un texto para buscar")
        return []
    resultados = []
    for p in paises:
        if busqueda in p['nombre'].lower():
            resultados.append(p)
    if len(resultados) == 0:
        print(f"  No se encontraron países con '{busqueda}'")
    else:
        print(f"\n  {len(resultados)} resultado(s) encontrado(s):")
        print(f"  {'NOMBRE':<25} {'POBLACIÓN':>14}  {'SUPERFICIE':>13}  CONTINENTE")
        print("  " + "-"*70)
        for r in resultados:
            mostrar_pais(r)
    return resultados

def filtrar_por_continente(paises):
    """Filtra y muestra países que pertenezcan al continente indicado."""
    print("\n  --- Filtrar por continente ---")
    print(f"  Continentes disponibles: {', '.join(CONTINENTES_VALIDOS)}")
    continente_buscar = input("  Ingrese continente: ").strip()
    if continente_buscar == "":
        print("  Error: Ingrese un continente")
        return []
    resultados = []
    for p in paises:
        if p['continente'].lower() == continente_buscar.lower():
            resultados.append(p)
    if len(resultados) == 0:
        print(f"  No hay países registrados en '{continente_buscar}'")
    else:
        print(f"\n  Países en {continente_buscar} ({len(resultados)}):")
        print(f"  {'NOMBRE':<25} {'POBLACIÓN':>14}  {'SUPERFICIE':>13}")
        print("  " + "-"*55)
        for r in resultados:
            print(f"  {r['nombre']:<25} {r['poblacion']:>14,}  {r['superficie']:>13,} km²")
    return resultados

def filtrar_por_poblacion(paises):
    """Filtra países dentro de un rango de población ingresado por el usuario."""
    print("\n  --- Filtrar por rango de población ---")
    try:
        minimo = int(input("  Población mínima: "))
        maximo = int(input("  Población máxima: "))
        if minimo < 0 or maximo < 0:
            print("  Error: Los valores no pueden ser negativos")
            return []
        if minimo > maximo:
            print("  Error: El mínimo no puede ser mayor al máximo")
            return []
        resultados = []
        for p in paises:
            if minimo <= p['poblacion'] <= maximo:
                resultados.append(p)
        if len(resultados) == 0:
            print(f"  No hay países con población entre {minimo:,} y {maximo:,}")
        else:
            print(f"\n  Países encontrados ({len(resultados)}):")
            print(f"  {'NOMBRE':<25} {'POBLACIÓN':>14}  CONTINENTE")
            print("  " + "-"*55)
            for r in resultados:
                print(f"  {r['nombre']:<25} {r['poblacion']:>14,}  {r['continente']}")
        return resultados
    except ValueError:
        print("  Error: Ingrese números enteros válidos")
        return []

def filtrar_por_superficie(paises):
    """Filtra países dentro de un rango de superficie ingresado por el usuario."""
    print("\n  --- Filtrar por rango de superficie ---")
    try:
        minimo = int(input("  Superficie mínima (km²): "))
        maximo = int(input("  Superficie máxima (km²): "))
        if minimo < 0 or maximo < 0:
            print("  Error: Los valores no pueden ser negativos")
            return []
        if minimo > maximo:
            print("  Error: El mínimo no puede ser mayor al máximo")
            return []
        resultados = []
        for p in paises:
            if minimo <= p['superficie'] <= maximo:
                resultados.append(p)
        if len(resultados) == 0:
            print(f"  No hay países con superficie entre {minimo:,} y {maximo:,} km²")
        else:
            print(f"\n  Países encontrados ({len(resultados)}):")
            print(f"  {'NOMBRE':<25} {'SUPERFICIE':>13}  CONTINENTE")
            print("  " + "-"*55)
            for r in resultados:
                print(f"  {r['nombre']:<25} {r['superficie']:>13,} km²  {r['continente']}")
        return resultados
    except ValueError:
        print("  Error: Ingrese números enteros válidos")
        return []

def ordenar_paises(paises):
    """Muestra un submenú para ordenar los países por distintos criterios."""
    print("\n  --- Ordenar países ---")
    print("  1. Por nombre (A-Z)")
    print("  2. Por nombre (Z-A)")
    print("  3. Por población (menor a mayor)")
    print("  4. Por población (mayor a menor)")
    print("  5. Por superficie (menor a mayor)")
    print("  6. Por superficie (mayor a menor)")
    opcion = input("\n  Elija una opción (1-6): ").strip()
    copia = paises[:]  # Trabajamos sobre una copia para no modificar el original
    criterios = {
        '1': (lambda x: x['nombre'], False, "nombre (A-Z)"),
        '2': (lambda x: x['nombre'], True,  "nombre (Z-A)"),
        '3': (lambda x: x['poblacion'], False, "población ascendente"),
        '4': (lambda x: x['poblacion'], True,  "población descendente"),
        '5': (lambda x: x['superficie'], False, "superficie ascendente"),
        '6': (lambda x: x['superficie'], True,  "superficie descendente"),
    }
    if opcion not in criterios:
        print("  Opción inválida")
        return paises
    clave, reverso, descripcion = criterios[opcion]
    copia.sort(key=clave, reverse=reverso)
    print(f"\n  Ordenado por {descripcion}:")
    print(f"  {'NOMBRE':<25} {'POBLACIÓN':>14}  {'SUPERFICIE':>13}  CONTINENTE")
    print("  " + "-"*70)
    for p in copia:
        mostrar_pais(p)
    return copia

def estadisticas(paises):
    """Calcula y muestra estadísticas generales del dataset."""
    if len(paises) == 0:
        print("  No hay datos para mostrar estadísticas.")
        return
    print("\n  --- Estadísticas generales ---")
    # Inicializar con el primer país
    mayor_pob = paises[0]
    menor_pob = paises[0]
    mayor_sup = paises[0]
    menor_sup = paises[0]
    suma_pob = 0
    suma_sup = 0
    cont_continentes = {}
    # Recorrer todos los países
    for p in paises:
        suma_pob += p['poblacion']
        suma_sup += p['superficie']
        if p['poblacion'] > mayor_pob['poblacion']:
            mayor_pob = p
        if p['poblacion'] < menor_pob['poblacion']:
            menor_pob = p
        if p['superficie'] > mayor_sup['superficie']:
            mayor_sup = p
        if p['superficie'] < menor_sup['superficie']:
            menor_sup = p
        # Contar países por continente
        cont_continentes[p['continente']] = cont_continentes.get(p['continente'], 0) + 1
    promedio_pob = suma_pob // len(paises)
    promedio_sup = suma_sup // len(paises)
    print(f"\n  POBLACIÓN")
    print(f"  {'Mayor población:':<25} {mayor_pob['nombre']} ({mayor_pob['poblacion']:,})")
    print(f"  {'Menor población:':<25} {menor_pob['nombre']} ({menor_pob['poblacion']:,})")
    print(f"  {'Promedio de población:':<25} {promedio_pob:,}")
    print(f"\n  SUPERFICIE")
    print(f"  {'Mayor superficie:':<25} {mayor_sup['nombre']} ({mayor_sup['superficie']:,} km²)")
    print(f"  {'Menor superficie:':<25} {menor_sup['nombre']} ({menor_sup['superficie']:,} km²)")
    print(f"  {'Promedio de superficie:':<25} {promedio_sup:,} km²")
    print(f"\n  PAÍSES POR CONTINENTE")
    for c, cant in sorted(cont_continentes.items()):
        print(f"  {c:<20}: {cant} país/es")
