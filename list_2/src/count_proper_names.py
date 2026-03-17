import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
def count_proper_names():
    totalCount = 0
    properCount = 0

    isFirst = True
    inWord = False
    isCapitalized = False
    containsProper = False
    hasContent=False

    for line in sys.stdin:
        if line.strip() == "":
            if hasContent:
                totalCount += 1
                if containsProper:
                    properCount += 1

            isFirst = True
            containsProper = False
            hasContent=False
            inWord = False
            continue

        for char in line:
            if char.isalpha():
                if not inWord:
                    inWord = True
                    hasContent = True
                    isCapitalized = char.isupper()

            else:
                if inWord:
                    inWord = False
                    if isCapitalized and not isFirst:
                        containsProper = True

                    isFirst = False

                if char in ".!?":
                    if hasContent:
                        totalCount += 1
                        if containsProper:
                            properCount += 1
                    isFirst = True
                    containsProper = False
                    hasContent = False

    if hasContent:
        totalCount += 1
        if containsProper:
            properCount += 1

    if totalCount == 0:
        return 0.0
    else:
        return (properCount / totalCount) * 100.0


if __name__ == "__main__":
    print(f"Percentage of sentences containing proper names {count_proper_names():.2f}%")
