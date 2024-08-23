import pandas as pd
import numpy as np
from CUNY_FUNCTIONS import haversine, find_closest_school

# READ IN CSV found at: https://data.cityofnewyork.us/Social-Services/Directory-Of-Homeless-Drop-In-Centers/bmxf-3rd4/data_preview
df_homeless = pd.read_csv('Directory_Of_Homeless_Drop-_In_Centers_20240821.csv')

# FILTER TO ONLY GET SPECIFIC COLUMNS
df_homeless_filtered = df_homeless[['Center Name', 'Borough', 'Address', 'Latitude', 'Longitude']]

# GET MANHATTAN COLLEGES NAMES & LONGITUDE WITH LATITUDE FOR HAVERSINE CALCULATION
Manhattan_Colleges = {'School Name_Longitude_Latitude' : 
    {'Baruch College' : (40.740471862767045, -73.98320075070929),
    'Borough of Manhattan Community College' : (40.71953032467742, -74.0122583597809),
    'The City College' : (40.82020054356874, -73.94920121829529),
    'The Graduate School and University Center' : (40.74872291234521, -73.98399902588334),
    'The Craig Newmark Graduate School Of Journalism At CUNY' : (40.75549343186426, -73.9888838498554),
    'The CUNY School of Professional Studies' : (40.748624471288885, -73.98997774243172),
    'The CUNY School of Public Health & Health Policy' : (40.80759882826305, -73.94413677128836),
    'Guttman Community College' : (40.753085075885885, -73.98393315408056),
    'Hunter College' : (40.767856030242825, -73.96451868134449),
    'John Jay College' : (40.77078057677287, -73.98922347116479)}}

# GET BRONX COLLEGES NAMES & LONGITUDE WITH LATITUDE FOR HAVERSINE CALCULATION
Bronx_Colleges = {'School Name_Longitude_Latitude' : 
    { 'Bronx Community College' : (40.85751548111299, -73.91292584723408),
      'Hostos Community College' : (40.817419002533605, -73.92720556500196),
      'Lehman College' : (40.872893348653186, -73.89450564981139)}}

# GET BROOKLYN COLLEGES NAMES & LONGITUDE WITH LATITUDE FOR HAVERSINE CALCULATION
Brooklyn_Colleges = {'School Name_Longitude_Latitude' : 
    {'Brooklyn College' : (40.630885328954854, -73.95144727442647),
    'Kingsborough Community College' : (40.57867000887434, -73.93510072510999),
    'Medgar Evers College' : (40.66641360715036, -73.95705031971266),
    'New York City College of Technology (City Tech)' : (40.69542658817722, -73.9875059527966)}}

# GET STATEN ISLAND COLLEGES NAMES & LONGITUDE WITH LATITUDE FOR HAVERSINE CALCULATION
Staten_Island_College = {'School Name_Longitude_Latitude' : 
    {'College of Staten Island' : (40.602172525459245, -74.15037037442788)}}

# GET QUEENS COLLEGES NAMES & LONGITUDE WITH LATITUDE FOR HAVERSINE CALCULATION
Queens_College = {'School Name_Longitude_Latitude' : 
    {'CUNY School of Law' : (40.74774050199094, -73.94404506461541),
     'LaGuardia Community College' : (40.74380390826902, -73.93506238946675),
     'Queens College' : (40.736742923005956, -73.82031639878407),
     'Queensborough Community College' : (40.75541808820755, -73.75739998840511),
     'York College' : (40.70104134897624, -73.79610986464256)}}

# DATA FRAME FOR HOMELESS MANHATTAN
df_homeless_manhattan = df_homeless_filtered[df_homeless_filtered['Borough'] == 'Manhattan'].copy() 

# DATA FRAME FOR HOMELESS BRONX
df_homeless_bronx = df_homeless_filtered[df_homeless_filtered['Borough'] == 'Bronx'].copy()

# DATA FRAME FOR HOMELESS BROOKLYN
df_homeless_brooklyn = df_homeless_filtered[df_homeless_filtered['Borough'] == 'Brooklyn'].copy()

# DATA FRAME FOR HOMELESS STATEN ISLAND
df_homeless_staten_island = df_homeless_filtered[df_homeless_filtered['Borough'] == 'Staten Island'].copy()

