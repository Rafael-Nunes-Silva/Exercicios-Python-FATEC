dias = float(input("Insira a quantidade de dias: "))
horas = float(input("Insira a quantidade de horas: "))
minutos = float(input("Insira a quantidade de minutos: "))
segundos = float(input("Insira a quantidade de segundos: "))

print("O total de segundos contidos em ", dias, "dias, ", horas, "horas, ", minutos, "minutos e ", segundos, "segundos é ", dias*86400 + horas*3600 + minutos*60 + segundos)
