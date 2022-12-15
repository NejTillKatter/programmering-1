import random

#Definerar funktionen för att ge nya kort till gekort (handen)
def nya(gekort, kortlek):

    for _ in range(3):

        nytt_kort = kortlek.pop(-1)
        gekort.append(nytt_kort)



#Popar allt ifrån listan gekort
def pop(gekort):
    for _ in range(3):
        gekort.pop(-1)



#Skapa kortleken
färger = [ "hjärter", "ruter", "spader", "klöver" ]

kort = [ "ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "knekt", "dam", "kung" ]

kortvärde = {"ess" : 11, "knekt" : 10, "dam" : 10, "kung" : 10}

kortlek = []

gekort = []

#Gör så att listan kortlek får alla kort i en kortlek
for färg in färger:
    for k in kort:
        kortlek.append(färg + " " + k)



#Shuffla listan kortlek
random.shuffle(kortlek)



while True:
    #Input så man kan välja om man vill börja eller inte
    börja = input("vill du börja spela Black Jack? Ja eller Nej\n:").capitalize()
    
    #Om inputen börja är Ja händer det under indenten
    if börja == "Ja":
        
        #Ger ut korten till gekort (handen)
        nya(gekort, kortlek)

        #Skriv ut korten i handen med , som separation
        print(gekort, sep=", ")
        
        #Kallar en funktion som tar bort allt från listan gekort
        pop(gekort)

        #Delar ut datorns kort


        


    elif börja == "Nej":
        
        #Avslutar programmet om man svarar nej på inputen börja
        break
    else:
        print("\nSkriv Ja eller nej\n")