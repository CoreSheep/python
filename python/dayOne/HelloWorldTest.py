while True:
    option = input("How to print 'hello world'?\n"
               "input  0: one line\n" 
               "input >0: two character at one line\n"
               "input <0: vertical\n")
    if(eval(option) == 0):
        print("Hello World")
    elif(eval(option) > 0):
        print("He")
        print("ll")
        print("o ")
        print("Wo")
        print("rl")
        print('d')
    else:
        print('H'+"\ne"+"\nl"+"\nl"+"\no"+"\n"+"\nW"+"\no"+"\nr"+"\nl"+"\nd\n")