# DATA FRAME FOR HOMELESS QUEENS
df_homeless_queens = df_homeless_filtered[df_homeless_filtered['Borough'] == 'Queens'].copy()

# GET ALL CUNY COLLEGES NAMES & LONGITUDE WITH LATITUDE FOR HAVERSINE CALCULATION
All_Cuny_Colleges = {'School Name_Longitude_Latitude' : 
    {'Baruch College' : (40.740471862767045, -73.98320075070929),
    'Borough of Manhattan Community College' : (40.71953032467742, -74.0122583597809),
    'The City College' : (40.82020054356874, -73.94920121829529),
    'The Graduate School and University Center' : (40.74872291234521, -73.98399902588334),
    'The Craig Newmark Graduate School Of Journalism At CUNY' : (40.75549343186426, -73.9888838498554),
    'The CUNY School of Professional Studies' : (40.748624471288885, -73.98997774243172),
    'The CUNY School of Public Health & Health Policy' : (40.80759882826305, -73.94413677128836),
    'Guttman Community College' : (40.753085075885885, -73.98393315408056),
    'Hunter College' : (40.767856030242825, -73.96451868134449),
    'John Jay College' : (40.77078057677287, -73.98922347116479),
    'CUNY School of Labor and Urban Studies': (40.754830, -73.981740),
    'Bronx Community College' : (40.85751548111299, -73.91292584723408),
    'Hostos Community College' : (40.817419002533605, -73.92720556500196),
    'Lehman College' : (40.872893348653186, -73.89450564981139),
    'Brooklyn College' : (40.630885328954854, -73.95144727442647),
    'Kingsborough Community College' : (40.57867000887434, -73.93510072510999),
    'Medgar Evers College' : (40.66641360715036, -73.95705031971266),
    'New York City College of Technology (City Tech)' : (40.69542658817722, -73.9875059527966),
    'College of Staten Island' : (40.602172525459245, -74.15037037442788),
    'CUNY School of Law' : (40.74774050199094, -73.94404506461541),
    'LaGuardia Community College' : (40.74380390826902, -73.93506238946675),
    'Queens College' : (40.736742923005956, -73.82031639878407),
    'Queensborough Community College' : (40.75541808820755, -73.75739998840511),
    'York College' : (40.70104134897624, -73.79610986464256)}}


# print(pd.DataFrame(All_Cuny_Colleges).nunique()) 23 CUNY COLLLEGES

college_names = list(All_Cuny_Colleges['School Name_Longitude_Latitude'].keys())
coordinates = list(All_Cuny_Colleges['School Name_Longitude_Latitude'].values())

college_df = pd.DataFrame({
    'College Name': college_names,
    'Latitude': [coord[0] for coord in coordinates],
    'Longitude': [coord[1] for coord in coordinates]
})
    
# CONVERT MANHATTAN DICTIONARY INTO A DATA FRAME
df_Manhattan_Colleges = pd.DataFrame(Manhattan_Colleges)

# ******* TESTING *******
# specific_LAT_STUFF = df_Manhattan_Colleges[df_Manhattan_Colleges['School Name_Longitude_Latitude'] == (40.740471862767045, -73.98320075070929)]
# print(df_homeless_manhattan[['Latitude', 'Longitude']])
# print(df_Manhattan_Colleges)

# for Lat in df_homeless_manhattan[['Latitude', 'Longitude']].items():
# ****** print(Lat) *******

# PUTTING IN MANHATTAN NUMBERS
Manhattan_Nums = ['212-833-0680', '212-594-2359', None]

# TRANSFORMED DF FOR MANHATTAN LAT & LON INTO FLOAT TYPES
df_homeless_manhattan.loc[:, 'Latitude'] = df_homeless_manhattan['Latitude'].astype(float)
df_homeless_manhattan.loc[:, 'Longitude'] = df_homeless_manhattan['Longitude'].astype(float)

# LIST TO STORE HOMELESS MANHATTAN SHELTERS
homeless_manhattan_colleges = []

# ADD NEW COLUMN INTO MANHATTAN DATA FRAME
df_homeless_manhattan.loc[:, 'Phone Number'] = Manhattan_Nums

