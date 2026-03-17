import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def count_letters():
    numberOfLetters = 0

    for line in sys.stdin:

        cleanedLine = line.strip()

        for char in cleanedLine:
            if not char.isspace():
                numberOfLetters+=1
                
    return numberOfLetters

if __name__=="__main__":
    print(f"Number of letters in text: {count_letters()}")