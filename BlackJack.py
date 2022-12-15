import random

#definerar funktionen för att ge nya kort till huset och handen
def nya(huset, gekort):

    for _ in range(3):

        nytt_kort = gekort.pop(-1)
        huset.append(nytt_kort)



#tar bort alla kort i nytt_kort tills det inte finns något kvar
def tabort(nytt_kort):
    while nytt_kort != 0:

        nytt_kort.pop(0)



#skapa kortleken
färger = [ "hjärter", "ruter", "spader", "klöver" ]

kort = [ "ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "knekt", "dam", "kung" ]

kortvärde = {"ess" : 11, "knekt" : 10, "dam" : 10, "kung" : 10}

gekort = []

huset = []

#Gör så att listan gekort får alla kort i en kortlek
for färg in färger:
    for k in kort:
        gekort.append(färg + " " + k)



#shuffla listan gekort
random.shuffle(gekort)



while True:
    #Input så man kan välja om man vill börja eller inte
    börja = input("vill du börja spela Black Jack? Ja eller Nej\n:").capitalize()
    

    if börja == "Ja":
        #ger ut korten till huset och handen
        nya(huset, gekort)

        print(huset)
        


    elif börja == "Nej":

        break
    else:
        print("\nSkriv Ja eller nej\n")