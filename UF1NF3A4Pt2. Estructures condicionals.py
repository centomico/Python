#Exercisi2

any = int(input("posa un any: "))

if (any % 4 == 0 and any % 100 != 0) or (any % 400 == 0):
    print("és any de traspàs")
else:
    print("no es any de transpas")

#-----------------------------------------------------------

#exercisi3
import random

prediccio = int(input("quin numero reus que soritra del 1 al 6? (1, 2, 3, 4, 5, 6): "))
resultat = random.randint

if resultat == 1:
    print("ha sorit: 1")
elif resultat == 2:
    print("Ha sortit: 2")
elif resultat == 3:
    print("Ha sotit: 3")
elif resultat == 4:
    print("Ha sortit: 4")
elif resultat == 5:
    print("Ha sortit: 5")
elif resultat == 6:
    print("Ha sortit: 6")

if prediccio == resultat:
    print("has guanyat")
else:
    print("Ha guanyat el ordinador")

#-------------------------------------------------------

#exercisi4

nota_practiques = float(input("Nota de practiques: "))
nota_teoria = float(input("Nota de teoria: "))

mitjana = 0
total_pes = 0

if nota_practiques >= 3:
    mitjana += nota_practiques * 0.7
    total_pes += 0.7

if nota_teoria >= 3:
    mitjana += nota_teoria * 0.3
    total_pes += 0.3

if total_pes > 0:
    mitjana /= total_pes
else:
    mitjana = 0 

if mitjana < 5:
    print("has supses")
elif mitjana < 7:
    print("aporvat")
elif mitjana < 9:
    print("notable")
elif mitjana < 10:
    print("excel·lent")
else:
    print("matricula de honor")

#-------------------------------------------------------

#exercisi 5
#tes
