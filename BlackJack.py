import random
#skapa kortleken
färger = [ "hjärter", "ruter", "spader", "klöver" ]

kort = [ "ess", "2", "3", "4", "5", "6", "7", "8", "9", "10", "knekt", "dam", "kung" ]

kortvärde = {"ess" : 11, "knekt" : 10, "dam" : 10, "kung" : 10}

gekort = []

huset = []

#Gör så att listan gekort får 
for färg in färger:
    for k in kort:
        gekort.append(färg + " " + k)

#shuffla listan gekort

random.shuffle(gekort)

#definera och ge huset sina kort när koden kallas på
for _ in range(3):
    nytt_kort = gekort.pop(-1)
    huset.append(nytt_kort)




while True:
    #Input så man kan välja om man vill börja eller inte
    börja = input("vill du börja spela Black Jack? Ja eller Nej\n:").capitalize()
    

    if börja == "Ja":
        #ger ut korten
        pass
        
        



    if börja == "Nej":
        break
    else:
        print("\nSkriv Ja eller nej\n")