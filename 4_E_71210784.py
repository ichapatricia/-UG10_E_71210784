blood = int(input("Masukan bilangan 1: "))
tears = int(input("Masukan bilangan 2:"))
sweat = int(input("Masukan bilangan 3:"))
if (blood<tears) and (blood<sweat):
    if (tears<sweat):
        print(blood, tears, sweat)
    else:
        print(blood, sweat, tears)
elif (tears<sweat) and (tears<blood):
    if (sweat<blood) : 
        print(tears, sweat, blood)
    else:
        print(tears, blood, sweat)
else:
    if (blood<tears):   
        print(sweat, blood, tears)
    else:
        print(sweat, tears, blood)    