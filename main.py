while True:
    name=input("Välkommen till frågesporten om hockey, vad heter du?")
    print("hej", name)
    points=1
    score=0

    #fråga 1

    print("Fråga 1")
    print("A. Colorado Avelanche")
    print("B. Chicago Black Hawks")
    print("C Tampa Bay Lightning")
    fråga1=input("Vilka vann stanley cup säsongen 2021/22?")
    if fråga1=="A":
        score+=points
        print("rätt") 

    else:
        print("fel")
        points-=0

    #fråga 2

    print("Fråga 2")
    print("A. 1")
    print("B. 2")
    print("C. 3")
    fråga2=input("Hur många målvakter brukar byta om i varje lag per match?")
    if fråga2=="B":
        score+=points
        print("rätt") 

    else:
        print("fel")
        points-=0

    #fråga 3

    print("Fråga 3")
    print("A. Henrik lundqvist")
    print("B. Igor Seshterkin")
    print("C. Jakob Markström")
    fråga3=input("Vem vann vezina trophy säsongen 2021/22?")
    if fråga3=="B":
        score+=points
        print("rätt") 

    else:
        print("fel")
        points-=0

    #fråga 4

    print("Fråga 4")
    print("A. 18")
    print("B. 21")
    print("C. 17")
    fråga4=input("Hur gammal är måste man vara för att bli draftad till NHL?")
    if fråga4=="A":
        score+=points
        print("rätt") 

    else:
        print("fel")
        points-=0

    print (name, "du fick", score, "/4 BRA JOBBAT!")

    if score != 4:
        
        om=input("vill du börja om quizen? ja eller nej")

    if om !="ja":
        break