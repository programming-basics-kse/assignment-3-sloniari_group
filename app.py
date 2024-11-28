import pandas as pd
import sys

print(sys.argv[0])

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
    print(df_countries)
    
totalProcess()


