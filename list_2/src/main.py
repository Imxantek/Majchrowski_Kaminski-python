import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')

def remove_spaces(cleanedLine):
    result = ""
    last_char_was_space = False
    for char in cleanedLine:
        if char.isspace():
            if not last_char_was_space:
                result+=" "
                last_char_was_space = True
        else:
            result+=char
            last_char_was_space = False
    return result

def main():
    try:
        inPreamble=True
        emptyLines=0
        lineCounter=0
        cache=""
        for line in sys.stdin:
            lineCounter+=1

            if inPreamble:
                cache+=line
                if line.strip()=='':
                    emptyLines+=1
                else:
                    emptyLines=0
                if emptyLines>=2:
                    inPreamble=False
                    cache=""
                    continue
                if lineCounter==10:
                    print(cache)
                    cache=""
                    inPreamble=False
                    continue
                continue
            if "-----" in line:
                break

            cleanedLine=line.strip()

            if cleanedLine=="":
                print("")
            else:
                print(remove_spaces(cleanedLine))
    except (EOFError, KeyboardInterrupt, BrokenPipeError) as e:
        sys.exit(0)

if __name__ == "__main__":
    main()

