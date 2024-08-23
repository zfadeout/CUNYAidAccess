import numpy as np

# Haversine function to calculate distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in kilometers
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    
    a = np.sin(delta_phi / 2)**2 + np.cos(phi1) * np.cos(phi2) * np.sin(delta_lambda / 2)**2
    c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))
    return R * c

# Function to find the closest school
def find_closest_school(location, school_map):
    min_distance = float('inf')
    closest_school = None
    
    # print(f"\nDistances from {location['Borough']}:")
    
    # iterate through the list of schools items
    for school, (school_lat, school_lon) in school_map.items():
        
        # calculate distance using haversine function
        distance = haversine(location['Latitude'], location['Longitude'], school_lat, school_lon)
        
        # TESTING
        # print(f"Distance to {school}: {distance:.2f} km")
        
        # swap until we find the closest school for specific location/rat
        if distance < min_distance:
            min_distance = distance
            closest_school = school
    
    return closest_school 

# PRINT FUNCTION FOR TXT FILES USED FOR ANALYSIS
def print_shelter_details(df, College):
    for index, row in df.iterrows():
        print(f"Center Name: {row['Center Name']}")
        print(f"Address: {row['Address']}")
        print(f"Borough: {row['Borough']}")
        print(f"Near {College}")
        print(f"{row['mi']:.2} Miles Away")
        # print(f"Latitude: {row['Latitude']}")
        # print(f"Longitude: {row['Longitude']}")
        print(f"Phone Number: {row['Phone Number']}")
        print(f"CUNY Recommended: {row['CUNY Recommended']}")
        print("-" * 40)  # Separator line for better readability
