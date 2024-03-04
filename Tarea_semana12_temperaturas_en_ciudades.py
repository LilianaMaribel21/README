# Crear una matriz 3D para almacenar datos de temperaturas
# Primera dimensión: Ciudades (3 ciudades)
# Segunda dimensión: Días de la semana (7 días)
# Tercera dimensión: Semanas (4 semanas)

temperaturas = [

    [  #  Santo Domingo
        [  # Semana 1
            {"day": "Lunes", "temp": 94},
            {"day": "Martes", "temp": 89},
            {"day": "Miércoles", "temp": 56},
            {"day": "Jueves", "temp": 70},
            {"day": "Viernes", "temp": 82},
            {"day": "Sábado", "temp": 76},
            {"day": "Domingo", "temp": 93}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 92},
            {"day": "Martes", "temp": 84},
            {"day": "Miércoles", "temp": 80},
            {"day": "Jueves", "temp": 79},
            {"day": "Viernes", "temp": 55},
            {"day": "Sábado", "temp": 97},
            {"day": "Domingo", "temp": 69}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 96},
            {"day": "Martes", "temp": 78},
            {"day": "Miércoles", "temp": 47},
            {"day": "Jueves", "temp": 65},
            {"day": "Viernes", "temp": 99},
            {"day": "Sábado", "temp": 97},
            {"day": "Domingo", "temp": 88}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 95},
            {"day": "Martes", "temp": 67},
            {"day": "Miércoles", "temp": 76},
            {"day": "Jueves", "temp": 99},
            {"day": "Viernes", "temp": 78},
            {"day": "Sábado", "temp": 88},
            {"day": "Domingo", "temp": 92}
        ]
    ],
    [  #  Quito
        [  # Semana 1
            {"day": "Lunes", "temp": 72},
            {"day": "Martes", "temp": 72},
            {"day": "Miércoles", "temp": 86},
            {"day": "Jueves", "temp": 94},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 85},
            {"day": "Domingo", "temp": 97}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 85},
            {"day": "Martes", "temp": 73},
            {"day": "Miércoles", "temp": 78},
            {"day": "Jueves", "temp": 88},
            {"day": "Viernes", "temp": 70},
            {"day": "Sábado", "temp": 65},
            {"day": "Domingo", "temp": 99}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 94},
            {"day": "Martes", "temp": 87},
            {"day": "Miércoles", "temp": 47},
            {"day": "Jueves", "temp": 55},
            {"day": "Viernes", "temp": 65},
            {"day": "Sábado", "temp": 93},
            {"day": "Domingo", "temp": 40}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 90},
            {"day": "Martes", "temp": 77},
            {"day": "Miércoles", "temp": 33},
            {"day": "Jueves", "temp": 60},
            {"day": "Viernes", "temp": 74},
            {"day": "Sábado", "temp": 99},
            {"day": "Domingo", "temp": 61}
        ]
    ],
    [   #  Puyo
        [  # Semana 1
            {"day": "Lunes", "temp": 54},
            {"day": "Martes", "temp": 83},
            {"day": "Miércoles", "temp": 65},
            {"day": "Jueves", "temp": 95},
            {"day": "Viernes", "temp": 69},
            {"day": "Sábado", "temp": 92},
            {"day": "Domingo", "temp": 72}
        ],
        [  # Semana 2
            {"day": "Lunes", "temp": 68},
            {"day": "Martes", "temp": 44},
            {"day": "Miércoles", "temp": 76},
            {"day": "Jueves", "temp": 88},
            {"day": "Viernes", "temp": 99},
            {"day": "Sábado", "temp": 46},
            {"day": "Domingo", "temp": 49}
        ],
        [  # Semana 3
            {"day": "Lunes", "temp": 77},
            {"day": "Martes", "temp": 85},
            {"day": "Miércoles", "temp": 96},
            {"day": "Jueves", "temp": 74},
            {"day": "Viernes", "temp": 79},
            {"day": "Sábado", "temp": 87},
            {"day": "Domingo", "temp": 99}
        ],
        [  # Semana 4
            {"day": "Lunes", "temp": 83},
            {"day": "Martes", "temp": 96},
            {"day": "Miércoles", "temp": 89},
            {"day": "Jueves", "temp": 73},
            {"day": "Viernes", "temp": 99},
            {"day": "Sábado", "temp": 84},
            {"day": "Domingo", "temp": 60}
        ]
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
Ciudades = ["Santo Domingo", "Quito", "Puyo"]
for ciudad_idx, ciudad in enumerate(temperaturas):
    for semana_idx, semana in enumerate(ciudad):
        suma_temperaturas = sum([dia["temp"] for dia in semana])
        promedio = suma_temperaturas / len(semana)
        print(f"Promedio de temperaturas para {Ciudades[ciudad_idx]}, Semana {semana_idx + 1}: {promedio: .1f} °C")