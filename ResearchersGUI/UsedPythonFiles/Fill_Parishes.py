import csv
import os
import re

with open("Parishes.csv", 'r') as csvfile:
        encounter_reader = csv.reader(csvfile)
        parish_list = []
        for my_list in encounter_reader:
            parish_list += [my_list]


with open("Cleaned_Names.csv", 'r') as csvfile:
        encounter_reader = csv.reader(csvfile)
        name_list = []
        for my_list in encounter_reader:
            name_list += my_list

name_list = name_list[1:]

def touch(path, i):
    sections = ["Name of Parish"]
    sections_nospace = ["NameOfParish"]
    orig_filename = path.strip()
    for index in range(len(sections)):
        filename = orig_filename + ".txt"
        filename = filename.replace("/", "")
        filename = filename.replace("\\", "")
        filename = filename.replace(":", "")
        filename = filename.replace("*", "")
        filename = filename.replace("?", "")
        filename = filename.replace("<", "")
        filename = filename.replace(">", "")
        filename = filename.replace("|", "")
        filename = filename.replace('"', "")
        filename = filename.replace("'", "")

        newpath = 'Mill_Files\\'
        newpath = os.path.join('Mill_Files', sections_nospace[index])
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        filename = "Mill_Files/" + sections_nospace[index] + "/" + filename
        try:
            with open(filename, 'w') as mytxtfile:
                row = parish_list[i+1][1]
                mytxtfile.write(row)
        except FileExistsError:
        	pass


index = 0
for value in name_list:
	touch(value, index)
	index += 1

