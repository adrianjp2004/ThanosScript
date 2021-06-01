import os
from os import path

def dirSnap(dir):
	os.chdir(dir)
	elementos = os.listdir()
	nElementos = len(elementos)

	if nElementos % 2 == 0: nSnapElementos = nElementos / 2
	else: nSnapElementos = (nElementos - 1) / 2

	for i in range(0, int(nSnapElementos)):
		if path.isdir(elementos[i]): os.rmdir(elementos[i])
		else: os.remove(elementos[i]) 

def pause():
	pause = input()

if __name__ == "__main__":
	dirName = input("Ingrese nombre o ruta de la carpeta: ")

	if not path.isdir(dirName): print("Error: Carpeta no encontrada")
	else:
		dirSnap(dirName)
		print("Esto, dibuja una sonrisa en mi rostro >:)")
		pause()