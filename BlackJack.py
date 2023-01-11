import random

#Definerar funktionen för att ge nya kort till gekort (handen)
def nya(gekort, kortlek):

    for _ in range(3):

        nytt_kort = kortlek.pop(-1)
        gekort.append(nytt_kort)



#Popar allt ifrån listan gekort
def nya(datorkort, kortlek):

    for _ in range(3):
        nya_kort = kortlek.pop(-1)
        datorkort.append(nya_kort)



def pop(gekort, datorkort):

    for _ in range(3):
        gekort.pop(-1)
        datorkort.pop(-1)



#Gör två listor n med alla nummer på korten och en med alla färgerna
färger = [ "hjärter", "ruter", "spader", "klöver" ]

kort = [ "ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "knekt", "dam", "kung" ]



#ger korten värde genom att splitta stringen i kortleken och ger värde utifrån kortet
def handsumma(hand):
    #Ge korten värde så man kan räkna ut poäng efter
    kortvärde = {"ess" : 10, "knekt" : 10, "dam" : 10, "kung" : 10, "10" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2}
    score = 0
    for card in hand:
        value = card.split()[1]
        score += kortvärde[value]

    return score

kortlek = []

gekort = []

datorkort = []




#Gör så att listan kortlek får alla kort i en kortlek
for färg in färger:
    for k in kort:
        kortlek.append(färg + " " + k)



#Shuffla listan kortlek så man inte får korten i en speciell ordning
random.shuffle(kortlek)



while True:
    #Input så man kan välja om man vill börja eller inte 
    #änvänds även i en loop så man kan köra flera gånger
    börja = input("vill du börja spela Black Jack? Ja eller Nej\n:").capitalize()
    


    #Om inputen börja är Ja händer det under indenten
    if börja == "Ja":

        #Ger ut korten (gekort) till handen
        nya(gekort, kortlek)

        #Skriv ut korten i handen med , som separation
        print(gekort, "är dina kort")
        print("Värdet är", handsumma(gekort))
        
        #Delar ut korten genom att kalla funktionen för att ge kort
        nya(datorkort, kortlek)

        print(datorkort, "är husets kort")
        print("värdet är", handsumma(datorkort))

        if handsumma(gekort) == handsumma(datorkort):
            print("Det blev lika")

        elif handsumma(gekort) == 30 and handsumma(datorkort) != 30:
            print("Vann")

        elif handsumma(gekort) == 21 and handsumma(datorkort) !=21:
            print("Vann")

        elif handsumma(gekort) == 10 and handsumma(datorkort) != 10:
            print("vann")

        elif handsumma(gekort) > handsumma(datorkort):
            print("Vann")


        pop(gekort, datorkort)



    elif börja == "Nej":
        
        #Avslutar programmet om man svarar nej på inputen börja
        break
    
    

    else:
        print("\nSkriv Ja eller Nej\n")