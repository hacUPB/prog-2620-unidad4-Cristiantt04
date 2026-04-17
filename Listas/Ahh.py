flota = {
    "N123AA": {
        "modelo": "Boeing 787-9",
        "año": 2018,
        "horas_vuelo": 12500,
        "ciclos": 1350,
        "estado": "En servicio",
        "base": "DFW",
        "proxima_revision": "2023-07-15"
    },
    "N456AA": {
        "modelo": "Boeing 777-300ER",
        "año": 2014,
        "horas_vuelo": 26800,
        "ciclos": 2940,
        "estado": "En mantenimiento",
        "base": "MIA",
        "proxima_revision": "2023-03-30"
    }
}

# Añadir nueva aeronave
flota["N789AA"] = {
    "modelo": "Airbus A321neo",
    "año": 2022,
    "horas_vuelo": 1200,
    "ciclos": 420,
    "estado": "En servicio",
    "base": "LAX",
    "proxima_revision": "2024-01-10"
}

print

Placa = input("Ingresa la placa: ")
mod = input("Ingresa el modelo: ")
ano = float(input("Ingresa el año de la aeronave: "))
horas_vuelo = float(input("Ingresa las horas de vuelo: "))
ciclos = float(input("Ingresa el número de ciclos de la aeronave: "))
estado = input("Ingresa el estado de la aeronave: ")
base = input("Inresa la base: ")
proxima_revision = input("Ingresa la fecha de la proxima revision: ")

temp = {}

