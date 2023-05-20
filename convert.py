# PNG to WEBP converter
import glob
import os
from pathlib import Path
from PIL import Image
import sys

def printHelp():
    print("-f\t convert one file in the given folder")
    print("-p\t convert all files in the given folder but not in the subfolders")
    print("-pr\t convert all files in the given folder and all subfolders recursively")
    print("-h\t print this help")
    
def convert_to_webp(source):
    destination = source.with_suffix(".webp")
    image = Image.open(source)  # Open image
    image.save(destination, format="webp")  # Convert image to webp
    return destination

def fileHandling(filename):
    folder, file = os.path.split(filename)
    extension = os.path.splitext(file)
    if os.path.exists(filename):
        if extension[-1] != ".png":
            print("Please add only png file")
        else:
            paths = Path(folder).glob(file)
            for path in paths:
                webp_path = convert_to_webp(path)
                print("Image converted to: " + str(webp_path))
    else:
        print("This path does not exist")
    
def folderHandling(folder, recursive):
    if os.path.isdir(folder):
        print("Convert all PNG file in " + folder + " ...")
        if recursive == "True":
            paths = Path(folder).glob("**/*.png")
        else:
            paths = Path(folder).glob("*.png")
        for path in paths:
            webp_path = convert_to_webp(path)
            print("Image converted to: " + str(webp_path))
    else:
        print("This folder does not exist")
        
def main():
    args = sys.argv
    try:
        if args[1] == "-f":
            try:
                fileHandling(args[2])
            except Exception as e:
                print("Please add a file to convert!")
        elif args[1] == "-p":
            try:
                folderHandling(args[2], "False")
            except Exception as e:
                print("Please add a folder to convert the files!")
        elif args[1] == "-pr":
            try:
                folderHandling(args[2], "True")
            except Exception as e:
                print("Please add a folder to convert the files!")
        elif args[1] == "-h":
            print("This program convert PNG files to WEBP format. You can use the next argumentums")
            print("-" * 60 + "\n")
            printHelp()
            print("\n")
            print("-" * 60 + "\n")
        else:
            print("Please use the next args for")
            printHelp()
    except IndexError:
            print("You did not specify what you want to do!\n")
            print("Please use the next args for")
            printHelp()
    except Exception as e:
        print("Error occured: " + type(e).__name__)

main()