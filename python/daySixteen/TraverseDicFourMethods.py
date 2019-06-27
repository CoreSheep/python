"""
    traverse dictionary in four methods
"""

# define dict
profile = dict()
profile['id'] = 20164586
profile['name'] = 'sheepcore'
profile['class'] = 'class 1606'
profile['gender'] = 'male'


# 1.traverse dict
for key in profile:
    print("{}: {}".format(key, profile[key]))
print()

# 2.traverse dict
for key in profile.keys():
    print("{}: {}".format(key, profile[key]))
print()

# 3.traverse dict with value
for Value in profile.values():
    print("%s" % Value)
print()

# 4.traverse dict with key, value
for key, Value in profile.items():
    print("{}: {}".format(key, Value))