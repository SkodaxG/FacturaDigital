from subprocess import call
from os import walk, remove

#Guardar noms de tots els fitxers
f = []
for (dirpath, dirnames, filenames) in walk("./Factures per processar"):
    f.extend(filenames)
    break

#Filtrar els arxius pdf
pdfNames = []
for file in f:
    if file[-4:] == '.pdf':
        pdfNames.append(file)
        
#Crear arxius pdf
for pdf in pdfNames:
    inFile = "./Factures per processar/" + pdf
    outFile = "./Factures processades/" + pdf
    r = call(["./cpdf.exe", "-stamp-under", "Plantilles/plantilla.pdf", inFile, "-o", outFile])
    
    if r == 0:
        #Esborrar el fitxer
        remove(inFile)
        
        #Misatge a l'usuari
        print("Factura digital creada de: "+pdf)
    else:
        print("No s'ha pogut crear la factura digital de: " + pdf)