# New rows of data for manhattan
new_manhattan_rows = [
    {'Center Name': 'Ali Forney Center', 
     'Address': '307 W 38th St, New York, NY 10018', 
     'Borough': 'Manhattan',
     'Latitude': 40.75513111685004,
     'Longitude': -73.9923542671043,
     'Phone Number': '212-206-0574',
     'CUNY Recommended': 1 },
    
    {'Center Name': 'The Door', 
     'Address': '555 Broome St, New York, NY 10013', 
     'Borough': 'Manhattan',
     'Latitude': 40.72410624138032,
     'Longitude': -74.00559652497343,
     'Phone Number': '212-941-9090',
     'CUNY Recommended': 1 },
    
    {'Center Name': 'Safe Horizon Streetwork Harlem', 
     'Address': '209 W 125th St, New York, NY 10027', 
     'Borough': 'Manhattan',
     'Latitude': 40.809382421786495,
     'Longitude': -73.94879364886535,
     'Phone Number': '212-695-2220',
     'CUNY Recommended': 1 },
    
    {
     'Center Name': 'Grand Central Neighborhood', 
     'Address': '120 E 32nd St, New York, NY 10016', 
     'Borough': 'Manhattan',
     'Latitude': 40.745244713218376, 
     'Longitude': -73.98143269120199,
     'Phone Number': '212-883-0680'
    },
    
    {
     'Center Name': 'The Bowery Mission - Tribeca Campus', 
     'Address': '90 Lafayette St, New York, NY 10013', 
     'Borough': 'Manhattan',
     'Latitude': 40.71750110267228, 
     'Longitude': -74.0016662372824, 
     'Phone Number': '212-226-6214'
    },
    
    {
     'Center Name': 'Urban Resource Institute', 
     'Address': '75 Broad St, New York, NY 10004', 
     'Borough': 'Manhattan',
     'Latitude': 40.704618547657454, 
     'Longitude': -74.01123209251429, 
     'Phone Number': '646-588-0030'
    },
    
    {
     'Center Name': 'Lalitamba Saranam', 
     'Address': 'PO Box 131 New York, NY 10024', 
     'Borough': 'Manhattan',
     'Latitude': 40.785911202514036, 
     'Longitude': -73.97425917956798, 
     'Phone Number': '212-873-0140'
    },
    
    {
     'Center Name': 'Project Renewal Third Street Mens Shelter', 
     'Address': '8 E 3rd St #8908, New York, NY 10003', 
     'Borough': 'Manhattan',
     'Latitude': 40.72584662603532, 
     'Longitude': -73.99102572396676,
     'Phone Number': '212-533-8400'
    },
    
    {
     'Center Name': '30th Street Mens Shelter Health Center', 
     'Address': '400 E 30th St, New York, NY 10016', 
     'Borough': 'Manhattan',
     'Latitude': 40.7404751598799, 
     'Longitude': -73.97400673137356,
     'Phone Number': '212-359-2820'
    },
    
    {
     'Center Name': 'Covenant House New York', 
     'Address': '460 W 41st St, New York, NY 10036', 
     'Borough': 'Manhattan',
     'Latitude': 40.75861911184105, 
     'Longitude': -73.99555441941283 ,
     'Phone Number': '212-613-0300'
    },
    
    {
     'Center Name': 'Breaking Ground', 
     'Address': '505 Eighth Avenue, 5th FloorNew York, NY 10018', 
     'Borough': 'Manhattan',
     'Latitude': 40.75317985312907, 
     'Longitude': -73.99322470769309,
     'Phone Number': '212-389-9300'
    },
    
    {
     'Center Name': 'Samaritan Village', 
     'Address': '225 E 53rd St, New York, NY 10022', 
     'Borough': 'Manhattan',
     'Latitude': 40.757340707410854,
     'Longitude': -73.96828146437606,
     'Phone Number': None
    },
    
    {
     'Center Name': 'Bowery Residents Committee', 
     'Address': '131 W 25th St, New York, NY 10001', 
     'Borough': 'Manhattan',
     'Latitude': 40.744923781631584, 
     'Longitude': -73.99311188769332,
     'Phone Number': '212-803-5700'
    },
    
    {
     'Center Name': 'Trinity Place Shelter', 
     'Address': '164 W 100th St, New York, NY 10025', 
     'Borough': 'Manhattan',
     'Latitude': 40.79621045446445, 
     'Longitude': -73.96808171813653,
     'Phone Number': '646-580-7045'
    },
]

# CONCAT THE NEW ROWS WITH MANHATTAN HOMELESS DATA FRAME
df_homeless_manhattan = pd.concat([df_homeless_manhattan, pd.DataFrame(new_manhattan_rows)], ignore_index=True)

