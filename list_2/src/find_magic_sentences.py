import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def find_magic_sentences():
    
    currentSentence = ""
    currentWord = ""
    magicCount = 0

    for line in sys.stdin:
        for char in line:
            
            currentSentence += char

            if char.isalpha():
                currentWord += char.lower()
                
            else:
                if currentWord != "":
                    if currentWord == "i" or currentWord == "oraz" or currentWord == "ale" or currentWord == "że" or currentWord == "lub":
                        magicCount += 1
                        
                    currentWord = ""
                
                if char in ".?!":
                    if magicCount >= 2:
                        yield currentSentence.strip()
                        
                    currentSentence = ""
                    magicCount = 0

if __name__ == "__main__":
    for sentence in find_magic_sentences():
        print(sentence)