def squirrel_play(temp, is_summer):
    if is_summer == True and (temp > 60 and temp < 100):
        return True

    elif temp > 60 and temp < 90:
        return True

    else:
        return("False")

print(squirrel_play(70, False)) #→ True
print(squirrel_play(95, False)) #→ False
print(squirrel_play(95, True)) #→ True