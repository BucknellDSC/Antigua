import json
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
# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
data = []
for name in MILL_DATA:
    print (name)

# Define data
    a_data = {
  "name": name,
  "parish": "St. John's",
  "founding_date": "1670",
  "type": "Extant",
  "long": "17.229085",
  "lat": "-61.833746",
  "chronology": {
    "1670": "William Boone, planter.  On Antigua 1665, still living in 1710.",
    "1672": "William Boone, still living in 1685; leased 10 acres from Ralph Haskins, also a planter.",
    "1676": "William Boone, a Quaker, was imprisoned by Major Thomas Mallet",
    "1678": "On May 20, Walter Burke, a planter, sold 20 acres to William Boone, a planter and Quaker.  In the census of Antigua taken in",
    "1700": "William Boone married Mary Ronan.",
    "1715": "Samuel Boone.  Will dated 1716.",
    "1717": "The Tortola census, taken in November, shows William Boone as born in Antigua, with \"one woman and fifteen negroes.\"",
    "1733": "Joseph Boone married Rachell Soanes.  He died 1750.",
    "1740": "Colonel William Dunbar.  d. 1749.",
    "1760": "John Delap-Halliday.  Owned 85 acres.  b. 1749; d. 1779/80.",
    "1788": "Admiral John Halliday Tollemache.   (1777/78 map by cartographer John Luffman.)",
    "1790": "John Delap-Halliday.  b. 1749; d. 1780.  85 acres.",
    "1852": "John Tollemache.  b. 1805; d. 1890.",
    "1872": "Charles Crosbie.",
    "1878": "G. John Crosbie.",
    "1891": "The heirs of Colonel Crosbie.",
    "1900": "John J. Camacho.  (d. 1929).",
    "1940": "Lee H. Westcott Sr.",
    "1960": "Blue Waters Hotel, built by O. (Keltic) Kelsick, the only Antiguan squadron leader in the Royal Air Force during World War II.",
    "2000": "The heirs of Lee Westcott.  d. 2012.",
    "2003": "The mill site is sold to Blue Waters Hotel"
  },
  "info": "The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas. The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas. The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas. The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas.  The magnificent sugar mill on this plantation stood water-side on the northwestern tip of Antigua, where the Caribbean and the Atlantic shake hands.  A rock formation known as \"Boone's Chair\" had been carved out of the rock by early settlers, enabling local Carib Indians to sit and look at the intersection of the two seas."
    }
    data.append(a_data)

# Write JSON file
with io.open('data.json', 'a', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))