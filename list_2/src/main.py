import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def main():
    text=""
    inPreamble=True
    emptyLines=0
    lineCounter=0

    for line in sys.stdin:
        lineCounter+=1

        if inPreamble:
            if line.strip()=='':
                emptyLines+=1
            else:
                emptyLines=0

            if emptyLines>=2 or lineCounter>=10:
                inPreamble=False
            continue

        if "-----" in line:
            break

        cleanedLine=line.strip()

        if cleanedLine=="":
            print("")
        else:
            normalizedLine=" ".join(cleanedLine.split())
            print(normalizedLine)

if __name__ == "__main__":
    main()

