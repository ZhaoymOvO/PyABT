#!/bin/env python3

import os
import re
import sys

_helpmsg = """
PyABT, a Python audio batch transcoder depends on SoX
Get SoX: https://sourceforge.net/projects/sox/

------------------------------------------------------

Usage: 

    Interactive command line:
        Just run main.py, the script will ask you all the questions in need
        
    ====================--------------------
    
    main.py [source path] [source format] [target path] [target format]
    
        source path: the path to the file you want to convert
        
        source format: the extension name for the source file's format
            tips: this script passes in the source format parameter
                  to determine what file extension needs to be converted.
                  
        target path: the path to output files
            tips: please create this path before running the script
            
        target format: the target format's stander extension name
            tips: SoX use the extension name to determine the format
        
    ====================--------------------

    main.py [-h|--help]
        Print this help massage
"""

has_sox = False
_path = os.getenv("PATH").split(":")
for i in _path:
    try:
        if "sox" in os.listdir(i):
            has_sox = True
            break
    except FileNotFoundError:
        continue

argv = sys.argv[1:]

if "-h" in argv or "--help" in argv:
    print(_helpmsg)
    exit()

if not has_sox:
    print("This script needs <SoX> to run")
    print("For get <SoX>, visit: https://sourceforge.net/projects/sox/")
    exit(1)

if len(argv) == 4:
    source_path = argv[0]
    source_format = argv[1]
    target_path = argv[2]
    target_format = argv[3]
elif len(argv) != 4 and argv:
    print("Incorrect input parameters")
    print("Use <main.py -h> to see help")
    exit(1)
else:
    source_path = input("Source path: ")
    source_format = input("Source format (extension name): ")
    target_path = input("Target/Output path: ")
    target_format = input("Target format(extension name): ")

source_file_list = []
for i in os.listdir(source_path):
    if i.endswith(f".{source_format}"):
        source_file_list.append(i)

target_file_list = [
    re.findall(r"(.+)\..+?", i)[0] + "." + target_format
    for i in source_file_list
]

for i in range(len(source_file_list)):
    print(
        f" [{i + 1}/{len(source_file_list)}]\tConverting '{source_file_list[i]}' to {target_format}"
    )
    if os.name == "nt":
        os.system(
            f"sox '{source_path}\\{source_file_list[i]}' '{target_path}\\{target_file_list[i]}'"
        )
    else:
        os.system(
            f"sox '{source_path}/{source_file_list[i]}' '{target_path}/{target_file_list[i]}'"
        )