# ITTERATE USING iterrows() on MANHATTAN DF
for index, location in df_homeless_manhattan.iterrows():
    
    # FIND CLOSEST SCHOOL USING FUNCTION FCS
    closest_school = find_closest_school(location, Manhattan_Colleges['School Name_Longitude_Latitude'])
    
    # print(f"The closest school to {location['Center Name']} is {closest_school}") (*****TESTING****)
    
    # APPEND SHELTER NAME AND COLLEGE CLOSEST TO THAT SHELTER
    homeless_manhattan_colleges.append([location['Center Name'], closest_school])

# CONVERT THE LIST INTO A NUMPY ARRAY FOR PERFORMANCE
homeless_manhattan_colleges_array = np.array(homeless_manhattan_colleges)

# CREATE DATAFRAME AND USING NP ARRAY TO CREATE NEW COLUMNS
df_homeless_manhattan_colleges = pd.DataFrame(homeless_manhattan_colleges_array, columns=['Center Name', 'Closest College'])

# FINALLY MERGE THE 2 DATA FRAMES TO GET ALL INFORMATION ON CLOSEST COLLEGE AND CENTER NAME
df_Manhattan_Help = pd.merge(df_homeless_manhattan_colleges, df_homeless_manhattan)
    
# FILL IN NA WITH 0 to represent CUNY CARES RECOMMENDED
df_Manhattan_Help.fillna({'CUNY Recommended' : 0}, inplace=True)

new_bronx_rows = [
    {'Center Name': 'Cardinal McCloskey Services', 
     'Address': '529 Courtlandt Ave, Bronx, NY 10451', 
     'Borough': 'Bronx',
     'Latitude': 40.8161273478613,
     'Longitude': -73.91999026491263,
     'Phone Number': '718-993-7700',
     'CUNY Recommended': 1 },
    
    {'Center Name': 'The Living Room', 
     'Address': '800 Barretto Street; Bronx, NY 10474', 
     'Borough': 'Bronx',
     'Latitude': 40.816615,
     'Longitude': -73.889883,
     'Phone Number': '718-893-3606',
     'CUNY Recommended': None },
    
    {'Center Name': 'FRANKLIN WILLIAMS WOMENS SHELTER', 
     'Address': '1122 Franklin Ave, Bronx, NY 10456', 
     'Borough': 'Bronx',
     'Latitude': 40.828124787728555,
     'Longitude': -73.9058161673152,
     'Phone Number': '718-842-9797',
     'CUNY Recommended': None },
    
   {'Center Name': 'PATH DHS Assessment Shelter', 
     'Address': '151 E 151st St, Bronx, NY 10451', 
     'Borough': 'Bronx',
     'Latitude': 40.82171873027406, 
     'Longitude': -73.92757736015133,
     'Phone Number': '718-503-6400',
     'CUNY Recommended': None }, 
   
   {'Center Name': 'Volunteers of America (1)', 
     'Address': '1375 Cromwell Ave, Bronx, NY 10452', 
     'Borough': 'Bronx',
     'Latitude': 40.84031379706285, 
     'Longitude': -73.92024960975446,
     'Phone Number': '718-293-2930',
     'CUNY Recommended': None }, 
   
   {'Center Name': 'Volunteers of America (2)', 
     'Address': '50 W Mount Eden Ave, Bronx, NY 10452', 
     'Borough': 'Bronx',
     'Latitude': 40.84445762370069, 
     'Longitude': -73.916249438536,
     'Phone Number': '718-716-2255',
     'CUNY Recommended': None }, 
   
   {'Center Name': 'Volunteers of America (3)', 
     'Address': '1887 Bathgate Ave, Bronx, NY 10457', 
     'Borough': 'Bronx',
     'Latitude': 40.8464378654409, 
     'Longitude': -73.89739858992915,
     'Phone Number': '718-466-3580',
     'CUNY Recommended': None }, 
   
   {'Center Name': 'Volunteers of America (4)', 
     'Address': '855 E 175th St, Bronx, NY 10460', 
     'Borough': 'Bronx',
     'Latitude': 40.840258802677155, 
     'Longitude': -73.88885609697294,
     'Phone Number': '718-893-0909',
     'CUNY Recommended': None }, 
   
   {'Center Name': 'Volunteers of America (5)', 
     'Address': '1150 Commonwealth Ave, Bronx, NY 10472', 
     'Borough': 'Bronx',
     'Latitude': 40.82862372223484, 
     'Longitude': -73.8672334050041,
     'Phone Number': None ,
     'CUNY Recommended': None }, 
   
   {'Center Name': 'America Volunteers', 
     'Address': '1564 Unionport Rd, Bronx, NY 10462', 
     'Borough': 'Bronx',
     'Latitude': 40.839822654203694, 
     'Longitude': -73.86180709544205, 
     'Phone Number': '718-828-5338',
     'CUNY Recommended': None }, 
   
   {'Center Name': 'Reaching New Heights', 
     'Address': '237 Landing Rd, Bronx, NY 10468', 
     'Borough': 'Bronx',
     'Latitude': 40.86261223827749, 
     'Longitude': -73.91128783144318, 
     'Phone Number': '212-803-5700',
     'CUNY Recommended': None }, 
   
   {'Center Name': 'MARRIOT BONVOY', 
     'Address': '2395 Grand Concourse, Bronx, NY 10468', 
     'Borough': 'Bronx',
     'Latitude': 40.86261223827749, 
     'Longitude': -73.91128783144318, 
     'Phone Number': '718-364-7650',
     'CUNY Recommended': None }, 
   
   {'Center Name': 'Siena House', 
     'Address': '85 W 168th St, Bronx, NY 10452', 
     'Borough': 'Bronx',
     'Latitude': 40.83848832680541, 
     'Longitude': -73.92393752530297,
     'Phone Number': '718-293-2390',
     'CUNY Recommended': None }, 
]

