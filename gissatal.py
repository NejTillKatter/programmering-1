import random

siffra = random.randint(1, 100)

while True:

    gissa = int(input("Gissa ett tal mellan 1-100 som datorn genererat.\n"))

    if gissa < siffra:
        print("\nTalet är högre\n")

    elif gissa > siffra:
        print("\nTalet är lägre\n")

    elif gissa == siffra:
        print("\nDu gissade rätt tal")
        break