extreme_cold = False

print("******* Welcome to the Extreme Cold Alert Detector ***********")

temps = [int(s) for s in input("Enter the list of temperatures: ").split()]
wspeed = int(input("Enter the wind speed: "))

def windchill(temps, wspeed):
    global extreme_cold

    for i in range(len(temps)):
        temps[i] = 13.12 + 0.6215 * float(temps[i]) - 11.37 * float(wspeed) * 0.16 + 0.3965 * float(temps[i]) * float(wspeed) * 0.16

        if temps[i] < -30 and temps[i-1] < -30:
            extreme_cold = True

    if extreme_cold == True:
        print("EXTREME COLD ALERT!")

    else:
        print("Conditions are Normal")


windchill(temps, wspeed)


