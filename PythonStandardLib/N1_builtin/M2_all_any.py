'''
判断 all(iteralble) 中iterable有无空元素
'''

me = ("SheepCore", 21, "male", "20164586")
profile = list(me)
profile[-1] = None

print(all(profile))
print(any(profile))