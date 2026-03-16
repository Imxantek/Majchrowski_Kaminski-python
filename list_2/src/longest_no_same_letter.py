import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
def longest_no_same_letter():
    max=-1
    inWord=False
    previous=''
    current=''
    check=False
    sentence=""
    longestSentence=""
    for line in sys.stdin:
        if line.strip()=="":
            previous=''
            inWord=False
            sentence=""
            current=''
            continue
        for char in line:

            if char == '\n':
                sentence += ' '
            else:
                sentence += char

            if char.isalpha():
                if not inWord:
                    inWord=True
                    current=char.lower()
                    if previous==current:
                        check=True
                else:
                    inWord=True
            else:
                if inWord:
                    inWord=False
                    previous=current

                if char in ".!?":
                    if not check:
                        if max<len(sentence):
                            max=len(sentence)
                            longestSentence=sentence
                        # print(sentence)

                    previous=''
                    sentence=""
                    current=''
                    check=False
    print("\nLongest sentence with no 2 neighboring words having the same starting letter:\n")
    print(f"\"{longestSentence}\"")
if __name__ == "__main__":
    longest_no_same_letter()