segundos_str = input("Por favor, entre com o número de segundos: ")
total_segs = int(segundos_str)

horas = total_segs//3600
segs_restantes = total_segs%3600
minutos = segs_restantes //60
segs_restante_finais = segs_restantes %60

print(horas, " horas, ", minutos, " minutos e ", segs_restante_finais, " segundos.")
