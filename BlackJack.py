import random
#skapa kortleken
färger = [ "hjärter", "ruter", "spader", "klöver" ]

kort = [ "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13" ]

gekort = []

for färg in färger:
    for k in kort:
        gekort.append(färg + " " + k)
print (gekort[])

 

while True:
    börja = input("vill du börja spela Black? Ja eller Nej\n:").capitalize()
    

    if börja == "Ja":
        #ger ut korten
        pass
        



    if börja == "Nej":
        break
    else:
        print("\nSkriv Ja eller nej\n")