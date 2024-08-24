import pandas as pd
import numpy as np
from CUNY_DOES_CARE import Full_Boroughs_Dataset, All_Cuny_Colleges, college_df
from CUNY_FUNCTIONS import haversine, print_shelter_details

baruch_college_lat = 40.740471862767045
baruch_college_lon = -73.98320075070929

All_Shelter_Names = Full_Boroughs_Dataset[['Center Name', 'Latitude', 'Longitude', 'Phone Number', 'CUNY Recommended', 'Address', 'Borough']]

df_homeless_manhattan = Full_Boroughs_Dataset[['Borough', 'Center Name', 'Address', 'Latitude', 'Longitude', 'Phone Number', 'CUNY Recommended']].copy()
df_homeless_manhattan = df_homeless_manhattan[df_homeless_manhattan['Borough'] == 'Manhattan']

# Convert the latitudes and longitudes to float
df_homeless_manhattan['Latitude'] = df_homeless_manhattan['Latitude'].astype(float)
df_homeless_manhattan['Longitude'] = df_homeless_manhattan['Longitude'].astype(float)

Full_Boroughs_Dataset['mi'] = Full_Boroughs_Dataset.apply(
    lambda row: haversine(baruch_college_lat, baruch_college_lon, row['Latitude'], row['Longitude']), axis=1
)

Full_Boroughs_Dataset = Full_Boroughs_Dataset.sort_values(by='mi')
# print(Full_Boroughs_Dataset.iloc[0:5])

# print_shelter_details(df_homeless_manhattan.iloc[0:5], 'Baruch College')

    
# HELPER FUNCTION
def iterating_through_col(college):
    df_baruch = college_df[college_df['College Name'] == college]
    gr1 = df_baruch[['College Name', 'Latitude', 'Longitude']].reset_index(drop=True)
    # repeat first row 49 times for each shelter to calculate for [mi] row
    if not gr1.empty:
        gr1 = pd.concat([gr1.iloc[[0]]] * 49, ignore_index=True)

    # create new column named [mi] with distance in miles calculated using haversine function
    gr1['mi'] = Full_Boroughs_Dataset.apply(
        lambda row: haversine(gr1['Latitude'].iloc[0], gr1['Longitude'].iloc[0], row['Latitude'], row['Longitude']), axis=1
    )
        
    # Match the index with the All_Shelter_Names DataFrame
    gr1.index = All_Shelter_Names.index
    
    # Concatenate with All_Shelter_Names to include shelter information
    final_df = pd.concat([gr1, All_Shelter_Names[['Center Name', 'Phone Number', 'CUNY Recommended', 'Address', 'Borough']]], axis=1)

    # SORT VALUES BY mi COLUMN
    final_df = final_df.sort_values(by='mi')

    # TAKING TOP 5 CLOSEST SHELTERS
    return final_df[0:5]

print(iterating_through_col('Baruch College'))

Bolleges = {'Baruch College' : (40.740471862767045, -73.98320075070929),
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
    'York College' : (40.70104134897624, -73.79610986464256)}

# LINE OF CODE FOR FORMATING TXT FILE
# for college in list(Bolleges.keys()):
#     print_shelter_details(iterating_through_col(college), college)

# LINE OF CODE FOR CREATING INDIVIDUAL CSV FILES FOR EACH COLLEGE
for college in list(Bolleges.keys()):
    df = iterating_through_col(college)
    df.to_csv(f'Help From {college}.csv')


    
