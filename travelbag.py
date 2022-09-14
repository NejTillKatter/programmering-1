travelbag = ["tandborste", "kläder", "legitimation", "kaka"]

while True:

   menyval = input("\n1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program\n")

   if menyval == "1":
       print(*travelbag, sep=", ", ) 

   elif menyval == "2":
       more = input("väljett föremål att lägga till väskan")
       travelbag.append(more)

   elif menyval == "3":
     less = input("välj ett föremål att ta bort")
     travelbag.remove(less)

   elif menyval == "4":
       break