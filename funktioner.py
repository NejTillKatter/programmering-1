# Övning 3 går ut på att implementera så många av nedanstående funktioner som möjligt
# Ta bort pass och implementera funktionerna


def best(name):

    print(name, "är bäst")
    # TODO Skriv ut att namnet är bäst
    # Ex: "Katherine" in - skriver ut "Katherine är bäst"
    
name = input("Vad heter du?\n")
best(name)

def square(number):
    
    print(number**2)
    # TODO Returnera talet kvadrerat
    # Ex: 5 in - 25 ut

number = int(input("Välj ett nummer som ska kvadreras\n"))
square(number)

def sums(a, b):

    print(a + b)
     # TODO Returnera summan av a och b
    # Ex: 2, 6 in - 8 ut
    
sums(5, 18)

# Nu blir det lite svårare


def maximum(a, b, c):
    
    if a > b and a > c:
        print(a)

    elif b > c:
        print(b)

    else:
        print(c)
    # TODO Returnera det största av a,b,c
    # Ex: 3, 6, 12 in - 12 ut
    

maximum(5, 12, 8)


def palindrom(ord):
    
    bak = ord[::-1]

    if ord == bak:
        print(ord, "är ett palindrom")

    else:
        print(ord, "är inte ett palindrom")
    # TODO Returnera True om ord är ett palindrom
    # Ex: abba in - True ut
    # Palindrom är ett ord som stavas likadant baklänges och framlänges.
    
ord = input("Skriv ett ord för att se om det är ett palindrom\n")
palindrom(ord)

def prime(nr):

    
    # TODO Returnera True om nr är ett primtal, annars returnera false
    # Ex: 5 in - True ut


nr = input("skriv ett nummer för att kolla om det är ett primtal\n")
prime(nr)

