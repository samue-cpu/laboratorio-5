print("laboratorio 5, ")

########################################################
#ejercicio 1
####################################################

edad= [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# A) ordenar y encontrar numero minimo y maximo
edad.sort()
print(edad)
#minimo y maximo
minimo=edad[0]
maximo = edad[-1]
print("el minimo y maximo es:",minimo, maximo)

#  B)añadimos de nuevo el numero max,min
edad.append(19)
edad.append(26)
print(edad)
# C) ENCONTRAR LA MEDIANA
edad.sort()
print(edad)
a = int(edad[5])
b =int(edad[6])
mediana=(a+b)/2
print(int(mediana))

# D) promedio de edad
promedio = sum(edad)/len(edad)
print(promedio)

# C) encontrar el rango de edades
minimo = edad[0]
maximo = edad[-1]
rango_edad = maximo -minimo
print("el rango de edades es:", rango_edad)
#################################################################
#EJERCICIO 2
################################################################

# ENCONTRAR PALABRAS UNICAS CON SPLIT, SETS
frase ="Soy profesor y me encanta inspirar y enseñar a la gente"
print(frase.split())
print(set(frase))

###############################################################
#EJERCICIO 3
###############################################################

lista1 = [1, 2, 3, 4, 5, 6,7, 8, 9, 10]
lista2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
lista3 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
#A) convertir de lista a conjunto
lista1 = set(lista1)
lista2 = set(lista2)
lista3 = set(lista3)
print(lista1, lista2, lista3)

# B ) ENCONTRAR LO CONJUNTOS DE TRES LISTAS (INTERSECCION)
interseccion_lista1_lista2 = lista1.intersection(lista2)
print(interseccion_lista1_lista2)
interseccion_final = interseccion_lista1_lista2.intersection(lista3)
print(interseccion_final)

# C) ENCONTRA LOS ELEMENTOS DE LOS CONJUNTOS (UNION)
lista4 = lista1.union(lista2, lista3)
print(lista4)
# D) ENCONTRE LOS ELEMENTOS DE LISTA 1, MENOS LISTA 3
lista_final=lista1.difference(lista3)
print(lista_final)

# E)convertir a duplas, y sumar primero y ultimo elemento
lista1=tuple(lista1)
lista2 =tuple(lista2)
lista3=tuple(lista3)
print(lista1,  lista2, lista3)

#sumar primero y ultimo elemento
dupla1 = lista1[0] + lista1[-1]
dupla2 = lista2[0] +lista2[-1]
dupla3 = lista3[0] + lista3[-1]
print("la suma es:", dupla1, dupla2, dupla3)
#############################################
# ejercicio 4
#############################################

s1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)] 
s2 = [("one", 1), ("two", 2), ("six", 6)] 
# A) CONVERTIR A CONJUNTOS 
s1=set(s1)
s2=set(s2)
print(s1, s2)

# B) ENCONTRA EL COMUN (INTERSECCION)
s3 = s1.intersection(s2)
print(s3)

# C) ENCONTRA EL UNICO ELEMENTO S1 Y S2
s4 = s1.union(s2)
print(s4)
# D) ENCUENTRE ELEMENTOS DE S3 Y S4
nueva_lista = s3.union(s4)
convertir = list(nueva_lista )
print(nueva_lista)