import pandas as pd
import sys

def totalProcess():
  
  if(sys.argv[1] == "-total" 
  and int(sys.argv[2]) >= 1896
  and int(sys.argv[2]) <= 2016):
    year = int(sys.argv[2])
    medals =["Gold", "Silver", "Bronze"]
    
    file_path = './dataSet/data.csv'
    file = pd.read_csv(file_path)
    
    df_year = file[file["Year"] == year]
    df_medals = df_year[df_year['Medal'].isin(medals)]
    df_countries = df_medals[df_medals['Team']]
    
    medal_counts = (
      df_medals.groupby(['Team', 'Medal'])
      .size()
      .unstack(fill_value=0)
    )
    for team, counts in medal_counts.iterrows():
      print(f"{team} - золото: {counts['Gold']} - серебро: {counts['Silver']} - бронза: {counts['Bronze']}")
    
totalProcess()


