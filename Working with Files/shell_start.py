import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")
    # make a backup copy by appending bak to the name
    dst = src + ".bak"

    # copy the permissions, modification times, and other info
    # shutil.copy(src, dst)
    # shutil.copystat(src, dst)

    # os.rename("textfile.txt", "newfile.txt")
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)
    # with is an object constructor
    with ZipFile("testzip.zip", "w") as newzip:
        newzip.write("textfile.txt")
        newzip.write("textfile.txt.bak")
