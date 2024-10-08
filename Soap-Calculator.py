import matplotlib.pyplot as plt

liste_saponification_naoh = [["abricot", 139], ["amande douce", 139], ["arachide", 137], ["argan", 136], ["avocat", 133], ["babassu", 175], ["boabab", 143], ["bourraches", 135], ["café", 128], ["camélia", 139], ["camelina", 134], ["canneberge", 135], ["canola", 133], ["carthame", 137], ["cassis", 133], ["cerises", 135], ["chanvre", 138], ["chardon marie", 126], ["citrouille", 139], ["colza", 124], ["coco", 183], ["coprah", 232], ["coton", 138], ["crisco", 137], ["cumin noir", 135], ["emu", 135], ["framboise", 134], ["fruit de la passion", 130], ["germe du blé", 130], ["jojoba ", 66], ["karanja", 131], ["kukui", 135], ["lin", 135], ["macadamia", 139], ["maïs", 137], ["mangues", 128], ["monoi de tahiti", 182], ["neem", 139], ["noisette", 139], ["noix", 135], ["oeillettes", 138], ["olive", 135], ["onagre", 136], ["palme", 142], ["palmiste", 176], ["pêches", 136], ["perilla", 135], ["pistache", 133], ["raisin", 129], ["ricin", 128], ["rose musquée", 133], ["sésame", 134], ["soja", 136], ["soja hydrogéné", 136], ["son de riz", 128], ["tamanu", 148], ["tournesol", 135], ["visons", 140]]

def TypeHuile (): #permet d'afficher les choix d'huiles à l'utilisateur
    print("Les choix d'huiles disponibles sont :")
    for type_huiles in liste_saponification_naoh:
        print("-",type_huiles[0],";")
        
def CalculQuantiteSoude (MasseHuile, IndiceSapo):
    QSoude=MasseHuile*IndiceSapo/1000
    return QSoude

def AfficheTypeSavon (Taux):
    if Taux < 0:
        print("Le savon est caustique et dangereux.")
        type_savon="Caustique & dangereux"
    elif Taux < 5:
        print("La marge de sécurité de 5 % n'est pas respectée.")
        type_savon="Marge de sécurité non respectée"
    elif (Taux > 5) and (Taux < 8):
        print("Le savon est peu surgras et par conséquent peu doux.")
        type_savon="Peu surgras et peu doux"
    elif (Taux > 8) and (Taux < 10):
        print("Le savon est surgras, il est doux et par conséquent idéal.")
        type_savon="surgras, doux et idéal"
    elif (Taux > 10) and (Taux < 12):
        print("Le savon est très surgras et très mou.")
        type_savon="très surgras et très mou"
    elif (Taux > 12):
        print("Le savon est trop riche en huile et risque de déphaser lors de la fabrication.")
        type_savon="trop riche, risque de déphasage"
    return type_savon

def TauxSurgraissage (MasseSoude, MasseHuileTotale, IndiceSapoMelange):
    TauxPredit=((MasseHuileTotale-(MasseSoude/IndiceSapoMelange*1000))/MasseHuileTotale)*100
    return TauxPredit

TypeHuile() #Présente les choix d'huiles disponibles a l'utilisateur

continuer=True
soude_totale_theorique=0
masse_totale_huiles=0
indice_sapo_melange=0
synthese=[]
while continuer : #Demande les types d'huiles et les masses à utiliser pour la saponification
    huiles = [huile[0] for huile in liste_saponification_naoh]
    indices_saponification = [huile[1] for huile in liste_saponification_naoh]
    TypeHuile=str(input("Préciser le type d'huile que vous souhaitez ajouter :"))
    
    if TypeHuile in huiles:
        MasseHuile=float(input("Entrer la quantité d'huile (en g):"))
        index = huiles.index(TypeHuile)
        IndiceSapo = indices_saponification[index]
        masse_soude_theorique = CalculQuantiteSoude(MasseHuile,IndiceSapo)
        soude_totale_theorique += masse_soude_theorique
        masse_totale_huiles += MasseHuile
        indice_sapo_melange += IndiceSapo*MasseHuile
        synthese.append([TypeHuile, MasseHuile])
    else:
        print("L'huile ",TypeHuile," n'est pas reconnue.")

    demande=str(input("Tapez 'fini' si vous ne souhaitez pas ajouter d'autre huile à votre savon. "))
    if demande == "fini":
        continuer = False
        print("La masse de soude pour saponifier totalement vos ",masse_totale_huiles," grammes d'huiles est de ",soude_totale_theorique," g.")
