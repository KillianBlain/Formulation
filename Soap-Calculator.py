import matplotlib.pyplot as plt

#variables globales
IndiceCoco=183
IndiceKarite=128
IndiceOlive=135
IndiceAmande=137
QSoudeCoco=0
QSoudeKarite=0
QSoudeOlive=0
QSoudeAmande=0
MasseCoco=0
MasseKarite=0
MasseOlive=0
MasseAmande=0

#fonctions
def calculeQuantiteSoude (MasseHuile, IndiceSapo): 
    QSoude=MasseHuile*IndiceSapo/1000
    return QSoude

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

def TauxSurgraissage (MasseSoude, MasseCoco, MasseKarite, MasseOlive, MasseAmande):
    MasseHuileTotale=MasseCoco+MasseAmande+MasseKarite+MasseOlive
    PCoco=MasseCoco/MasseHuileTotale
    PKarite=MasseKarite/MasseHuileTotale
    POlive=MasseOlive/MasseHuileTotale
    PAmande=MasseAmande/MasseHuileTotale

    IndiceSapoMelange=(PCoco*IndiceCoco+PKarite*IndiceKarite+POlive*IndiceOlive+PAmande*IndiceAmande)

    TauxPredit=((MasseHuileTotale-(MasseSoude/IndiceSapoMelange*1000))/MasseHuileTotale)*100

    return TauxPredit

continuer=True #Demande des types d'huiles et des masses à utiliser pour la saponification
while continuer :
    TypeHuile=str(input("Préciser le type d'huile (coco, karité, olive ou amande douce):"))
    while ((TypeHuile != "coco") and (TypeHuile != "karité") and (TypeHuile != "olive") and (TypeHuile != "amande douce")):
        print("Seuls les choix suivants sont autorisés : coco, karité, olive ou amande douce")
        TypeHuile=str(input("Préciser le type d'huile (coco, karité, olive ou amande douce):")) 

    MasseHuile=float(input("Entrer la quantité d'huile (en g):"))
    while MasseHuile<0:
        print("La quantité d'huile ne peut pas être négative")
        MasseHuile=float(input("Entrer la quantité d'huile (en g):"))

    if TypeHuile == "coco":
        MasseCoco=MasseHuile
        QSoudeCoco=calculeQuantiteSoude (MasseCoco,IndiceCoco)
    elif TypeHuile == "karité":
        MasseKarite=MasseHuile
        QSoudeKarite=calculeQuantiteSoude (MasseKarite,IndiceKarite)
    elif TypeHuile == "olive":
        MasseOlive=MasseHuile
        QSoudeOlive=calculeQuantiteSoude (MasseOlive,IndiceOlive)
    elif TypeHuile == "amande douce":
        MasseAmande=MasseHuile
        QSoudeAmande=calculeQuantiteSoude (MasseAmande,IndiceAmande)

    demande=str(input("Tapez 'fini' si vous ne souhaitez pas ajouter d'autre huile à votre savon. "))
    if demande == "fini":
        continuer = False

QSoudeTheorique=QSoudeKarite+QSoudeAmande+QSoudeCoco+QSoudeOlive
print("La masse de soude pour saponifier totalement vos huiles est de ",QSoudeTheorique," g.")

continuer=True #Demande de la masse de soude à utiliser pour la saponification
while continuer :
    MasseSoude=float(input("Entrer la quantité prévue de soude à utiliser (en g):"))
    while MasseSoude<0:
            print("La quantité de soude ne peut pas être négative")
            MasseSoude=float(input("Entrer la quantité prévue de soude à utiliser (en g): "))

    Taux=TauxSurgraissage (MasseSoude, MasseCoco, MasseKarite, MasseOlive, MasseAmande)
    print("Pour une masse de ",MasseSoude," g de soude, le taux de surgraissage du savon sera de ",Taux," %.")
    TypeSavon=AfficheTypeSavon(Taux)

    demande=int(input("Tapez 0 si vous voulez quitter ce calcul ou n'importe quel autre chiffre si vous souhaitez continuer."))
    if demande == 0:
        continuer = False

SoudePesee=float(input("Renseigner la masse de soude utilisée (en g) :")) #Calcul du taux de surgraissage en fonction de la masse de soude pesée
while SoudePesee<0:
    print("La quantité de soude pesée ne peut pas être négative")
    SoudePesee=float(input("Renseigner la masse de soude utilisée (en g): "))
Taux=TauxSurgraissage (SoudePesee, MasseCoco, MasseKarite, MasseOlive, MasseAmande)
print("Le taux de surgraissage calculé est de ",Taux,"%.")

TypeSavon=AfficheTypeSavon(Taux)

MasseEau=float(input("Entrer la masse d'eau pesée (en g):")) #autres MP
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
x = [MasseEau, MasseParfum, MasseColorant, MasseCoco, MasseKarite, MasseOlive, MasseAmande, SoudePesee]
normalize=True
plt.pie(x, labels = ["Eau", "Parfum", "Colorant", "Coco", "Karité", "Olive", "Amande", "Soude"],
           colors = ['blue', 'green', 'yellow','brown','brown','brown','brown','red'],
           explode = [0, 0, 0, 0, 0, 0, 0, 0],
           autopct = lambda x: str(round(x, 1)) + "%",
           pctdistance = 0.4, labeldistance = 0.6,
           shadow = True)
plt.title("Composition finale du savon fabriqué")
plt.legend()
