# text process bar

import time
print("Start".center(20, '-'))
for i in range(101):
    star = '*' * i
    bar = '-' * (100 - i)
    print("\r{: ^3} % [{:}->{:}]".format(i, star, bar), end='')
    time.sleep(0.1)
print("\n{:-^20}".format("end"))

