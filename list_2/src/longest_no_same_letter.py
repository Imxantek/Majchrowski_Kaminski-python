import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
def longest_no_same_letter():
    max_length=-1
    previous=''
    current=''
    sentence=""
    longestSentence=""
    check=False
    inWord=False
    for line in sys.stdin:
        if line.strip()=="":
            if max_length<len(sentence) and not check:
                max_length=len(sentence)
                longestSentence=sentence
            previous=''
            current=''
            sentence=""
            check=False
            inWord=False
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
                        if max_length<len(sentence):
                            max_length=len(sentence)
                            longestSentence=sentence
                        # print(sentence)

                    previous=''
                    current=''
                    sentence=""
                    check=False
    print("\nLongest sentence with no 2 neighboring words having the same starting letter:\n")
    print(f"\"{longestSentence}\"")
if __name__ == "__main__":
    longest_no_same_letter()