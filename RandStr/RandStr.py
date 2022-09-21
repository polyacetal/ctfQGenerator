import random
import string
import sys

def Main():
    args = sys.argv
    del args[0]
    ops = ["-f", "-k", "-x", "-y", "-h"]

    if "-h" in args:
        HelpPrint()
    else:
        arg = {}
        for op in ops:
            if op in args:
                idx = args.index(op)
                data = args[idx + 1]
                arg[op] = data

        filename, key, xMax, yMax = DecisionVar(arg)
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

def HelpPrint():
    print("RandStr.pyの使い方")
    print("-h: helpコマンド")
    print("    これが含まれていると他に書かれていてもhelpを表示する\n")
    print("-f: 出力するファイル名を指定する")
    print("    デフォルトは\"question.txt\"です\n")
    print("-k: 文字列に隠す文字列を指定する")
    print("    デフォルトは\"CTFKIT{well done}\"です\n")
    print("-x: 横幅の最大字数を指定する")
    print("    デフォルトは1000文字です\n")
    print("-y: 横幅の最大字数を指定する")
    print("    少なくとも隠す文字の文字数以上を指定してください")
    print("    デフォルトは1000文字です\n")

def DecisionVar(arg):
    if "-f" in arg.keys():
        filename = arg["-f"]
    else:
        filename = "question.txt"

    if "-k" in arg.keys():
        key = arg["-k"]
    else:
        key = "CTFKIT{well done}"

    if "-x" in arg.keys():
        xMax = arg["-x"]
    else:
        xMax = 1000

    if "-y" in arg.keys():
        yMax = arg["-y"]
    else:
        yMax = 1000

    return filename, key, xMax, yMax

if __name__ == "__main__":
    Main()
