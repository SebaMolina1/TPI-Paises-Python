Sistema de Gestión de Países

Trabajo Práctico Integrador — Programación 1
Tecnicatura Universitaria en Programación — UTN (A Distancia)
Cohorte Marzo 2026


Descripción

Aplicación de consola desarrollada en Python que permite gestionar información sobre países del mundo. Los datos se almacenan en una lista de diccionarios y se persisten en un archivo CSV. El sistema permite agregar, actualizar, buscar, filtrar, ordenar países y generar estadísticas.


Integrantes

Sebastian Molina
Andrés Manríquez


 Requisitos

Python 
No requiere librerías externas (solo csv que viene incluida en Python)


📁 Estructura del proyecto

TPI-Paises-Python/
│
├── main.py          # Menú principal y flujo del programa
├── funciones.py     # Todas las funciones del sistema
├── paises.csv       # Dataset base con 12 países
├── README.md        # Este archivo
└── documentacion/
    └── informe.pdf  # Documentación académica


▶️ Instrucciones de uso

Clonar o descargar el repositorio
Asegurarse de tener Python 3.x instalado
Ejecutar desde la terminal:

bashpython main.py

El programa carga los datos automáticamente al iniciar
Navegar por el menú con los números del 1 al 9


📌 Funcionalidades

Opciónes:
1 Ver todos los países cargados
2 Agregar un nuevo país
3 Actualizar población y superficie de un país
4 Buscar país por nombre (coincidencia parcial)
5 Filtrar por continente, rango de población o superficie
6 Ordenar por nombre, población o superficie (asc/desc)
7 Estadísticas: máximos, mínimos, promedios y cantidad por continente
8 Guardar cambios al CSV9Salir (con opción de guardar)


✅ Validaciones implementadas


El nombre no puede contener números ni estar vacío
Población y superficie deben ser números enteros positivos (acepta formato 45,000,000)
El continente debe ser uno de los válidos (acepta con o sin tildes)
No se permiten países duplicados
Nombres se guardan siempre con la primera letra en mayúscula
Mensajes claros de error en cada caso
Detección automática del separador del CSV (coma o punto y coma)



💡 Ejemplo de uso

Agregar un país:

Nombre: Uruguay
Población (solo números): 3500000
Superficie (km²) (solo números): 176215
Continentes válidos: América, Europa, Asia, África, Oceanía, Antártida
Continente: America

  País 'Uruguay' agregado correctamente.

Buscar por nombre parcial:

Ingrese nombre o parte del nombre: ar

  2 resultado(s) encontrado(s):
  Argentina                  Pob:   45,376,763  Sup:  2,780,400 km²  [America]
  Mejico                     Pob:  128,932,753  Sup:  1,964,375 km²  [America]

Estadísticas:

  POBLACIÓN
  Mayor población:          China (1,412,600,000)
  Menor población:          Australia (25,788,000)
  Promedio de población:    319,146,552

  SUPERFICIE
  Mayor superficie:         Canada (9,984,670 km²)
  Menor superficie:         Alemania (357,022 km²)
  Promedio de superficie:   3,919,530 km²


📄 Documentación



🎥 Video demostración



📚 Tecnologías utilizadas


Python 3.x — Lenguaje principal
Módulo csv — Lectura y escritura de archivos CSV
Estructuras de datos — Listas y diccionarios
Funciones — Modularización del código (una función = una responsabilidad)