# HOMELESS BRONX LIST
homeless_bronx_colleges = []

# APPENDING NEW BRONX SHELTERS
df_homeless_bronx = pd.concat([pd.DataFrame(new_bronx_rows)], ignore_index=True)
for index, location in df_homeless_bronx.iterrows():
    closest_school = find_closest_school(location, Bronx_Colleges['School Name_Longitude_Latitude'])
    # print(f"The closest school to {location['Center Name']} is {closest_school}")
    homeless_bronx_colleges.append([location['Center Name'], closest_school])

homeless_bronx_colleges_array = np.array(homeless_bronx_colleges)
df_homeless_bronx_colleges = pd.DataFrame(homeless_bronx_colleges_array, columns=['Center Name', 'Closest College'])
df_Bronx_Help = pd.merge(df_homeless_bronx_colleges, df_homeless_bronx)

# FILL ALL NAN VALUES IN CUNY RECOMMENDED COL
df_Bronx_Help.fillna({'CUNY Recommended' : 0}, inplace=True)


# NEW ROWS SHELTERS FOR BROOKLYN
new_brooklyn_rows = [
    {'Center Name': 'SCO Family of Services', 
     'Address': '3674 Third Ave, Bronx, NY 10456', 
     'Borough': 'Brooklyn',
     'Latitude': 40.83459300665873, 
     'Longitude': -73.9036394877873,
     'Phone Number': '718-293-7401',
     'CUNY Recommended': 1 },
    
    {'Center Name': 'Providence House', 
     'Address': '703 Lexington Ave, Brooklyn, NY 11221', 
     'Borough': 'Brooklyn',
     'Latitude': 40.68988020653402, 
     'Longitude': -73.93271483342149,
     'Phone Number': '718-455-0197',
     'CUNY Recommended': None },
    
    {'Center Name': 'Ready Willing and Able', 
     'Address': '520 Gates Ave, Brooklyn, NY 11216', 
     'Borough': 'Brooklyn',
     'Latitude': 40.68662060213262, 
     'Longitude': -73.9450977758282,
     'Phone Number': '718-628-3223',
     'CUNY Recommended': None },
    
    {'Center Name': 'HELP Womens Shelter', 
     'Address': '104-152 Williams Ave, Brooklyn, NY 11207', 
     'Borough': 'Brooklyn',
     'Latitude': 40.67322260209598, 
     'Longitude': -73.90022710034704,
     'Phone Number': '718-483-7700',
     'CUNY Recommended': None },
    
    {'Center Name': 'CAMBA The Gathering Place', 
     'Address': '2402 Atlantic Ave, Brooklyn, NY 11233', 
     'Borough': 'Brooklyn',
     'Latitude': 40.67579930901325, 
     'Longitude': -73.90520223915638,
     'Phone Number': '718-385-8726',
     'CUNY Recommended': None },
    
    {'Center Name': 'Barbara Kleiman Residence', 
     'Address': '300 Skillman Ave, Brooklyn, NY 11211', 
     'Borough': 'Brooklyn',
     'Latitude': 40.716799086641366, 
     'Longitude': -73.93905759711917,
     'Phone Number': '718-963-3800',
     'CUNY Recommended': None },
    
    {'Center Name': 'BRC', 
     'Address': '146 Clay St, Brooklyn, NY 11222', 
     'Borough': 'Brooklyn',
     'Latitude': 40.73680550871135,
     'Longitude': -73.95199823998117,
     'Phone Number': '718-383-1910',
     'CUNY Recommended': None },
    
    {'Center Name': 'Armory Mens Shelter', 
     'Address': '1322 Bedford Ave, Brooklyn, NY 11216', 
     'Borough': 'Brooklyn',
     'Latitude': 40.67813857787603, 
     'Longitude': -73.95350356521462,
     'Phone Number': '718-636-3908',
     'CUNY Recommended': None },
    
    {'Center Name': 'Breaking Grounds Safe Haven', 
     'Address': '781 Clarkson Ave, Brooklyn, NY 11203', 
     'Borough': 'Queens',
     'Latitude': 40.65721804242698,
     'Longitude': -73.93235833997561,
     'Phone Number': '718-360-8000',
     'CUNY Recommended': None }
]

