'''
    class people
'''

class People():
    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return self.name + " lives in " + self.city

    def moveto(self, newcity):
        return self.name + " moved to " + self.city

    def __lt__(self, other):
        return self.city > other.city

    def __del__(self):
        print("Instance " + self.name + " has been released.")


p1 = People("David", "LA")
p2 = People("Marshall", "Paris")
p3 = People("SheepCore", "Shengyang")
p4 = People("Lopez", "Kabul")

ls = [p1, p2, p3, p4]
# ls.sort()
print(ls)
