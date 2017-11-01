import csv
import os
import re

with open("Cleaned_Names.csv", 'r') as csvfile:
		encounter_reader = csv.reader(csvfile)
		name_list = []
		for my_list in encounter_reader:
			name_list += my_list

name_list = name_list[1:]

def touch(path):
	sections = ["Name of Mill", "Name of Parish", "Date of Establishment", "Longitude", "Latitude", "Extant or Ruin"]
	sections_nospace = ["DisplayName", "NameOfParish", "DateOfEstablishment", "Longitude", "Latitude", "ExtantOrRuin"]
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
			open(filename, 'x').close()
		except FileExistsError:
			pass

for value in name_list:
	touch(value)