import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def find_longest_sentence():

    longestSentence = ""
    maxSize = 0
    currentSentence = ""

    for line in sys.stdin:
        for char in line:

            currentSentence+=char

            if char in ".?!":
                if len(currentSentence) > maxSize:
                    longestSentence = currentSentence
                    maxSize = len(currentSentence)
                currentSentence = ""
                
    return longestSentence

if __name__=="__main__":
    print(f"The longest sentence in the text: {find_longest_sentence()}")
                
