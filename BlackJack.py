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



#skapar en funktion som tar bort 
#korten man och huset har i handen
def pop(gekort, datorkort):

    for _ in range(3):
        gekort.pop(-1)
        datorkort.pop(-1)



#Gör två listor med alla nummer på korten och en med alla färgerna
#för att jag ska kunna göra 
färger = [ "hjärter", "ruter", "spader", "klöver" ]

kort = [ "ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "knekt", "dam", "kung" ]



#ger korten värde genom att splitta stringen 
#i kortleken och ger värde utifrån kortet
def handsumma(hand):
    #Ge korten värde så man kan räkna ut poäng när man fått sina kort
    kortvärde = {"ess" : 10, "knekt" : 10, "dam" : 10, "kung" : 10, "10" : 10, "9" : 9, "8" : 8, "7" : 7, "6" : 6, "5" : 5, "4" : 4, "3" : 3, "2" : 2}
    score = 0
    for card in hand:
        value = card.split()[1]
        score += kortvärde[value]

    return score



#Tomma listor som kan användas 
kortlek = []

gekort = []

datorkort = []




#Gör så att listan kortlek får alla kort i en kortlek
for färg in färger:
    for k in kort:
        kortlek.append(färg + " " + k)


#Shuffla listan kortlek så kortleken blandas
random.shuffle(kortlek)



#Man väljer ett användarnamn för att programmet ska kännas 
#mer personligt när man får resultaten
användarnamn = input("Välj ditt användarnamn\n:").capitalize()



#En loop för att man ska kunna spela flera gånger 
while True:
    
    #Gör så programmet avslutas om det fins färre än 6 kort i 
    #kortleken som används, för att det behövs 6 kort per omgång
    if len(kortlek) < 6:
        print(användarnamn, "det finns inte tillräckligt många kort")
        break
    
    #Input så man kan välja om man vill börja eller inte 
    #änvänds även i en loop så man kan köra flera gånger
    börja = input("vill du börja spela Flexible? Ja eller Nej\n:").capitalize()
    

    #Om inputen börja är Ja händer det under indenten
    if börja == "Ja":

        #Ger ut korten (gekort) till handen
        nya(gekort, kortlek)

        #Skriv ut korten i handen med , som separation
        print(gekort, "är dina kort")
        print("Värdet är", handsumma(gekort))
        
        #Delar ut korten till handen och datorn genom 
        #att kalla funktionen för att ge kort
        nya(datorkort, kortlek)

        #Printar ut datorns och dina kort
        print(datorkort, "är husets kort")
        print("värdet är", handsumma(datorkort))

        #Gör så att det blir lika om korten man har i handen 
        #är lika mycket värd som korten datorn har
        if handsumma(gekort) == handsumma(datorkort):
            print(användarnamn, "Det blev lika")

        #Gör så man vinner ifall kortens totala värde är 
        #30 och datorn inte har samma värde på korten
        elif handsumma(gekort) == 30 and handsumma(datorkort) != 30:
            print(användarnamn, "Du vann")

        elif handsumma(datorkort) ==30 and handsumma(gekort) != 30:
            print(användarnamn, "datorn vann")

        elif handsumma(gekort) == 21 and handsumma(datorkort) != 21:
            print(användarnamn, "Du vann")

        elif handsumma(datorkort) ==21 and handsumma(gekort) != 21:
            print(användarnamn, "datorn vann")

        elif handsumma(gekort) == 10 and handsumma(datorkort) != 10:
            print(användarnamn, "Du vann")

        elif handsumma(datorkort) == 10 and handsumma(gekort) != 10:
            print(användarnamn, "datorn vann")

        elif handsumma(gekort) > handsumma(datorkort):
            print(användarnamn, "Du vann")

        else:
            print(användarnamn, "Datorn vann")

        #Kallar på funktionen som tar bort korten från en lista 
        #och applicerar den på listorna gekort och datorkort
        pop(gekort, datorkort)



    elif börja == "Nej":
        
        #Avslutar programmet om man svarar nej på inputen börja
        break
    
    
    #Om 
    else:
        print("\nSkriv Ja eller Nej\n")