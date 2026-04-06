import collections
import string
import json

def analyze_txt_file():
    
    filepath = input()

    number_of_chars = 0
    number_of_words = 0
    number_of_rows = 0

    word_counter = collections.Counter()
    char_counter = collections.Counter()

    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            
            for line in file:
                words_list = line.split()

                for word in words_list:
                    cleaned_word = word.upper().strip(string.punctuation)
                    word_counter[cleaned_word] +=1

                    for char in word:
                        char_counter[char] +=1

                number_of_chars += len(line)
                number_of_words += len(words_list)
                number_of_rows += 1
                
    except Exception as e:
        return {"error": str(e)}
    
    return {
        "filepath:": filepath,
        "number_of_chars": number_of_chars,
        "number_of_words": number_of_words,
        "number_of_rows": number_of_rows,
        "most_common_word": word_counter.most_common(1)[0][0],
        "most_common_word_count": word_counter.most_common(1)[0][1],
        "most_common_char": char_counter.most_common(1)[0][0],
        "most_common_char_count": char_counter.most_common(1)[0][1]
    }

def json_print(stats: dict):
    print(json.dumps(stats))

if __name__ == '__main__':
    stats = analyze_txt_file()
    json_print(stats)