def calcular_promedio_temperaturas(ciudades, temperaturas):
    """
    Calcula el promedio de temperaturas por semana para cada ciudad.

    :param ciudades: Lista de nombres de las ciudades.
    :param temperaturas: Lista de temperaturas estructuradas por ciudad y semana.
    :return: Diccionario con los promedios de temperatura.
    """
    promedios = {}

    for i, ciudad in enumerate(ciudades):
        promedios[ciudad] = []

        for semana, dias in enumerate(temperaturas[i]):
            promedio_semana = sum(dia["temp"] for dia in dias) / len(dias)
            promedios[ciudad].append(promedio_semana)

        # Agregar promedio total de todas las semanas
        promedio_total = sum(promedios[ciudad]) / len(promedios[ciudad])
        promedios[ciudad].append(promedio_total)

    return promedios


def obtener_promedio_ciudad(ciudad, promedios):
    """
    Obtiene el promedio de temperatura del mes de febrero para una ciudad específica.

    :param ciudad: Nombre de la ciudad.
    :param promedios: Diccionario con los promedios de temperatura.
    """
    if ciudad in promedios:
        print(f"Temperatura promedio en {ciudad} durante febrero: {promedios[ciudad][-1]:.2f}°C")
    else:
        print("Ciudad no encontrada.")


# Lista de nombres de las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Datos de temperaturas
temperaturas = [
    [  # Quito
        [
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 12},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 10},
            {"day": "Viernes", "temp": 12},
            {"day": "Sábado", "temp": 9},
            {"day": "Domingo", "temp": 9}
        ],
        [
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 10},
            {"day": "Domingo", "temp": 9}
        ],
        [
            {"day": "Lunes", "temp": 11},
            {"day": "Martes", "temp": 10},
            {"day": "Miércoles", "temp": 11},
            {"day": "Jueves", "temp": 11},
            {"day": "Viernes", "temp": 11},
            {"day": "Sábado", "temp": 11},
            {"day": "Domingo", "temp": 11}
        ],
        [
            {"day": "Lunes", "temp": 12},
            {"day": "Martes", "temp": 11},
            {"day": "Miércoles", "temp": 10},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 8},
            {"day": "Sábado", "temp": 8},
            {"day": "Domingo", "temp": 9}
        ]
    ],
    [  # Guayaquil
        [
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 24},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 23},
            {"day": "Sábado", "temp": 25},
            {"day": "Domingo", "temp": 29}
        ],
        [
            {"day": "Lunes", "temp": 23},
            {"day": "Martes", "temp": 26},
            {"day": "Miércoles", "temp": 30},
            {"day": "Jueves", "temp": 32},
            {"day": "Viernes", "temp": 25},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 31}
        ],
        [
            {"day": "Lunes", "temp": 25},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 26},
            {"day": "Jueves", "temp": 28},
            {"day": "Viernes", "temp": 29},
            {"day": "Sábado", "temp": 30},
            {"day": "Domingo", "temp": 31}
        ],
        [
            {"day": "Lunes", "temp": 26},
            {"day": "Martes", "temp": 28},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 31},
            {"day": "Sábado", "temp": 32},
            {"day": "Domingo", "temp": 33}
        ]
    ],
    [  # Cuenca
        [
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 8},
            {"day": "Sábado", "temp": 8},
            {"day": "Domingo", "temp": 8}
        ],
        [
            {"day": "Lunes", "temp": 8},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 8},
            {"day": "Sábado", "temp": 8},
            {"day": "Domingo", "temp": 8}
        ]
    ]
]

# Calcular y mostrar los promedios
datos_promedios = calcular_promedio_temperaturas(ciudades, temperaturas)
for ciudad in ciudades:
    obtener_promedio_ciudad(ciudad, datos_promedios)

ciudad_input = input("Ingrese el nombre de la ciudad para ver su temperatura promedio en febrero: ")
obtener_promedio_ciudad(ciudad_input, datos_promedios)