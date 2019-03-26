def caught_speeding(speed, is_birthday):
    if is_birthday == True and speed <= 65:
        return("0")

    elif is_birthday == True and speed >=86:
        return("2")

    elif speed <= 60:
        return("0")

    elif speed >=81:
        return("2")

    else:
        return("1")

print(caught_speeding(60, False)) #→ 0
print(caught_speeding(65, False)) #→ 1
print(caught_speeding(65, True)) #→ 0
