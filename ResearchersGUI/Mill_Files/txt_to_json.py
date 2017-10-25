import json
import os

OLD_MILL_DATA = ['Barnacle Point', 'Barnes Hill', "Blackman's/Mount Lucie", 'Carlisles', 'Date Hill', \
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

MILL_DATA = ['Barnacle Point.txt', 'Barnes Hill.txt', 'BlackmansMount Lucie.txt', 'Carlisles.txt', 'Date Hill.txt', 'Donovans (Vaughans).txt',\
 'Fitches Creek.txt', 'Giles Blizzard.txt', 'Gravenors.txt', 'Gunthorpes (ASF).txt', 'Hight Point.txt', 'Judge Blizzards.txt', \
 'LightfootsThe Grove.txt', 'Long Island.txt', 'Millars.txt', 'Nibbs.txt', 'North Sound (Thomass HillCol. Thomas North Sound Plantation.txt',\
 'Paynters.txt', 'SherwoodsLebanon.txt', 'Weirs (WaresGlanvillesLittle Zoar).txt', 'Will Blizzards.txt', 'Winthorpes.txt',\
 'Allens Plantation (a.k.a. Mountains View).txt', 'Belle VueStony Hill Plantation.txt', 'BelmontMurrays.txt',\
 'Belvedere Plantation (a.k.a. Hornes).txt', 'Bendals Plantation.txt', 'Body Ponds Plantation (a.k.a. Carleton).txt', 'Boones.txt',\
 'Brecknocks Plantation.txt', 'Briggins (Little Zoar).txt', 'Buckleys Plantation.txt', 'Cassandra Gardens.txt', 'Cedar Valley Plantation.txt',\
 'Clare Hall.txt', 'Cooks.txt', 'Creek SideThibous Plantation.txt', 'Crosbies.txt', 'Denfields.txt', 'Drews Hill.txt', 'Dunbars.txt',\
 'Five Islands Plantation (Upper and Lower Pelican).txt', 'Friars Hill.txt', 'Galley Bay Plantation.txt', 'Gambles.txt', 'George Byams Plantation.txt',\
 'Golden Grove (Pauls).txt', 'GraysTurnbils.txt', 'Hallidays Mountation (a.k.a. Gilleads, Gilliats, or Providence).txt', 'Harts and Royals.txt',\
 'Hawkebills Plantation (a.k.a. Hansons).txt', 'Herberts.txt', 'Hill HouseDry Hill.txt', 'Hodges.txt', 'Langfords.txt', 'Marble Hill.txt', 'McKinnon.txt',\
 'Mount Pleasant.txt', 'Olivers (Stock Estate).txt', 'Ottos.txt', 'Potters Plantation.txt', 'Renfrews.txt', 'Rose Hill and Hammersfield.txt',\
 'St. ClareWilliams Plantation (Originally known as The Body).txt', 'The Folly (Bath Lodge) Plantation (a.k.a. Duncombs Folly).txt',\
 'The Union Plantation (HaddonHatton or Weekes).txt', 'The Wood Plantation.txt', 'ThibouJarvis Plantation (a.k.a. Mt. Joshua).txt',\
 'Tomlinson.txt', 'Villa.txt', 'Weatherills.txt', 'Williams.txt', 'YeptonsYapton Farm Plantation.txt', 'Barbuda.txt', 'Bettys Hope.txt',\
 'Big Duers.txt', 'Brookes.txt', 'Cedar Hill (Hall).txt', 'Cochrans.txt', 'Cocoa Nut Hall & Hawes.txt', 'Cotton Garden.txt',\
 'Cotton New Works.txt', 'Crabbs.txt', 'Freemans Upper.txt', 'Gilberts.txt', 'Guiana Island.txt', 'Jonas.txt', 'Little Duers.txt',\
 'Lower Freemans.txt', 'MartinsDiamond.txt', 'Mercers Creek.txt', 'Pares.txt', 'Parham Hill & Parham Lodge.txt', 'Parham New Works.txt',\
 'Parrys.txt', 'SandersonsOsbornes.txt', 'Vernons (Wakering Hall).txt', 'Yeamons.txt', 'Christian Hill  Cussacks.txt', 'Rooms.txt',\
 'Parsons Maul  Parson Maules.txt', 'Glanvilles.txt', 'Collins.txt', 'Grants.txt', 'Jefferson  Zion Hill.txt', 'Mayers  Benlomand.txt',\
 'Retreat  Montgomery.txt', 'Comfort Hall.txt', 'Grays Belfast  Lambert Hall.txt', 'Wickhams  Upper Freemans.txt', 'Elliott  Frenchs.txt',\
 'Lon Lane.txt', 'Gaynors.txt', 'The Grange.txt', 'Elme Creek.txt', 'Goble  Gables.txt', 'Montpelie  Murrays.txt', 'Archbolds.txt',\
 'Brown Bay harmony Hall.txt', 'Skerret & Folly  Nugents.txt', 'Colebrooks.txt', 'Walrond Upper.txt', 'Walrond Lower.txt',\
 'Frye  Frys.txt', 'Th Hope.txt', 'Harman  Harmons  Lloyds.txt', 'Lavingtons.txt', 'Lynchs.txt', 'Lyon (Upper & Lower).txt', 'Mannings.txt',\
 'Sheriff (Exchange).txt', 'Watsons.txt', 'Gree Island.txt', 'Harr Hardings.txt', 'Th Grange.txt', 'Matthews.txt', 'Burkes.txt', 'Blakes.txt',\
 'L Roche.txt', 'Luca  Rock Hill.txt', 'Delaps.txt', 'Thomas.txt', 'Cochran (Bethesda).txt', 'Gale (Table Hill Gordon).txt', 'Morri Loobys.txt',\
 'Bodkins.txt', 'Willi Freemans.txt', 'Tyrrel (Formerly Tankards or Orleans).txt', 'Mill Byams (Folly  Byam).txt', 'Savannah.txt', 'Picadilly.txt',\
 'Richmonds.txt', 'Howards.txt', 'Horsefords.txt', 'Pattersons.txt', 'Swete (Sweets).txt', 'Buckshornes.txt', 'Barter (Osbornes  Windward).txt',\
 'Doigs.txt', 'Dimsdal (Michaels Mount  Langhams).txt', 'Dee Bay  Dieppe Bay.txt', 'Fry Pasture.txt', 'Isaac Hill.txt', 'Guine Bush (Monks Hill).txt',\
 'Cherr Hill (miscellaneous).txt', 'Wind Hill (miscellaneous).txt', 'Tuck (Farley Bay miscellaneous).txt', 'Farley (Tucks miscellaneous).txt',\
 'Freeman Rest (Fig Tree Hill - miscellaneous).txt', 'Cabadg (Cabbage) Tree Plantation (miscellaneous).txt', 'Barre Beef Estate (miscellaneous).txt',\
 'Seaforths.txt', 'Smith (Darby).txt', 'Rigby (Perrys).txt', 'Gree Castle.txt', 'Monteros.txt', 'Ne Division (Tremills).txt', 'Hermitage.txt',\
 'Joll Hill.txt', 'Blubbe Valley (Rose Valley).txt', 'Tranquil Vale.txt', 'Tottenham Park.txt', 'Willocks.txt', 'Ffry (Frys).txt',\
 'Orang Valley (Furlongs).txt', 'Picart (Herman Vale).txt', 'Sawcolts.txt', 'Sag Hill (Tom Moores Mill  Upper).txt', 'Mil Hill.txt',\
 'Claremon (see #178).txt', 'Tremontain  The Mountain.txt', 'Youngs.txt', 'Young  Nantons.txt', 'Brook (Old Road).txt', 'Morris (Old Mill  Brambles).txt',\
 'Douglas Estate (Ravenscroft).txt', 'Yorke (Musketo Cove & Bear Gardens).txt', 'Christia Valley  Biffins.txt']


# Make it work for Python 2+3 and with Unicode
import io
try:
    to_unicode = unicode
except NameError:
    to_unicode = str
data = []


for name in MILL_DATA:

    mill_name = name[:-4]

    #print('FoundingDate/' + mill_name + '.txt')
    founding_date_file = open('FoundingDate/' + mill_name + '.txt','r')
    founding_date = founding_date_file.read()

    # Define data
    a_data = {
    "name": mill_name,
    "parish": "Some Parish",
    "founding_date": founding_date,
    "type": "Extant / Ruined",
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
    "additional_info": "Placeholder Data."
    }
    data.append(a_data)


# Write JSON file
with io.open('mill_data.json', 'w', encoding='utf8') as outfile:
    str_ = json.dumps(data,
                    indent=4, sort_keys=True,
                    separators=(',', ': '), ensure_ascii=False)
    outfile.write(to_unicode(str_))
