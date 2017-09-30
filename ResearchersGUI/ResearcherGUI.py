import tkinter as tk                # python 3
from tkinter import font  as tkfont # python 3
from tkinter import *
#import Tkinter as tk     # python 2
#import tkFont as tkfont  # python 2

SECTIONS = ["Extant or Ruin", "Founding Date", "Chronology", "Additional Information", "Enslaved Peoples"]

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


class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=30, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.config(bg='steelblue')
        container.grid(row=0)
        # container.grid_rowconfigure(0, weight=2)
        # container.grid_columnconfigure(0, weight=2)

        self.frames = {}
        for F in (StartPage, PageOne):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=1, sticky="nsew")

        self.show_frame("StartPage", "NA")

    def show_frame(self, page_name, mill_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        if page_name == "StartPage":
            frame.show_again()
        elif page_name == "PageOne":
            frame.grid_propagate(1)
            frame.add_mill_specific(mill_name)
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.controller.config(bg='steelblue')
        label = tk.Label(self, text="Antigua Map Researcher's GUI", font=controller.title_font, bg = 'steelblue')
        label.grid(row=0)
        label.grid_rowconfigure(0, weight=1)

        # self.scrollbar = Scrollbar(controller)

        self.listbox = Listbox(controller, \
            background = 'steelblue', width=60)

        for i in MILL_DATA:
            self.listbox.insert(END, str(i))

        
        # self.scrollbar.config(command=self.listbox.yview)
        self.listbox.grid(sticky='nsew')
        # self.scrollbar.grid()
        # side=RIGHT, fill = BOTH, expand = True

        button1 = tk.Button(self, text="Go to Selected Mill's Page",
                            command=lambda: self.swap_and_forget("PageOne",\
                             MILL_DATA[self.listbox.curselection()[0]]))
        button1.config(bg='steelblue')
        button1.grid()
        # button2.pack(side = BOTTOM)

    def swap_and_forget(self, page_info, mill_name):
        self.listbox.grid_forget()
        # self.scrollbar.grid_forget()
        self.controller.show_frame(page_info, mill_name)

    def show_again(self):
        self.listbox.grid()
        # side=LEFT, fill=BOTH, expand = True
        # self.scrollbar.grid()


class PageOne(tk.Frame):

    def __init__(self, parent, controller):
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

        self.main_label = tk.Label(self.main_label_frame, text=mill_name, \
            font=self.controller.title_font, bg='steelblue')
        self.main_label.pack()
        self.main_label_frame.grid(row=0, sticky=E+W+N+S)
        self.main_label_frame.grid_rowconfigure(0, weight=1)
        self.main_label_frame.config(background = 'steelblue')

        orig_filename = mill_name.strip()

        for index in range(len(SECTIONS)):
            new_frame = tk.Frame(self.controller, bg = 'steelblue')
            filename = SECTIONS[index] + "_" + orig_filename + ".txt"
            filename = filename.replace("/", "")
            filename = "Mill_Files/" + filename

            temp_box = tk.Text(new_frame, height=5, width=130, background = 'goldenrod', borderwidth = 1, wrap = CHAR)
            with open(filename, 'r') as text_file:
                try:
                    temp_box.insert(END, text_file.read())
                except AttributeError:
                    pass
            temp_label = tk.Label(new_frame, text=SECTIONS[index], font=12, bg = 'dark turquoise')
            temp_label.pack()
            temp_box.pack()
            new_frame.grid(row = (index + 1))
            new_frame.grid_rowconfigure((index+1), weight=1)
            self.sub_label_list += [temp_label]
            self.entry_list += [temp_box]
            self.frame_list += [new_frame]

        reset_button = tk.Button(self.button_frame, text="Update Information!", \
            command=lambda: self.update(orig_filename))
        button = tk.Button(self.button_frame, text="Go to the start page",
                           command=lambda: self.clear_and_return())
        self.button_list = [reset_button, button]
        reset_button.grid(row=0)
        reset_button.grid_rowconfigure(0, weight=1)
        button.grid(row=1)
        button.grid_rowconfigure(0, weight=1)
        self.button_frame.grid(row = len(SECTIONS)+2)
        self.button_frame.grid_rowconfigure(0, weight=1)

        # LAYOUT


        # self.entry.pack()


    def clear_and_return(self):
        self.main_label_frame.grid_forget()
        [x.grid_forget() for x in self.entry_list]
        [x.grid_forget() for x in self.sub_label_list]
        [x.grid_forget() for x in self.frame_list]
        [x.grid_forget() for x in self.button_list]
        self.main_label.pack_forget()
        self.button_frame.grid_forget()
        self.grid_forget()
        self.controller.show_frame("StartPage", "NA")

    def update(self, orig_filename):
        my_input_list = [x.get("1.0",END) for x in self.entry_list]

        for index in range(len(SECTIONS)):
            filename = SECTIONS[index] + "_" + orig_filename + ".txt"
            filename = filename.replace("/", "")
            filename = "Mill_Files/" + filename
            with open(filename, 'w') as text_file:
                text_file.write(my_input_list[index])


        for my_input in my_input_list:
            with open(filename, 'w') as text_file:
                text_file.write(my_input)



# class PageTwo(tk.Frame):

#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         label = tk.Label(self, text="This is page 2", font=controller.title_font)
#         label.pack(side="top", fill="x", pady=10)
#         button = tk.Button(self, text="Go to the start page",
#                            command=lambda: controller.show_frame("StartPage", "NA"))
#         button.pack()


if __name__ == "__main__":
    app = SampleApp()
    app.mainloop()