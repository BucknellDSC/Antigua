
# Antigua Researcher's GUI
# Author: Alexander Murph
# Last Edited: 9/30 by Murph
# Please run on Python 3

import tkinter as tk				# python 3
from tkinter import font  as tkfont # python 3
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
from subprocess import call
from txt_to_json import txt_to_json
from PIL import Image, ImageTk

#changes

# DATA SECTION
# SECTIONS is editable based on what data sections are wanted, but Fix_Names must then also be edited and run befor
# GUI will work.
# MILL_DATA is assumed to remain constant.
SECTIONS = ["Extant or Ruin", "Founding Date", "Chronology", "Additional Information", "Enslaved Peoples"]
SECTIONS_NOSPACE = ["ExtantOrRuin", "FoundingDate", "Chronology", "AdditionalInformation", "EnslavedPeoples"]

SECTIONS = ["Chronology", "Additional Information", "Enslaved Peoples"]
SECTIONS_NOSPACE = ["Chronology", "AdditionalInformation", "EnslavedPeoples"]
SUB_SECTIONS = ["Display Name", "Date of Establishment", "Longitude", "Latitude", "Extant or Ruin"]
SUB_SECTIONS_NOSPACE = ["DisplayName", "NameOfParish", "DateOfEstablishment", "Longitude", "Latitude", "ExtantOrRuin"]


