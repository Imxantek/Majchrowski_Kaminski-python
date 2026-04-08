import sys
import os
import subprocess
import utils # Importujemy Twój nowy moduł!

def convert_media():

    input_dir = sys.argv[1]
    target_format = sys.argv[2]

    target_dir = utils.get_target_directory()
    media_files = utils.find_media_files(input_dir)

    if not media_files:
        print(f"No media files in directory: {input_dir}")
        return

    print(f"target directory: {target_dir}")
    
    for file_path in media_files:
        new_filename = utils.generate_timestamped_filename(file_path, target_format)
        output_path = os.path.join(target_dir, new_filename)
        
        print(f"Converting: {os.path.basename(file_path)} -> {new_filename}")
        
        # '-y' wymusza nadpisanie pliku
        # -i Informuje FFmpega, że kolejny parametr to fle
        # ffmpeg odbiera to przez "main(int argc, char **argv)"
        
        try:
            result = subprocess.run(
                ["ffmpeg", "-y", "-i", file_path, output_path],
                capture_output=True,
                text=True
            )
            
            if result.returncode == 0:
                print("Succes!")
                utils.log_history(target_dir, file_path, target_format, output_path)
            else:
                print(f"Conversion ERROR!")
                print(result.stderr) 
                
        except FileNotFoundError:
            print("File not found: ffmpeg.exe")
            print("Add it to environment PATH")
            break

if __name__ == "__main__":
    if len(sys.argv) == 3:
        convert_media()
    else:
        print("Użycie: python mediaconvert.py <katalog_z_plikami> <format_docelowy>")
        print("Przykład: python mediaconvert.py moje_audio wav")
