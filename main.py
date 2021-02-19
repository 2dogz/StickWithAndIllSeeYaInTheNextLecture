from main_helpers import fLoop, validatePath
from write_text import image_writer
import os.path

def main():
    #USER PROMPT AT START
    pawprint = input("Enter Your PawPrint\n")
    #pawprint = "KW2M4"
    projectName = input("Enter Project Name\n")
    #projectName = "ProjectsS21"
    inputPath = validatePath("Enter the directory where the images currently are\n");
    #inputPath = "C:/Users/Kyle/Pictures/Screenshots" # default location for win + print screen screenshots
    outputPath = validatePath("Enter the directory where you would like images to be saved\n")
    #outputPath = "C:/Users/Kyle/Desktop"

    count = 0
    folderData = fLoop(inputPath)
    for file in folderData:
        if file.endswith('.png'):
            count += 1
            print("{} {} ".format(file, count))
            image_writer("{}/{}".format(inputPath,file), pawprint,"{}/{}{}Screenshot{}automated.png".format(outputPath, pawprint, projectName, count))

if __name__ == '__main__':
    main()
