import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/dashboard-v3/master/data/us-population-2010-2019.csv')
df

new_columns = ['states', 'states_code', 'id', '2010', '2011', '2012', '2013', '2014', '2015', '2016',
       '2017', '2018', '2019']
df = df.reindex(columns=new_columns)
df

states_abbreviation = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
    "District of Columbia": "DC",
    "American Samoa": "AS",
    "Guam": "GU",
    "Northern Mariana Islands": "MP",
    "Puerto Rico": "PR",
    "United States Minor Outlying Islands": "UM",
    "U.S. Virgin Islands": "VI",
}

# invert the dictionary
# abbrev_to_us_state = dict(map(reversed, us_state_to_abbrev.items()))

df['states_code'] = [states_abbreviation[x] for x in df.states]
df

# Save data to CSV
df.to_csv('us-population-2010-2019-states-code.csv', index=False)
# Reshape the DataFrame
df_reshaped = pd.melt(df, id_vars=['states', 'states_code', 'id'], var_name='year', value_name='population')

# Convert 'year' column values to integers
df_reshaped['states'] = df_reshaped['states'].astype(str)
df_reshaped['year'] = df_reshaped['year'].astype(int)
df_reshaped['population'] = df_reshaped['population'].str.replace(',', '').astype(int)

df_reshaped
