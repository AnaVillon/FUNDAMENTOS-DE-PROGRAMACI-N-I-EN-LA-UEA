# Lista de nombres de las ciudades
ciudades = ["Quito", "Guayaquil", "Cuenca"]

# Datos de temperaturas corregidos
temperaturas = [
    [   # Quito
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
    [   # Guayaquil
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
            {"day": "Lunes", "temp": 31},
            {"day": "Martes", "temp": 25},
            {"day": "Miércoles", "temp": 28},
            {"day": "Jueves", "temp": 30},
            {"day": "Viernes", "temp": 32},
            {"day": "Sábado", "temp": 26},
            {"day": "Domingo", "temp": 30}
        ],
        [
            {"day": "Lunes", "temp": 24},
            {"day": "Martes", "temp": 27},
            {"day": "Miércoles", "temp": 29},
            {"day": "Jueves", "temp": 31},
            {"day": "Viernes", "temp": 28},
            {"day": "Sábado", "temp": 27},
            {"day": "Domingo", "temp": 30}
        ]
    ],
    [   # Cuenca
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
        ],
        [
            {"day": "Lunes", "temp": 9},
            {"day": "Martes", "temp": 9},
            {"day": "Miércoles", "temp": 9},
            {"day": "Jueves", "temp": 9},
            {"day": "Viernes", "temp": 9},
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

# Calcular y mostrar el promedio
for i, ciudad in enumerate(ciudades):
    print(f"Temperaturas promedio en {ciudad}:")
    for semana, dias in enumerate(temperaturas[i]):
        promedio = sum(dia["temp"] for dia in dias) / len(dias)
        print(f"  Semana {semana + 1}: {promedio:.2f}°C")
    print()


Temperaturas promedio en Quito:
  Semana 1: 10.57°C
  Semana 2: 10.29°C
  Semana 3: 10.86°C
  Semana 4: 9.57°C

Temperaturas promedio en Guayaquil:
  Semana 1: 26.14°C
  Semana 2: 27.71°C
  Semana 3: 28.86°C
  Semana 4: 28.00°C

Temperaturas promedio en Cuenca:
  Semana 1: 8.57°C
  Semana 2: 8.43°C
  Semana 3: 8.71°C
  Semana 4: 8.43°C
