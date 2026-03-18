import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def print_found_sentences(foundSentences):
    for sentence in foundSentences:
        print(sentence)

def find_questions_and_exclamation():

    foundSentences = []
    currentSentence = ""

    for line in sys.stdin:

        for char in line:

            currentSentence += char

            if char in "?!":
                foundSentences.append(currentSentence.strip())
                currentSentence = ""
            elif char == ".":
                currentSentence = ""
    return foundSentences

if __name__=="__main__":
    print_found_sentences(find_questions_and_exclamation())