MILL_DATA = ['Barnacle Point', 'Barnes Hill', "Blackman's/Mount Lucie", 'Carlisles', 'Date Hill', \
"Donovan's (Vaughans)", 'Fitches Creek', 'Giles Blizzard', "Gravenor's", 'Gunthorpes (ASF)', 'Hight Point', \
"Judge Blizzard's", "Lightfoot's/The Grove", 'Long Island', 'Millars', "Nibb's", \
"North Sound (Thomas's Hill/Col. Thomas North Sound Plantation", 'Paynters', 'Sherwoods/Lebanon', \
"Weir's (Ware's/Glanville's/Little Zoar)", "Will Blizzard's", 'Winthorpes', \
"Allen's Plantation (a.k.a. Mountain's View)", 'Belle Vue/Stony Hill Plantation', "Belmont/Murray's", \
"Belvedere Plantation (a.k.a. Horne's)", "Bendal's Plantation", 'Body Ponds Plantation (a.k.a. Carleton)', \
"Boone's", "Brecknock's Plantation", "Briggin's (Little Zoar)", "Buckley's Plantation", 'Cassandra Gardens', \
'Cedar Valley Plantation', 'Clare Hall', "Cook's", "Creek Side/Thibou's Plantation", "Crosbie's", "Denfield's", \
"Drew's Hill", "Dunbar's", 'Five Islands Plantation (Upper and Lower: Pelican)', "Friar's Hill", \
'Galley Bay Plantation', "Gamble's", "George Byam's Plantation", "Golden Grove (Paul's)", "Gray's/Turnbil's", \
"Halliday's Mountation (a.k.a. Gillead's, Gilliat's, or Providence)", "Hart's and Royal's", \
"Hawkebill's Plantation (a.k.a. Hanson's)", "Herbert's", 'Hill House/Dry Hill', "Hodge's", "Langford's", \
'Marble Hill', 'McKinnon', 'Mount Pleasant', "Oliver's (Stock Estate)", "Otto's", "Potter's Plantation", \
"Renfrew's", 'Rose Hill and Hammersfield', "St. Clare/William's Plantation (Originally known as The Body)", \
"The Folly (Bath Lodge) Plantation (a.k.a. Duncomb's Folly)", 'The Union Plantation (Haddon/Hatton or Weekes)', \
'The Wood Plantation', 'Thibou/Jarvis Plantation (a.k.a. Mt. Joshua)', 'Tomlinson', 'Villa', "Weatherill's", \
'Williams', "Yepton's/Yapton Farm Plantation", 'Barbuda', "Betty's Hope", "Big Duer's", 'Brookes', \
'Cedar Hill (Hall)', 'Cochrans', 'Cocoa Nut Hall & Hawes', 'Cotton Garden', 'Cotton New Works', "Crabb's", \
"Freeman's Upper", "Gilbert's", 'Guiana Island', 'Jonas', "Little Duer's", "Lower Freeman's", "Martin's/Diamond", \
"Mercer's Creek", 'Pares', 'Parham Hill & Parham Lodge', 'Parham New Works', "Parry's", "Sanderson's/Osborne's", \
"Vernon's (Wakering Hall)", "Yeamon's", 'Christian Hill / Cussacks', "Room's", "Parson's Maul / Parson Maule's", \
"Glanville's", 'Collins', 'Grants', 'Jefferson / Zion Hill', 'Mayers / Benlomand', 'Retreat / Montgomery', \
'Comfort Hall', "Gray's Belfast / Lambert Hall", "Wickham's / Upper Freeman's", "Elliott' / French's", 'Lon Lane', \
"Gaynor's", 'The Grange', "Elme' Creek", "Goble' / Gable's", "Montpelie / Murray's", "Archbold's", \
"Brown' Bay/ harmony Hall", "Skerret' & Folly / Nugent's", "Colebrook's", "Walrond' Upper", "Walrond' Lower", \
"Frye' / Fry's", 'Th Hope', "Harman' / Harmon's / Lloyd's", "Lavington's", "Lynch's", "Lyon' (Upper & Lower)", \
"Manning's", "Sheriff' (Exchange)", "Watson's", 'Gree Island', "Harr Harding's", 'Th Grange', 'Matthews', "Burke's", \
"Blake's", 'L Roche', 'Luca / Rock Hill', "Delap's", 'Thomas', "Cochran' (Bethesda)", "Gale' (Table Hill Gordon)", \
"Morri Looby's", "Bodkin's", "Willi Freeman's", 'Tyrrel\' (Formerly Tankard\'s or "Orleans")', \
"Mill Byam's (Folly / Byam)", 'Savannah', 'Picadilly', "Richmond's", "Howard's", "Horseford's", "Patterson's", \
"Swete' (Sweet's)", "Buckshorne's", "Barter' (Osborne's / Windward)", "Doig's", \
"Dimsdal (Michael's Mount / Langham's)", 'Dee Bay / Dieppe Bay', "Fry' Pasture", "Isaac' Hill", \
"Guine Bush (Monk's Hill)", 'Cherr Hill (miscellaneous)', 'Wind Hill (miscellaneous)', \
"Tuck' (Farley Bay? miscellaneous)", "Farley' (Tuck's? miscellaneous)", \
"Freeman' Rest (Fig Tree Hill - miscellaneous)", 'Cabadg (Cabbage) Tree Plantation (miscellaneous)', \
'Barre Beef Estate (miscellaneous)', "Seaforth's", 'Smith (Darby)', "Rigby (Perry's)", 'Gree Castle', \
"Montero's", 'Ne Division (Tremills)', 'Hermitage', 'Joll Hill', 'Blubbe Valley (Rose Valley)', 'Tranquil Vale', \
'Tottenham Park', "Willock's", "Ffry' (Fry's)", 'Orang Valley (Furlongs)', "Picart' (Herman Vale)", "Sawcolt's", \
"Sag Hill (Tom Moore's Mill / Upper)", 'Mil Hill', 'Claremon (see #178)', 'Tremontain / The Mountain', "Young's", \
'Young / Nantons', 'Brook (Old Road)', "Morris' (Old Mill / Brambles)", "Douglas' Estate (Ravenscroft)", \
"Yorke' (Musketo Cove & Bear Gardens)", 'Christia Valley / Biffins']

def popupBonus(image_name):
	"""
		General seperate method that procures a popup
	"""
	toplevel = Toplevel()
	image = Image.open(image_name)
	image_copy = image.copy()
	image = image_copy.resize((650, 500))

	background_image = ImageTk.PhotoImage(image)

	label = tk.Label(toplevel,image=background_image)
	label.pack(fill=BOTH, expand=YES)

	label.image = background_image

	label.place(x=0, y=0, relwidth=1.0, relheight=1.0, anchor="nw")
	toplevel.geometry('650x500')

def edit_file_name(filename):
	"""
		General method for the many times I have to play with filenames (oh so many).
	"""
	filename = filename + ".txt"
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
	return filename

