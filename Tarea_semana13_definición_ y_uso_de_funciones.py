# Tarea 13 Definición y uso de funciones en programación
# Desarrollar una función para calcular la temperatura promedio de las ciudades

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

# Ciudades para calcular la temperatura promedio
ciudades = ["Santo Domingo", "Quito", "Puyo"]

# Calculamos los promedios de temperaturas
def calcular_promedio_semanal(temperaturas, semana, ciudades):
    resultados = []
    if 2 <= semana <= 3:
        for ciudad_temperaturas in temperaturas:
            semana_temperaturas = ciudad_temperaturas[semana - 2]
            total_temp = sum(dia['temp'] for dia in semana_temperaturas)
            promedio = total_temp / len(semana_temperaturas)
            resultados.append(promedio)
    else:
        # Si el usuario ingresa un valor incorrecto mostramos el siguiente mensaje
        print("El número de semana que ingreso es incorrecto. Se debe ingresar entre 1 y 4.")
    return resultados

# Solicitar datos
semana = int(input("Ingresar el número de semana (1-4): "))

# Ejecutamos la función y reflejamos los resultados
promedios_semanales = calcular_promedio_semanal(temperaturas, semana, ciudades)

# Imprimimos los resultados
if promedios_semanales:
    print(f"\nPromedios de temperatura para la semana {semana} en todas las ciudades:")
    for i, promedio in enumerate(promedios_semanales):
        print(f"{ciudades[i]}: {promedio:.2f}°C")

# Fin de la función
