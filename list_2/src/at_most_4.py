import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
def at_most_4():
    count=0
    inWord=False
    sentence=""
    for line in sys.stdin:
        if line.strip() == "":
            if 0 < count <= 4:
                print(sentence)
            count=0
            inWord=False
            sentence=""
            continue

        for char in line:
            if char=="\n":
                sentence+=" "
            else:
                sentence+=char

            if char.isalpha():
                if not inWord:
                    count += 1
                    inWord = True
            else:
                if inWord:
                    inWord = False
                if char in ".?!":
                    if 0 < count <= 4:
                        print(sentence)
                    sentence=""
                    count=0
    if 0 < count <= 4:
        print(sentence.strip())
if __name__ == "__main__":
    at_most_4()
