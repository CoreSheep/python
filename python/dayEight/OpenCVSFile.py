'''
    open cvs(comma-separated values) file
    two dimension table
'''

def openCVSFile(filename, mode):
    f = open(filename, mode)
    datals = []
    for line in f:
        line = line.replace('\n', '')
        datals.append(line.split(','))
    print(datals)
    f.close()
    return datals


data = [['end game', 'Taylor Swift'], ['pray', 'Sam Smith']]
f = open("qqmusic.csv", 'a')
for line in data:
    f.write(",".join(line) + "\n")
f.close()




