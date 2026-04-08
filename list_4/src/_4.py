import os
import subprocess
import json
import sys

def capture_json_output_from_files(catalogue : str):

    dir = os.listdir(catalogue)
    raw_json_list = []
    script_path = os.path.join(os.path.dirname(__file__), "Analyze_file.py")

    for file in dir:
        full_filepath = os.path.join(catalogue, file)

        result = subprocess.run(
            ["python", script_path],
            input=full_filepath,
            text=True,
            capture_output=True,
            encoding='utf-8'
        )

        raw_json_list.append(result.stdout)
    
    return raw_json_list

def parse_jsons_to_dicts(raw_jsons_list: list):

    dict_list = []

    for raw_json in raw_jsons_list:
        try:
            dict_list.append(json.loads(raw_json))
        except json.JSONDecodeError:
            print(f"JSON Error: wrong decoding")
            
    return dict_list

def analyze_catalogue(directory_path : str):

    raw_json_data = capture_json_output_from_files(directory_path)
    list_of_file_stats = parse_jsons_to_dicts(raw_json_data)

    files_read = 0
    total_chars = 0
    total_words = 0
    total_rows = 0
    
    best_word = "None"
    best_word_count = 0
    best_char = "None"
    best_char_count = 0

    for file_stats in list_of_file_stats:
        if "error" in file_stats:
            continue
            
        files_read += 1
        total_chars += file_stats["number_of_chars"]
        total_words += file_stats["number_of_words"]
        total_rows += file_stats["number_of_rows"]
        
        if file_stats["most_common_word_count"] > best_word_count:
            best_word_count = file_stats["most_common_word_count"]
            best_word = file_stats["most_common_word"]
            
        if file_stats["most_common_char_count"] > best_char_count:
            best_char_count = file_stats["most_common_char_count"]
            best_char = file_stats["most_common_char"]


    return {
        "files_read": files_read,
        "total_chars": total_chars,
        "total_words": total_words,
        "total_rows": total_rows,
        "most_common_char": best_char,
        "most_common_word": best_word
    }
    
def print_global_report(stats: dict):
    # A separate function strictly responsible for data presentation
    if not stats:
        print("No data to display.")
        return

    print(f" Files read: {stats['files_read']}")
    print(f" Total characters: {stats['total_chars']}")
    print(f" Total words: {stats['total_words']}")
    print(f" Total rows: {stats['total_rows']}")
    print(f" Most common character in single file: '{stats['most_common_char']}'")
    print(f" Most common word in single file: '{stats['most_common_word']}'")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        catalogue = sys.argv[1]
        result = analyze_catalogue(catalogue)
        print_global_report(result)
    else:
        print("Usage: python _4.py <path_to_catalogue>")