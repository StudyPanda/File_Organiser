import os
import shutil
import logging


# Configure logging
logging.basicConfig(filename='file_cleaner.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def move_file(source_path, target_path, source, target):
    file =  os.path.join(source_path, source)
    directory = os.path.join(target_path, target)
    #check if folder exists
    if not os.path.exists(directory):
        os.mkdir(directory)
        logging.info("Created folder {} at {}".format(target, target_path))

    shutil.move(file,directory)
    logging.info("Moved {} to {}".format(source, target))

def sort_files(dl, dt):
    #move all files from downloads to appropriate location desktop
    os.chdir(dl)

    media_extensions = {
        "Audio": [
            "mp3", "wav", "aac", "flac", "ogg", "wma", "m4a", "aiff"
        ],
        "Videos": [
            "mp4", "mkv", "flv", "avi", "mov", "wmv", "mpg", "mpeg", "m4v", "h264"
        ],
        "Images": [
            "jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg", "psd", "raw"
        ],
        "Documents": [
            "pdf", "doc", "docx", "ppt", "pptx", "xls", "xlsx", "txt", "odt"
        ]
    }

    #list of files
    files = os.listdir()
    
    #iterate through each file
    for file in files:
        #get the file type to know where to sort
        try:
            file_type = file.split(".")[-1]
        except ValueError as e:
            logging.info("{}: {}".format(e, file))

        misc = True

        for media in media_extensions.keys():
            if file_type in media_extensions[media]:
                move_file(dl, dt, file, media)
                misc = False
            
        if misc:
            move_file(dl, dt, file, "Misc")
            



#def clean_old():




    


def main():
    desk_path = os.path.expanduser("~/Desktop")
    down_path = os.path.expanduser("~/Downloads")
    sort_files(down_path, desk_path)
    



if __name__  == "__main__":
    main()
