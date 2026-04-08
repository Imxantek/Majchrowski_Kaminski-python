import os
import json
from datetime import datetime

def get_target_directory():

    target_dir = os.environ.get("CONVERTED_DIR")
    if not target_dir:
        target_dir = os.path.join(os.getcwd(), "converted")
    
    os.makedirs(target_dir, exist_ok=True)
    return target_dir

def find_media_files(directory : str):

    allowed_extensions = {".mp3", ".mp4", ".avi", ".wav", ".mkv", ".webm", ".ogg"}
    media_files = []
    
    if not os.path.isdir(directory):
        return media_files
    
    for file in os.listdir(directory):
        # splittext dzieli mi po kropce
        ext = os.path.splitext(file)[1].lower()
        if ext in allowed_extensions:
            media_files.append(os.path.join(directory, file))
            
    return media_files

def generate_timestamped_filename(original_path, target_format):

    # Format daty 20250324153022
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # basename odcina ścieżkę do pliku i zostawia sama nazwe
    base_name = os.path.splitext(os.path.basename(original_path))[0]
    
    if not target_format.startswith("."):
        target_format = "." + target_format
        
    return f"{timestamp}-{base_name}{target_format}"

def log_history(target_dir, original_path, output_format, output_path):
    history_file = os.path.join(target_dir, "history.json")
    
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "original_path": original_path,
        "output_format": output_format.replace(".", ""), # bez kropki, czysty format
        "output_path": output_path
    }
    
    # odczytywanie pliku przed dodawaniem
    history = []
    if os.path.exists(history_file):
        try:
            with open(history_file, 'r', encoding='utf-8') as file:
                history = json.load(file)
        except json.JSONDecodeError:
            pass
            
    history.append(log_entry)
    
    with open(history_file, 'w', encoding='utf-8') as file:
        json.dump(history, file, indent=4)