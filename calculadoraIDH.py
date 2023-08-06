
#Este programa calcula el índice de esperanza de vida, índice de ingresos e índice de Eduación de un país que ha introducido el usuario


#Solicitar al usuario los tres índices

pais = input("Ingresa el nombre del país: ")
indice_esperanza_de_vida = float(input("Ingresa el índice de esperanza de vida del país: "))
indice_inbpc = float(input("Ingresa el índice de ingreso nacional bruto per cápita del país: "))
indice_de_educacion = float(input("Ingresa el índice de educación del país: "))


#Calcular el IDH utilizando la fórmula

idh = (indice_esperanza_de_vida * indice_inbpc * indice_de_educacion) ** (1/3)

#Mostrar el IDH en la consola

print("El IDH de", pais, " es: ", idh)

if idh >= 0.8: 
    print("El IDH de ", pais, " es alto.")
elif idh >= 0.5 and idh < 0.8: 
    print("El IDH de", pais, " es medio.")
else:
    print("El IDH de", pais, " es bajo.")