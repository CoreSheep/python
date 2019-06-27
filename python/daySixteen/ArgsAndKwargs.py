"""
    using **args and **kwargs in python function definition
"""


def args_test(Id, *args):
    print("Student Id: %d" % Id)
    print("profile:")
    Index = 1
    for arg in args:
        print("info{}: {}".format(Index, arg))
        Index += 1
    print()


def kwargs_test(Id, **kwargs):
    print("the first param is: ", Id)
    for key in kwargs:
        print("%s: %s" % (key, kwargs[key]))


if __name__ == "__main__":
    # both list and tuple are fine
    profile = ('sheepcore', 'class 1606', 'male', 'handsome')
    args_test(20164586, *profile)
    args_test(20161111, 'marshall', 'class 1508', 'male')

    profile2 = {'name': 'Anna Hathaway', 'class': 'class 1709', 'gender':
        'female'}
    kwargs_test(Id=20184434, **profile2)



