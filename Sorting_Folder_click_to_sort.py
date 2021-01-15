'''
This project is for those people who have so many files in a folder but not sorted in a proper manner.
This python project is created by using the os module  and separate file format by using the def functions

By simply clicking on the python application the folder sorted properly by making new folders separately for formatted files 
like: FOLDER Images for .jpg .jpeg .png etc
       FOLDER Video for .mp4 .gif .webm etc
is takes negligible time to sort.
For download python file visit :

'''


# Created By : Ayush Shete

import os
import pyttsx3
speaker = pyttsx3.init()
voices = speaker.getProperty('voices')
speaker.setProperty('voice',voices[1].id)


def create_folder(foldername):
    # if not os.path.exists(folder):
    #     os.makedirs(folder)
    # OR

    if os.path.exists(foldername):
        pass
    else:
        os.makedirs(foldername)


def move(folderName, files):
    for file in files:
        print(f"file {files} succesfully moved to {folderName}")
        os.replace(file, f"{folderName}/{file}")
        


if __name__ == "__main__":
    files = os.listdir()
    files.remove("Sorting_Folder_click_to_sort.py")

    create_folder("Audios")
    create_folder("Documents")
    create_folder("Images")
    create_folder("Microsoft_office")
    create_folder("Others")
    create_folder("Videos")

    audioExists = [".mp3", '.m4a', '.flac', '.wav', '.wma', '.aac', '.aiff', '.alac', '.dsd', '.mp1', '.mp2', '.ac3',
                   '.aiff', '.3ga', '.ogg', '.amr', '.pcm', '.mov']
    audioExists = [file for file in files if os.path.splitext(file)[
        1].lower() in audioExists]

    docExists = [".txt", '.psd', '.html', '.css', '.js', '.pdf', '.ai', '.id', '.php', '.py', '.tiff', '.odt', '.ods', '.c',
                 '.cpp', '.xmls', '.dj', '.java', '.xhtml', '.php', '.php4', '.php3', '.phtml', '.rb', '.xml', '.svg', '.cson', 'pub']
    docExists = [file for file in files if os.path.splitext(file)[
        1].lower() in docExists]

    imgExists = [".jpg", '.jpeg', '.png', '.bmp', '.ppm',
                 '.pgm', '.pbm', '.hdr', '.bat', '.paint', '.wmf']
    imgExists = [file for file in files if os.path.splitext(file)[
        1].lower() in imgExists]

    MSExists = [".doc", '.dot', '.wbk', '.docx', '.dotx', '.xls', '.xlsx', '.xlt', '.xlm', '.xltm', '.ppt', '.pot', '.pps', '.pptx',
                '.pptm', '.potx', '.potm', '.ppsx', '.sldx', '.sldm', '.one', '.accdb', '.accde', '.accdt', '.acdr', '.pub', '.xps']
    MSExists = [file for file in files if os.path.splitext(file)[
        1].lower() in MSExists]


    videoExists = ['.mp4', '.wmv', '.avchd', '.f4v', '.webm', '.mpg', '.mpeg', '.mpv', '.mp4', '.m4v', '.avi', '.gif', '.flv',
                   '.mkv', '.gifv', '.3gp', '.3g2', '.nsv', '.f4a', '.f4b', '.flv']
    videoExists = [file for file in files if os.path.splitext(file)[
        1].lower() in videoExists]

    othersExists = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in audioExists) and (ext not in docExists) and (ext not in imgExists) and (ext not in MSExists) and (ext not in videoExists) and os.path.isfile(file):
            othersExists.append(file)

    move("Audios", audioExists)
    move("Documents", docExists)
    move("Images", imgExists)
    move("Microsoft_office", MSExists)
    move("Videos", videoExists)
    move("Others", othersExists)
    print("◎◎◎◎  Succesfully file moved  ◎◎◎◎")
    exit()
