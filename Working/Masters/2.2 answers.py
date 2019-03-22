def date_fashion(you, date):
    if(you >= 8 and date >= 8) or (you >= 8) or (date >= 8):
        print("2")
    elif(you <= 2 and date <= 2) or (you <= 2) or (date <= 2):
        print("0")
    else:
        print("1")

date_fashion(5, 10) #→ 2
date_fashion(5, 2) #→ 0
date_fashion(5, 5) #→ 1