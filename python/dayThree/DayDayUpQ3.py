'''
A work 5 days, rest 2 days ?%
B work 7 days 1%
'''

def dayUP(df):
    dayup = 1
    for i in range(365):
        if i % 7 in [6, 0]:  # on weekend
            dayup *= 1 - 0.01
        else:
            dayup *= 1 + df
    return dayup

dayfactor = 0.01
while dayUP(dayfactor) < 1.01 ** 365:
    dayfactor += 0.001
print(dayfactor)