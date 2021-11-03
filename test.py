# este archivo es solo para probar la libreria procesador_texto.py
import procesador_texto as pt

print("CONTAR CARACTERES")
cad = input("Digita el texto: ")
num_car = pt.contar_caracteres(cad)
print(num_car, "caracteres en", cad)

pt.contar_palabras(input("Ingresar texto:"))