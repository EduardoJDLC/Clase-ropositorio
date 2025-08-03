#texto_variado = "Palabra 123 +. #$%&"
#print(type(texto_variado))

#Podemos utilizar comillas triples para que el texto se muestre con la cadena que hemos escrito
#print("""" 
#   Funcionamiento de\
 #  programa: (opciones)   
 #  -1 Para acceder a opciones
 #  -2 Para salir
 #     """)
##############################################################################################################
#Subscripting e indexado
#texto = "Python"
#print(texto[0])
#print(texto[5])
#print(texto[-1])
#print(texto[-6])

#print(texto[6]) #Error No podemos acceder a una posición que no existe
#print(texto[-7]) #Error No podemos acceder a una posicion que no existe

#letra = texto[0]
#print(letra)
#texto[0] ="p" #No podemos modificar una cadena
#letra = "p"
#print(letra)

#texto_compuesto = letra + texto[1] #Concatenación
#print(texto_compuesto)
#################################################################################################################
#Slicion o Substringing
#texto = "Python"
#print(texto[0:3])
#print(texto[0:-3])
#print(texto[0;-2])
#print(texto[2:])
#print(texto[:3])
#print(texto[-3::-1])
#print(texto[::-1])
#print(texto[1:50])
#print(texto[2:2])
#######################################################################################################################
#Cadenas y Formatos
#texto = "Hola mundo! Buenastardes"
#print(texto.lower()) #Minusculas
#print(texto.upper()) #Mayusculas
#print(texto.capitalize()) #La primera en mayuscula
#print(texto.title()) #Inicial de cada palabra con mayuscula
#print(texto.swapcase()) #Intercambia las letras entre mayusculas y minusculas
#texto = texto.upper()
#print(texto)

print("{} + {} = {}".format(1, 2, 1 + 2))
print("{} + {} = {}".format("Hola", "mundo", "Hola mundo"))
print("{:.3f} + {:.4f} = {}".format(2, 3, 2 + 3))
print("{1} + {0} = {2}".format(2, 3, 2 + 3))
print("{2} + {0} = {1}".format("Hola", "mundo", "Hola mundo"))
print("{:d} = {:b} = {:o} = {:x}".format(15, 15, 15, 15))
