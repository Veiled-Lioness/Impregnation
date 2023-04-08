import math
import random

##Inputs
x = "y"
while x != "n":
    print("Average Fertility (chance of impregnation): 20, Average Ova (the number of offspring per pregnancy): 1,")
    p1_Fertility = float(input("'Mother's' Fertility (0-100%): ", )) / 100
    p1_Ova = float(input("'Mother's' Ova: ", ))
    p2_Fertility = float(input("2nd Parent Fertility (0-100%): ", )) / 100
    p2_Ova = float(input("2nd Parent Ova: ", ))
    Loads = float(input("Loads: ", ))
    if p1_Fertility == "auto": p1_Fertility = .2 ** (1 / p1_Ova)
    if p2_Fertility == "auto": p2_Fertility = .2 ** (1 / p2_Ova)
    Preg = int(input("'Mother' Currently Carrying: ", ))
    if Preg != 0: p1_Fertility = p1_Fertility ** Preg
        
    Ova = (p1_Ova + p2_Ova) / 2
    Fertility = ((p1_Fertility + p2_Fertility) / 2) ** (1 / Loads)

    ##Impregnation:
    Impregnation_Roll = random.random()
    print("Roll: ", Impregnation_Roll)
    if Impregnation_Roll <= Fertility:
        b = ((math.log(Impregnation_Roll) / math.log(Fertility)) * -1) + 1 + Ova
        if random.randint(0, 1) == 0 or b <= 0:
            b = (math.log(Impregnation_Roll) / math.log(Fertility)) - 1 + Ova
    else:
        b = 0
    b = round(b)

    print(b)

    x = input("Again? (y/n): ", )
    

