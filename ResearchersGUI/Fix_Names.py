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
	sections = ["Extant or Ruin", "Founding Date", "Chronology", "Additional Information", "Enslaved Peoples"]
	orig_filename = path.strip()
	for value in sections:
		filename = value + "_" + orig_filename + ".txt"
		filename = filename.replace("/", "")
		filename = "Mill_Files/" + filename
		try:
			open(filename, 'x').close()
		except FileExistsError:
			pass

for value in name_list:
	touch(value)