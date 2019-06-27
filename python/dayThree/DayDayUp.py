# day day up
dayfactor = 0.005

def dayUpOrDown(factor):
    dayup = pow(1 + dayfactor, 365)
    daydown = pow(1 - dayfactor, 365)
    print("up: {:.2f}, down: {:.2f}".format(dayup, daydown))

dayUpOrDown(dayfactor)
dayfactor = 0.02
dayUpOrDown(dayfactor)

