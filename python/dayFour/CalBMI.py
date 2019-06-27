'''
计算 BMI： Body Mass Index = weight / height**2
'''

try:
    weight, height = eval(input("enter your height(m) and weight(kg)[eg: 1.75, "
                            "74]: "))
except NameError or SyntaxError or ValueError:
    print("Please check you input format. ^_^")
else:
    bmi = weight / height**2
    who, nat = "", ""
    if bmi < 18.5:
        who, nat = "slim", "slim"
    elif 18.5 <= bmi < 24:
        who, nat = "normal", "normal"
    elif 24 <=bmi < 25:
        who, nat = "normal", "little fat"
    elif 25 <= bmi <28:
        who, nat = "little fat", "little fat"
    elif 28 <= bmi < 30:
        who, nat = "little fat", "fat"
    else:
        who, nat = "fat", "fat"
    print("Your BMI: {:.2f}".format(bmi))
    print("international standard: {}, domestic standard: {}".format(who, nat))

