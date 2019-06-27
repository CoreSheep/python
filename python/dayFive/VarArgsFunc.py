"""
    变长参数

"""


def function(arg, *args, **kwargs):
    print(arg, args, kwargs)


function(6, 7, 8, 9, a=1, b=2, c=3)