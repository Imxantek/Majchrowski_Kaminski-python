import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def find_first_sentence_with_two_commas():
    
    currentSentence = ""
    commaCount = 0

    for line in sys.stdin:
        for char in line:
            
            currentSentence += char

            if char == ",":
                commaCount += 1

            if char in ".?!":
                
                if commaCount >= 2:
                    
                    return currentSentence
                currentSentence = ""
                commaCount = 0
                
    return ""

if __name__=="__main__":
    print(f"First sentence with at least two commas: {find_first_sentence_with_two_commas()}")