# Basic structure found on StackOverflow.  Citation:
# https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter
class ResearcherGUI(tk.Tk):
	"""
		Class to create and implement the root frame of the GUI.
	"""

	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)
		call(["git", "pull"])
		# Set relevant styling
		self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")

		# the container is where we'll stack a bunch of frames
		# on top of each other, then the one we want visible
		# will be raised above the others
		container = tk.Frame(self)
		container.config(bg='steelblue')
		container.grid(row=0)
		container.master.title("Researcher's Interface")

		#Create the particular frames for the two types of pages.  Use the classes created later.
		self.frames = {}
		for F in (StartPage, PageOne):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

			# put all of the pages in the same location;
			# the one on the top of the stacking order
			# will be the one that is visible.
			frame.grid(row=1, sticky="nsew")
		# Begin by showing the starting page.
		self.show_frame("StartPage", "NA")

	def show_frame(self, page_name, mill_name):
		"""
			When called, swaps the current frame to be the page we wish to see.
		"""
		frame = self.frames[page_name]
		if page_name == "StartPage":
			frame.show_again()
		elif page_name == "PageOne":
			frame.grid_propagate(1)
			frame.add_mill_specific(mill_name)
		frame.tkraise()


class StartPage(tk.Frame):
	"""
		Class for the opening page of the python GUI.  Will have a title, a list of the available mills, and the ability
		to choose a mill to go to its researcher's page.
	"""

	def __init__(self, parent, controller):
		"""
			Initialize all frames for displaying for the Start Page.
		"""

		# To allow for ease of coloring and placement, each grouping of items is given its own frame, and each frame
		# is placed on our main controller.
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.controller.config(bg='steelblue')
		self.button_frame = tk.Frame(self.controller)
		self.bottom_button_frame = tk.Frame(self.controller)

		# Creating the main label.
		self.label = tk.Label(self, text="Antigua Map Researcher's GUI", font=controller.title_font, bg = 'dark turquoise')
		self.label.grid(row=0)
		self.label.grid_rowconfigure(0, weight=1)

		# Create the Listbox and load into it all Mill names.
		self.listbox = Listbox(controller, background = 'goldenrod', width=60)

		for i in MILL_DATA:
			self.listbox.insert(END, str(i))

		# Initialize the style for buttons (so that it will function for Macs)
		ttk.Style().configure('green/black.TButton', foreground='goldenrod', background='steelblue')

		button1 = ttk.Button(self.button_frame, text="Go to Mill's Page", style='green/black.TButton',
							command=lambda: self.swap_and_forget("PageOne", self.listbox.curselection()))
		button1.pack()
		button2 = ttk.Button(self.bottom_button_frame, text="Update the Map!", style='green/black.TButton',
							command=lambda: self.push_changes())
		button2.pack()

		# Place the buttons and listbox onto the frame.
		self.button_frame.grid(row=1)
		self.button_frame.grid_rowconfigure(1, weight=1)
		self.button_frame.config(bg = 'steelblue')
		self.listbox.grid(row = 2, sticky='nsew')
		self.bottom_button_frame.grid(row=3)
		self.bottom_button_frame.grid_rowconfigure(3, weight=1)
		self.bottom_button_frame.config(bg = 'steelblue')
		self.controller.geometry("537x280")

	def swap_and_forget(self, page_info, box_input):
		"""
			Change to a specific mill's page.  Remove all information for the start page and tell
			Root to swap pages.
		"""
		# We first check to see if there is any input at all
		if box_input:
			self.listbox.grid_forget()
			self.controller.show_frame(page_info, MILL_DATA[box_input[0]])
			self.controller.geometry("930x716")
		else:
			return

	def show_again(self):
		"""
			Put things back on the root frame.
		"""
		self.label.grid(row=0)
		self.button_frame.grid(row=1)
		self.listbox.grid(row=2)
		self.bottom_button_frame.grid(row=3)
		self.controller.geometry("537x280")

	def push_changes(self):
		"""
			Pushes changes to the Mill Files to the remote repository.
		"""
		call(["git", "remote", "set-url", "origin", "git@github.com:particknewhart/Antigua.git"])
		call(["git", "add", "Mill_Files"])
		call(["git", "add", "mill_data.json"])
		call(["git", "commit", "-m", '"Mill files updated"'])
		call(["git", "pull"])
		call(["git", "push"])
		popupBonus("GriotTree.jpeg")


