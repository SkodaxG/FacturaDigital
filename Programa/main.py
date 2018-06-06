from subprocess import call
from os import walk, remove
from subprocess import Popen

#Title print
print("\nCREADOR DE FACTURES DIGITALS\n")

#Guardar noms de tots els fitxers
f = []
for (dirpath, dirnames, filenames) in walk("../Factures per processar"):
    f.extend(filenames)
    break

#Filtrar els arxius pdf
pdfNames = []
for file in f:
    if file[-4:] == '.pdf':
        pdfNames.append(file)
        
#Crear arxius pdf
succededConversions = 0
for pdf in pdfNames:
    inFile = "../Factures per processar/" + pdf
    outFile = "../Factures processades/" + pdf
    r = call(["./cpdf.exe", "-stamp-under", "Plantilles/plantilla.pdf", inFile, "-o", outFile])
    
    if r == 0:
        #Una altre conversió exitosa
        succededConversions += 1

        #Esborrar el fitxer
        remove(inFile)
        
        #Misatge a l'usuari
        print("\n\t Factura digital creada de: "+pdf)
    else:
        print("\n\tNo s'ha pogut crear la factura digital de: " + pdf)

#Resum de la seqüència
if succededConversions > 0:
    print("\n\n S'han digitalitzat "+ str(succededConversions) +" factures de " + str(len(pdfNames)) + " possibles")

    #Obrir la carpeta de factures digitals
    Popen(r"explorer \\WIN-5JMR4Q95587\Documentacio\FacturaDigital\Factures processades") 
else:
    print("\n\n No s'ha digitalitzat cap factura!")

