import matplotlib.pyplot as plt

def calculeQuantiteSoude (MasseHuile, IndiceSapo,name):
    QSoude=MasseHuile*IndiceSapo/1000
    print("La quantité de soude pour saponifier totalement " ,MasseHuile," grammes ",name," est de " ,QSoude, " g.")
    return QSoude

def TauxSurgraissage (Qsoude, SoudePesee):
    Taux=(((MasseHuile-((SoudePesee/IndiceSapo)*1000))/MasseHuile)*100)
    return Taux

def AfficheTypeSavon (Taux):
    if Taux < 0:
        print("Le savon est caustique et dangereux.")
    elif Taux < 5:
        print("La marge de sécurité de 5 % n'est pas respectée.")
    elif (Taux > 5) and (Taux < 8):
        print("Le savon est peu surgras et par conséquent peu doux.")
    elif (Taux > 8) and (Taux < 10):
        print("Le savon est surgras, il est doux et par conséquent idéal.")
    elif (Taux > 10) and (Taux < 12):
        print("Le savon est très surgras et très mou.")
    else: print("Le savon est trop riche en huile et risque de déphaser lors de la fabrication.")

def TauxSurgraissageEnFonctionDeLhuile (MasseHuile,MasseSoude,IndiceSapo):
    TauxPredit=(((MasseHuile-((MasseSoude/IndiceSapo)*1000))/MasseHuile)*100)
    print("Pour une masse de ",MasseSoude," g de soude, le taux de surgraissage du savon devrait être de ",TauxPredit," %.")
    return TauxPredit

#Masse d'huile et type d'huile
continuer=True
while continuer :
    TypeHuile=str(input("Préciser le type d'huile (coco, karité, olive ou amande douce):"))
    while ((TypeHuile != "coco") and (TypeHuile != "karité") and (TypeHuile != "olive") and (TypeHuile != "amande douce")):
        print("Seuls les choix suivants sont autorisés : coco, karité, olive ou amande douce")
        TypeHuile=str(input("Préciser le type d'huile (coco, karité, olive ou amande douce):")) 

    MasseHuile=float(input("Entrer la quantité d'huile (en g):"))
    while MasseHuile<0:
        print("La quantité d'huile ne peut pas être négative")
        MasseHuile=float(input("Entrer la quantité d'huile 'en g):"))
    
    demande=str(input("Tapez 'fini' si vous ne souhaitez pas ajouter d'autre huile à votre savon. "))
    if demande == "fini":
        continuer = False

#Quantité de soude et taux de surgraissage
continuer=True
while continuer :
    MasseSoude=float(input("Entrer la quantité prévue de soude à utiliser (en g):"))
    while MasseSoude<0:
            print("La quantité de soude ne peut pas être négative")
            MasseSoude=float(input("Entrer la quantité prévue de soude à utiliser (en g): "))

    if TypeHuile == "coco":
        IndiceSapo=183
        name="d'huile de coco"
    elif TypeHuile == "karité":
        IndiceSapo=128
        name="de beurre de karité"
    elif TypeHuile == "olive":
        IndiceSapo=135
        name="d'huile d'olive"
    elif TypeHuile == "amande douce":
        IndiceSapo=137
        name="d'amande douce"

    QSoude=calculeQuantiteSoude (MasseHuile,IndiceSapo,name)
    TauxPredit=TauxSurgraissageEnFonctionDeLhuile(MasseHuile,MasseSoude,IndiceSapo)
    TypeSavonPredit=AfficheTypeSavon(TauxPredit)

    demande=int(input("Tapez 0 si vous voulez quitter ce calcul"))
    if demande == 0:
        continuer = False

#Taux de surgraissage pour chaque type d'huile
QSoude=calculeQuantiteSoude (MasseHuile,183,"d'huile de coco")
TauxPredit=TauxSurgraissageEnFonctionDeLhuile(MasseHuile,MasseSoude,183)
TypeSavonPredit=AfficheTypeSavon(TauxPredit)
QSoude=calculeQuantiteSoude (MasseHuile,128,"de beurre de karité")
TauxPredit=TauxSurgraissageEnFonctionDeLhuile(MasseHuile,MasseSoude,128)
TypeSavonPredit=AfficheTypeSavon(TauxPredit)
QSoude=calculeQuantiteSoude (MasseHuile,135,"d'huile d'olive")
TauxPredit=TauxSurgraissageEnFonctionDeLhuile(MasseHuile,MasseSoude,135)
TypeSavonPredit=AfficheTypeSavon(TauxPredit)
QSoude=calculeQuantiteSoude (MasseHuile,137,"d'amande douce")
TauxPredit=TauxSurgraissageEnFonctionDeLhuile(MasseHuile,MasseSoude,137)
TypeSavonPredit=AfficheTypeSavon(TauxPredit)

#Masse de soude
SoudePesee=float(input("Renseigner la masse de soude utilisée (en g) :"))
while SoudePesee<0:
    print("La quantité de soude pesée ne peut pas être négative")
    SoudePesee=float(input("Renseigner la masse de soude utilisée (en g): "))
Taux=TauxSurgraissage (QSoude,SoudePesee)
print("Le taux de surgraissage calculé est de ",Taux,"%.")

TypeSavon=AfficheTypeSavon(Taux)

#Matières premières annexes
MasseEau=float(input("Entrer la masse d'eau pesée (en g):"))
while MasseEau<0:
    print("La quantité d'eau ne peut pas être négative")
    MasseEau=float(input("Entrer la masse d'eau pesée (en g):"))

MasseParfum=float(input("Entrer la masse de parfum pesée (en g):"))
while MasseParfum<0:
    print("La quantité de parfum ne peut pas être négative")
    MasseParfum=float(input("Entrer la masse de parfum pesée (en g):"))

MasseColorant=float(input("Entrer la masse de colorant pesée (en g):"))
while MasseColorant<0:
    print("La quantité de colorant ne peut pas être négative")
    MasseColorant=float(input("Entrer la masse de colorant pesée (en g):"))

#Affichage graphique
plt.figure(figsize = (10, 5))
x = [MasseEau, MasseParfum, MasseColorant, MasseHuile, SoudePesee]
normalize=True
plt.pie(x, labels = ["Eau", "Parfum", "Colorant", "huile", "Soude"],
           colors = ['blue', 'green', 'yellow','brown','red'],
           explode = [0, 0, 0, 0, 0],
           autopct = lambda x: str(round(x, 1)) + "%",
           pctdistance = 0.4, labeldistance = 0.6,
           shadow = True)
plt.title("Composition finale du savon fabriqué")
plt.legend()
