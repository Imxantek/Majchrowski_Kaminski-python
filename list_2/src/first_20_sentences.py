import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
def first_20_sentences():
    count=0
    sentence=""
    inWord=False
    for line in sys.stdin:
        if count>=20:
            continue

        if line.strip()=="":
            if sentence.strip()!="":
                count+=1
                print(sentence.strip())

            sentence=""
            inWord=False
            continue

        for char in line:
            if count>=20:
                break

            if char=="\n":
                sentence+=' '
            else:
                sentence+=char
            if char.isalpha():
                if not inWord:
                    inWord=True
            else:
                if inWord:
                    inWord=False

                if char in ".?!":
                    if sentence.strip()!="":
                        count+=1
                        print(sentence.strip())

                    sentence=""
                    inWord=False

if __name__ == "__main__":
    first_20_sentences()