class PageOne(tk.Frame):
	"""
		Frame that allows user to edit information for a specific Mill.  Loads that Mill's current information,
		allows a user to edit it and save it to the Mill's relevant files.
	"""

	def __init__(self, parent, controller):
		"""
			Create all relevant frames, and lists of widgets that will need to disappear later.
		"""
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.main_label_frame = tk.Frame(self.controller)
		self.main_label = None
		self.button_frame = tk.Frame(self.controller, highlightbackground='dark turquoise')
		self.button_list = []
		self.sub_label_list = []
		self.entry_list = []
		self.frame_list = []

	def add_mill_specific(self, mill_name):
		"""
			Depending on which mill is chosen, that mill's information must be gathered, and its name
			must be displayed.
		"""

		# Display relevant mill's name
		self.main_label = tk.Label(self.main_label_frame, text=mill_name, \
			font=self.controller.title_font, bg='steelblue')
		self.main_label.pack()
		self.main_label_frame.grid(row=0, sticky=E+W+N+S)
		self.main_label_frame.grid_rowconfigure(0, weight=1)
		self.main_label_frame.config(background = 'steelblue')

		# Prepare and implement all things for the image processing
		self.image_frame = tk.Frame(self.controller, bg = 'steelblue')
		self.image_label = tk.Label(self.image_frame, text = "Mill's Image (JPEGs Only):", \
			font=12, bg = 'dark turquoise')

		updated_mill_name = "Mill_Files/Photos/" + edit_file_name(mill_name)[:-4] + ".jpeg"
		self.image_view = ttk.Button(self.image_frame, text="View Current Image", style='green/black.TButton',\
			command=lambda: self.find_and_view_image(updated_mill_name))
		self.image_upload = ttk.Button(self.image_frame, text="Upload New Image", style='green/black.TButton',\
			command=lambda: self.find_and_upload_image(updated_mill_name))

		self.image_label.grid(row=0, column=0)
		self.image_view.grid(row=0, column=1)
		self.image_upload.grid(row=0, column=2)
		self.image_frame.grid(row=1)

		# Prepare to find the file name for the specific information
		orig_filename = mill_name

		new_frame = tk.Frame(self.controller, bg = 'steelblue')


		for index in range(2):
			filename = edit_file_name(mill_name)
			filename = "Mill_Files/" + SUB_SECTIONS_NOSPACE[index] + '/' + filename
			temp_box = tk.Text(new_frame, height=5, width=40, background = 'goldenrod', borderwidth = 1, wrap = CHAR)
			with open(filename, 'r') as text_file:
				try:
					temp_box.insert(END, text_file.read())
				except AttributeError:
					pass
			temp_label = tk.Label(new_frame, text=SUB_SECTIONS[index], font=12, bg = 'dark turquoise')

			temp_label.grid(row = 0, column = index)
			temp_box.grid(row = 1, column = index)

			# Place the text box and label into a frame, then place that frame in the next available location.
			self.sub_label_list += [temp_label]
			self.entry_list += [temp_box]

		new_frame.grid(row = 2)
		new_frame.grid_rowconfigure(2, weight=1)
		self.frame_list += [new_frame]

		new_frame = tk.Frame(self.controller, bg = 'steelblue')

		for index in range(2,5):
			filename = edit_file_name(mill_name)
			filename = "Mill_Files/" + SUB_SECTIONS_NOSPACE[index] + '/' + filename
			temp_box = tk.Text(new_frame, height=5, width=40, background = 'goldenrod', borderwidth = 1, wrap = CHAR)
			with open(filename, 'r') as text_file:
				try:
					temp_box.insert(END, text_file.read())
				except AttributeError:
					pass
			temp_label = tk.Label(new_frame, text=SUB_SECTIONS[index], font=12, bg = 'dark turquoise')

			temp_label.grid(row = 0, column = index)
			temp_box.grid(row = 1, column = index)

			# Place the text box and label into a frame, then place that frame in the next available location.
			self.sub_label_list += [temp_label]
			self.entry_list += [temp_box]

		new_frame.grid(row = 3)
		new_frame.grid_rowconfigure(3, weight=1)
		self.frame_list += [new_frame]

		# For each section, find the relevant file and create a textbox with a label.
		for index in range(len(SECTIONS)):
			new_frame = tk.Frame(self.controller, bg = 'steelblue')
			filename = edit_file_name(mill_name)
			filename = "Mill_Files/" + SECTIONS_NOSPACE[index] + '/' + filename

			temp_box = tk.Text(new_frame, height=5, width=130, background = 'goldenrod', borderwidth = 1, wrap = CHAR)
			with open(filename, 'r') as text_file:
				try:
					temp_box.insert(END, text_file.read())
				except AttributeError:
					pass
			temp_label = tk.Label(new_frame, text=SECTIONS[index], font=12, bg = 'dark turquoise')

			# We want the chronology section to have a special label, so we check:
			if SECTIONS[index] == 'Chronology':
				self.add_in_chronology(new_frame, index, temp_box)
				continue
			temp_label.pack()
			temp_box.pack()

			# Place the text box and label into a frame, then place that frame in the next available location.
			new_frame.grid(row = (index + 4))
			new_frame.grid_rowconfigure((index+4), weight=1)
			self.sub_label_list += [temp_label]
			self.entry_list += [temp_box]
			self.frame_list += [new_frame]

		# Style the two buttons at the bottom to follow Griot conventions.
		ttk.Style().configure('green/black.TButton', foreground='goldenrod', background='steelblue')

		reset_button = ttk.Button(self.button_frame, text="Update Information!", style='green/black.TButton',\
			command=lambda: self.update(orig_filename))

		button = ttk.Button(self.button_frame, text="Go to the start page", style='green/black.TButton',
						   command=lambda: self.clear_and_return())

		# Hold onto the buttons so that we can erase them later, then place them under everything else.
		self.button_list = [reset_button, button]
		reset_button.grid(row=0)
		reset_button.grid_rowconfigure(0, weight=1)
		button.grid(row=1)
		button.grid_rowconfigure(0, weight=1)
		self.button_frame.grid(row = len(SECTIONS)+5)
		self.button_frame.grid_rowconfigure(0, weight=1)

	def add_in_chronology(self, new_frame, index, temp_box):
		"""
			We want our chronology to be special.  So here we are.
		"""
		temp_label_1 = tk.Label(new_frame, text=SECTIONS[index], font=12, bg = 'dark turquoise')
		temp_label_2 = tk.Label(new_frame, text="Please Input using Format =>\n[YEAR]:[INFORMATION ABOUT YEAR]\nexample -> 1994:Murph was born",
			font=12, bg = 'dark turquoise')
		temp_label_1.grid(row=0)
		temp_label_2.grid(row=1)
		temp_box.grid(row=2)
		new_frame.grid(row = (index + 4))
		new_frame.grid_rowconfigure((index+4), weight=1)
		self.sub_label_list += [temp_label_1]
		self.sub_label_list += [temp_label_2]
		self.entry_list += [temp_box]
		self.frame_list += [new_frame]


	def clear_and_return(self):
		"""
			If we wish to return to the main page, we need to delete everything we put on the frame.  Since we
			held onto everything as instance variables, this happens quickly.
		"""
		self.main_label_frame.grid_forget()
		[x.grid_forget() for x in self.entry_list]
		[x.grid_forget() for x in self.sub_label_list]
		[x.grid_forget() for x in self.frame_list]
		[x.grid_forget() for x in self.button_list]
		self.image_view.grid_forget()
		self.image_upload.grid_forget()
		self.image_frame.grid_forget()
		self.main_label.pack_forget()
		self.button_frame.grid_forget()
		self.grid_forget()
		self.controller.show_frame("StartPage", "NA")

	def update(self, orig_filename):
		"""
			If the user wishes to update the information, this method grabs what is currently in the textboxes
			and writes it to the files where the information belongs.
		"""
		my_input_list = [x.get("1.0",END) for x in self.entry_list]

		for index in range(len(SUB_SECTIONS)):
			filename = edit_file_name(orig_filename)
			filename = "Mill_Files/" + SUB_SECTIONS_NOSPACE[index] + '/' + filename
			print(filename)
			with open(filename, 'w') as text_file:
				text_file.write(my_input_list[index])

		for index in range(len(SECTIONS)):
			filename = edit_file_name(orig_filename)
			filename = "Mill_Files/" + SECTIONS_NOSPACE[index] + '/' + filename
			print(filename)
			with open(filename, 'w') as text_file:
				text_file.write(my_input_list[index+5])

		To_Json = txt_to_json()
		To_Json.convert_to_json()
		# import txt_to_json

		popupBonus("GriotTreeData.jpeg")

	def find_and_upload_image(self, mill_photo_name):
		"""
			Allows a user to access their file system for an image to upload to the GUI
		"""

		filename = filedialog.askopenfilename()
		if filename == '':
			return
		image = Image.open(filename).convert('RGB')
		image.save(mill_photo_name, format='JPEG')


	def find_and_view_image(self, image_name):
		"""
			Allows user to see image that is currently uploaded for a given mill.
		"""
		popupBonus(image_name)

# Begin process -- call classes
if __name__ == "__main__":
	app = ResearcherGUI()
	app.mainloop()