homeless_brooklyn_colleges = []

df_homeless_brooklyn = pd.concat([pd.DataFrame(new_brooklyn_rows)], ignore_index=True)
for index, location in df_homeless_brooklyn.iterrows():
    closest_school = find_closest_school(location, Brooklyn_Colleges['School Name_Longitude_Latitude'])
    # print(f"The closest school to {location['Center Name']} is {closest_school}")
    homeless_brooklyn_colleges.append([location['Center Name'], closest_school])

homeless_brooklyn_colleges_array = np.array(homeless_brooklyn_colleges)
df_homeless_brooklyn_colleges = pd.DataFrame(homeless_brooklyn_colleges_array, columns=['Center Name', 'Closest College'])
df_Brooklyn_Help = pd.merge(df_homeless_brooklyn_colleges, df_homeless_brooklyn)

# FILL ALL NAN VALUES IN CUNY RECOMMENDED COL
df_Brooklyn_Help.fillna({'CUNY Recommended' : 0}, inplace=True)

new_staten_island_rows = [
    {'Center Name': 'Project Hospitality', 
     'Address': '100 Park Ave, Staten Island, NY 10302', 
     'Borough': 'Staten Island',
     'Latitude': 40.63564017001498, 
     'Longitude': -74.1343281614341,
     'Phone Number': '718-448-1544',
     'CUNY Recommended': 1 },
    
    {'Center Name': 'A Shelter', 
     'Address': '2 Dehart Ave, Staten Island, NY 10303', 
     'Borough': 'Staten Island',
     'Latitude': 40.63674029143336, 
     'Longitude': -74.15705098644058,
     'Phone Number': None,
     'CUNY Recommended': None }
    ]

homeless_staten_island_colleges = []

df_homeless_staten_island = pd.concat([pd.DataFrame(new_staten_island_rows)], ignore_index=True)
for index, location in df_homeless_staten_island.iterrows():
    closest_school = find_closest_school(location, Staten_Island_College['School Name_Longitude_Latitude'])
    # print(f"The closest school to {location['Center Name']} is {closest_school}")
    homeless_staten_island_colleges.append([location['Center Name'], closest_school])

homeless_staten_island_colleges_array = np.array(homeless_staten_island_colleges)
df_homeless_staten_island_colleges = pd.DataFrame(homeless_staten_island_colleges_array, columns=['Center Name', 'Closest College'])
df_Staten_Island_Help = pd.merge(df_homeless_staten_island_colleges, df_homeless_staten_island)

# FILL ALL NAN VALUES IN CUNY RECOMMENDED COL
df_Staten_Island_Help.fillna({'CUNY Recommended' : 0}, inplace=True)

