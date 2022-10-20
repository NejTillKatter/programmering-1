# Travelbag
# Skelettkod till uppgiften

accounts = {"user" : "password"}
logged_in = False

while True:
    menyval = input(
    "1. Skapa konto\n"
    "2. Logga in\n"
    "3. Läs en rolig historia\n"
    "4. Logga ut\n"
    "5. Avsluta program\n")
    

    if menyval == "1":
        user = input("Välj användarnamn till kontot\n")
        password = input("Välj lösenord till kontot\n")

        # TODO Skapa ett konto genom att lägga till ett key-value par i accounts
        # username = key, password = value
        # Bonus: Kolla först så att användaren inte redan finns
        

    elif menyval == "2":
        log_user = input("Skriv ditt användarnamn\n")
        log_password = input("skriv ditt lösenord\n")
        if log_user == user and log_password == password:
            logged_in = True
            print("Du har loggat in\n")
        else:
            logged_in = False
            print("Fel användarnamn eller lösenord")


       
        # TODO Användaren ska få logga in med username och password
        # Ändra variabeln logged_in till True om de lyckas logga in
        # Bonus: Ge användaren ett visst antal försök att logga in
        

    elif menyval == "3":
        if logged_in == False:
            
        
        # TODO skriv ut en rolig historia, men bara om användaren är inloggad
        # Bonus: Skriv ut en tråkig historia om de inte är inloggade
        pass

    elif menyval == "4":
        # TODO Ändra variabeln logged_in till False
        # Bonus: Fråga om de är säkra först
        pass

    elif menyval == "5":
        break