indice_sapo_melange = indice_sapo_melange / masse_totale_huiles

continuer=True #Demande de la masse de soude à utiliser pour la saponification
while continuer :
    MasseSoude=float(input("Entrer la quantité prévue de soude à utiliser (en g):"))
    while MasseSoude<0:
            print("La quantité de soude ne peut pas être négative")
            MasseSoude=float(input("Entrer la quantité prévue de soude à utiliser (en g): "))

    Taux=TauxSurgraissage (MasseSoude, masse_totale_huiles, indice_sapo_melange)
    print("Pour une masse de ",MasseSoude," g de soude, le taux de surgraissage du savon sera de ",Taux," %.")
    AfficheTypeSavon(Taux)

    demande=int(input("Tapez 0 si vous voulez quitter ce calcul ou n'importe quel autre chiffre si vous souhaitez continuer."))
    if demande == 0:
        continuer = False

SoudePesee=float(input("Renseigner la masse de soude utilisée (en g) :")) #Calcul du taux de surgraissage en fonction de la masse de soude pesée
while SoudePesee<0:
    print("La quantité de soude pesée ne peut pas être négative")
    SoudePesee=float(input("Renseigner la masse de soude utilisée (en g): "))
Taux=TauxSurgraissage (SoudePesee, masse_totale_huiles, indice_sapo_melange)
print("Le taux de surgraissage calculé est de ",Taux,"%.")
type_savon=AfficheTypeSavon(Taux)
synthese.append(["Soude (g)", SoudePesee])
synthese.append(["Taux (%)", Taux])
synthese.append(["Type de savon", type_savon])

#autres MP
MasseEau=float(input("Entrer la masse d'eau pesée (en g):"))
while MasseEau<0:
    print("La quantité d'eau ne peut pas être négative")
    MasseEau=float(input("Entrer la masse d'eau pesée (en g):"))
synthese.append(["Eau (g)", MasseEau])

MasseParfum=float(input("Entrer la masse de parfum pesée (en g):"))
while MasseParfum<0:
    print("La quantité de parfum ne peut pas être négative")
    MasseParfum=float(input("Entrer la masse de parfum pesée (en g):"))
synthese.append(["Parfum (g)", MasseParfum])

MasseColorant=float(input("Entrer la masse de colorant pesée (en g):"))
while MasseColorant<0:
    print("La quantité de colorant ne peut pas être négative")
    MasseColorant=float(input("Entrer la masse de colorant pesée (en g):"))
synthese.append(["Colorant (g)", MasseColorant])

print(synthese)
print("-----------Synthèse-----------")
for lst in synthese:
        print("-",lst[0]," : ",lst[1],";")

plt.figure(figsize = (10, 5)) #Affichage graphique
x = [MasseEau, MasseParfum, MasseColorant, masse_totale_huiles, SoudePesee]
normalize=True
plt.pie(x, labels = ["Eau", "Parfum", "Colorant", "Matières grasses", "Soude"],
           colors = ['blue', 'green', 'yellow','brown','red'],
           explode = [0, 0, 0, 0, 0],
           autopct = lambda x: str(round(x, 1)) + "%",
           pctdistance = 0.4, labeldistance = 0.6,
           shadow = True)
plt.title("Composition finale du savon fabriqué")
plt.legend()
