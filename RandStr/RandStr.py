import random
import string

def Main():
    f = open('question.txt', 'w')
    datalst = []
    key = "CTFKIT{well done}"
    x = random.randint(1,1000)
    y = random.randint(1,1000 - len(key))

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