new_queens_rows = [
    {'Center Name': 'Safe Space', 
     'Address': '89-74 162nd St, Queens, NY 11432', 
     'Borough': 'Queens',
     'Latitude': 40.70475293294447, 
     'Longitude': -73.79810364894684,
     'Phone Number': '718-526-2400',
     'CUNY Recommended': 1 },

    {'Center Name': 'Sheltering Arms Far Rockaway', 
     'Address': '1600 Central Ave, Far Rockaway, NY 11691', 
     'Borough': 'Queens',
     'Latitude': 40.60517360413047, 
     'Longitude': -73.7522424881994,
     'Phone Number': '718-471-6818',
     'CUNY Recommended': 1 },
    
    {'Center Name': 'The Landing Family Shelter', 
     'Address': '94-00 Ditmars Blvd, East Elmhurst, NY 11369', 
     'Borough': 'Queens',
     'Latitude': 40.76974738868478, 
     'Longitude': -73.87577788126589,
     'Phone Number': '718-226-0414',
     'CUNY Recommended': None },
    
    {'Center Name': 'Sweet Home', 
     'Address': '3805 Hunters Point Ave, Long Island City, NY 11101', 
     'Borough': 'Queens',
     'Latitude': 40.736947615157646, 
     'Longitude': -73.92802286719026,
     'Phone Number': '929-244-1520',
     'CUNY Recommended': None },
    
    {'Center Name': 'Borden Avenue Veterans Residence', 
     'Address': '21-10 Borden Ave, Long Island City, NY 11101', 
     'Borough': 'Queens',
     'Latitude': 40.74019459268401, 
     'Longitude': -73.94939185676857,
     'Phone Number': '718-784-5690',
     'CUNY Recommended': None },
    
    {'Center Name': 'Homes For the Homeless', 
     'Address': '17515 Rockaway Blvd, Jamaica, NY 11434', 
     'Borough': 'Queens',
     'Latitude': 40.657853043576424, 
     'Longitude': -73.76939004867276,
     'Phone Number': '718-244-0670',
     'CUNY Recommended': None },
    
    {'Center Name': 'Restfull Nights Organization', 
     'Address': '106-38 150th St, South Jamaica, NY 11435', 
     'Borough': 'Queens',
     'Latitude': 40.69501679423713, 
     'Longitude': -73.80121031501137,
     'Phone Number': '718-954-5744',
     'CUNY Recommended': None },
    
    {'Center Name': 'Fairfield Inn (North Star)', 
     'Address': '52-34 Van Dam St, Long Island City, NY 11101', 
     'Borough': 'Queens',
     'Latitude': 40.73616784972075, 
     'Longitude': -73.93668777833439,
     'Phone Number': '718-389-7700',
     'CUNY Recommended': None },
    
]

homeless_queens_colleges = []
df_homeless_queens = pd.concat([pd.DataFrame(new_queens_rows)], ignore_index=True)
for index, location in df_homeless_queens.iterrows():
    closest_school = find_closest_school(location, Queens_College['School Name_Longitude_Latitude'])
    # print(f"The closest school to {location['Center Name']} is {closest_school}")
    homeless_queens_colleges.append([location['Center Name'], closest_school])

homeless_queens_colleges_array = np.array(homeless_queens_colleges)
df_homeless_queens_colleges = pd.DataFrame(homeless_queens_colleges_array, columns=['Center Name', 'Closest College'])
df_Queens_Help = pd.merge(df_homeless_queens_colleges, df_homeless_queens)

# FILL ALL NAN VALUES IN CUNY RECOMMENDED COL
df_Queens_Help.fillna({'CUNY Recommended' : 0}, inplace=True)

# ***************************
# DF_MANHATTAN_HELP COMPLETED ********
# DF_BRONX_HELP COMPLETED *********
# DF_BROOKLYN_HELP COMPLETED ********
# DF_STATEN_ISLAND_HELP COMPLETED *******
# DF_QUEENS_HELP COMPLETED ********
# ^^^^ USED FOR PROGRESS TRACKING ^^^^

# LASTLY CREATE THE FULL DATA SET OF SHELTERS FOR 
# ALL 5 BOROUGHS WITH CUNY SCHOOLS BY CONCATING!
Full_Boroughs_Dataset = pd.concat([
    df_Manhattan_Help, 
    df_Bronx_Help, 
    df_Brooklyn_Help, 
    df_Queens_Help, 
    df_Staten_Island_Help
], axis=0, ignore_index=True)
