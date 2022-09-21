import random
import string

def Main():
    filename = "question.txt"
    key = "CTFKIT{well done}"
    xMax = 1000
    yMax = 1000
    Process(filename, xMax, yMax, key)

def Process(filename, xMax, yMax, key):
    f = open(filename, 'w')
    datalst = []
    x = random.randint(1, xMax)
    y = random.randint(1, yMax - len(key))

    for i in range(1000):
        if i == x:
            datalst.append(RandStr(y) + key + RandStr(1000 - y - len(key)) + '\n')
        datalst.append(RandStr(1000) + '\n')

    f.writelines(datalst)
    f.close()

def RandStr(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
    return ''.join(randlst)

if __name__ == "__main__":
    Main()
