duracion_dalto = 1.5
duracion_rapido = 2.5
duracion_lento = 7.0
promedio_duracion = 4.0

#Inciso A
diferencia_rapido = round(100 - (duracion_dalto / duracion_rapido * 100), 1)

diferencia_lento = round(100 - duracion_dalto /duracion_lento * 100 , 1)

diferencia_promedio = round(100 - duracion_dalto / promedio_duracion * 100 , 1)

print(f'La diferencia porcentual entre el curso de dalto y el mas rapido es:  %{diferencia_rapido}')

print(f'La diferencia porcentual entre el curso de dalto y el mas lento es:  %{diferencia_lento}')

print(f'La diferencia porcentual entre el curso de dalto y el promedio es:  %{diferencia_promedio}')


#Inciso B 

crudo_otros = 5.0
crudo_dalto = 3.5

inservible_otros = round(100 - promedio_duracion / crudo_otros * 100 , 1)
inservible_dalto = round(100 - duracion_dalto / crudo_dalto * 100 , 1)

print(f'El porcentaje de material inservible de los otros cursos es:  %{inservible_otros}')
print(f'El porcentaje de material inservible de dalto es:  %{inservible_dalto}')
